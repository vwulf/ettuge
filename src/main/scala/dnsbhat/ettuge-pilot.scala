//> using scala 3.6.4
//> using dep com.softwaremill.sttp.client4::core:4.0.3
//> using dep com.softwaremill.sttp.client4::zio-json:4.0.3
//> using dep dev.zio::zio-json:0.7.3

import sttp.client4.*
import sttp.client4.ziojson.*
import zio.json.*

import java.nio.file.{Files, Paths, StandardOpenOption}
import java.nio.charset.StandardCharsets

// ── Groq API types ──────────────────────────────────────────────

case class ChatMessage(role: String, content: String) derives JsonEncoder, JsonDecoder

case class ChatRequest(
    model: String,
    messages: Seq[ChatMessage],
    temperature: Double,
    max_tokens: Int
) derives JsonEncoder

case class Choice(index: Int, message: ChatMessage) derives JsonDecoder
case class Usage(prompt_tokens: Int, completion_tokens: Int, total_tokens: Int) derives JsonDecoder
case class ChatResponse(choices: Seq[Choice], usage: Option[Usage]) derives JsonDecoder

// ── Configuration ───────────────────────────────────────────────

object Config:
  val groqApiKey: String   = sys.env.getOrElse("GROQ_API_KEY", throw RuntimeException("Set GROQ_API_KEY env var"))
  val model: String        = "qwen-qwen3-32b"
  val batchSize: Int       = 20
  val temperature: Double  = 0.3
  val maxTokens: Int       = 4000
  val outputFile: String   = "pilot-results.jsonl"
  val promptFile: String   = "DNS_BHAT_WORD_FORMATION_PROMPT.md"

// ── Pilot word list (200 words across difficulty tiers) ─────────

object PilotWords:

  // Category A: Words with likely existing native equivalents (~80 words)
  val categoryA: Seq[String] = Seq(
    "water", "fire", "earth", "wind", "sky", "sun", "moon", "star", "rain", "cloud",
    "tree", "flower", "seed", "root", "leaf", "fruit", "stone", "sand", "river", "lake",
    "mountain", "forest", "field", "village", "house", "door", "wall", "roof", "path", "bridge",
    "mother", "father", "child", "brother", "sister", "friend", "enemy", "king", "thief", "farmer",
    "head", "eye", "ear", "nose", "mouth", "hand", "foot", "heart", "blood", "bone",
    "food", "milk", "salt", "oil", "rice", "bread", "meat", "fish", "egg", "honey",
    "day", "night", "morning", "evening", "year", "winter", "summer", "spring", "cold", "hot",
    "big", "small", "old", "new", "good", "bad", "long", "short", "heavy", "light"
  )

  // Category B: Words needing suffix-derived coinages (~60 words)
  val categoryB: Seq[String] = Seq(
    "teacher", "student", "writer", "reader", "singer", "dancer", "player", "worker", "driver", "leader",
    "addition", "subtraction", "multiplication", "division", "measurement", "comparison", "education", "creation", "destruction", "protection",
    "happiness", "sadness", "kindness", "darkness", "brightness", "weakness", "strength", "height", "depth", "width",
    "equipment", "ornament", "instrument", "document", "monument", "supplement", "experiment", "treatment", "punishment", "nourishment",
    "bicycle", "unicorn", "triangle", "semicircle", "multilingual", "autobiography", "cooperate", "hyperactive", "underdeveloped", "forecast",
    "submarine", "international", "television", "telephone", "transcontinental", "prehistoric", "postmortem", "rewrite", "neoclassical", "paleolithic"
  )

  // Category C: Hard words needing novel compounds or creative coinage (~60 words)
  val categoryC: Seq[String] = Seq(
    "democracy", "bureaucracy", "astronomy", "biology", "geology", "psychology", "thermometer", "telescope", "microscope", "astronaut",
    "computer", "algorithm", "database", "internet", "software", "hardware", "website", "download", "upload", "server",
    "vaccine", "antibiotic", "chromosome", "ecosystem", "photosynthesis", "biodiversity", "sustainability", "infrastructure", "semiconductor", "electromagnetic",
    "feminist", "nationalist", "linguist", "botanist", "journalist", "apprentice", "refugee", "employee", "trainee", "nominee",
    "capitalism", "socialism", "globalization", "privatization", "deforestation", "urbanization", "industrialization", "decentralization", "denationalization", "demilitarization",
    "artificial intelligence", "machine learning", "neural network", "quantum computing", "renewable energy", "climate change", "human rights", "public health", "open source", "supply chain"
  )

  val all: Seq[(String, Seq[String])] = Seq(
    "A" -> categoryA,
    "B" -> categoryB,
    "C" -> categoryC
  )
end PilotWords

// ── Result type ─────────────────────────────────────────────────

case class PilotResult(
    category: String,
    batchIndex: Int,
    words: Seq[String],
    response: String,
    promptTokens: Int,
    completionTokens: Int
) derives JsonEncoder

// ── Main application ────────────────────────────────────────────

@main def run(): Unit =
  val backend = DefaultSyncBackend()

  println("═══════════════════════════════════════════════════")
  println("  ಎತ್ತುಗೆ (Ettuge) — Kannada Word Formation Pilot")
  println(s"  Model: ${Config.model} on Groq")
  println(s"  Batch size: ${Config.batchSize}")
  println(s"  Output: ${Config.outputFile}")
  println("═══════════════════════════════════════════════════")

  // Load system prompt
  val promptPath = Paths.get(Config.promptFile)
  if !Files.exists(promptPath) then
    System.err.println(s"ERROR: Prompt file not found: ${Config.promptFile}")
    System.err.println("Run from the dnsbhat directory.")
    sys.exit(1)

  val systemPrompt = String(Files.readAllBytes(promptPath), StandardCharsets.UTF_8)
  println(s"Loaded system prompt: ${systemPrompt.length} chars")

  // Delete old output file
  Files.deleteIfExists(Paths.get(Config.outputFile))

  var totalTokensIn  = 0
  var totalTokensOut = 0
  var totalWords     = 0

  for (category, words) <- PilotWords.all do
    val batches = words.grouped(Config.batchSize).toSeq
    println(s"\n── Category $category: ${words.size} words in ${batches.size} batches ──")

    for (batch, idx) <- batches.zipWithIndex do
      println(s"  Batch ${idx + 1}/${batches.size}: ${batch.take(3).mkString(", ")}...")

      val result = sendBatch(backend, systemPrompt, batch, category, idx)
      appendResult(result)

      totalTokensIn  += result.promptTokens
      totalTokensOut += result.completionTokens
      totalWords     += batch.size

      println(s"    ✓ ${result.promptTokens} in / ${result.completionTokens} out tokens")

      // Rate limiting: Groq free tier is 30 req/min for some models
      Thread.sleep(2500)
  end for

  val costIn    = totalTokensIn * 0.29 / 1_000_000.0
  val costOut   = totalTokensOut * 0.59 / 1_000_000.0
  val totalCost = costIn + costOut

  println(s"\n═══════════════════════════════════════════════════")
  println(s"  Done! $totalWords words processed")
  println(f"  Input tokens:  $totalTokensIn  ($$${costIn}%.4f)")
  println(f"  Output tokens: $totalTokensOut  ($$${costOut}%.4f)")
  println(f"  Total cost:    $$${totalCost}%.4f")
  println(s"  Results: ${Config.outputFile}")
  println(s"═══════════════════════════════════════════════════")

  backend.close()
end run

// ── HTTP / Groq ─────────────────────────────────────────────────

def buildUserPrompt(words: Seq[String], category: String): String =
  val wordList = words.zipWithIndex.map((w, i) => s"${i + 1}. $w").mkString("\n")
  val catDesc = category match
    case "A" => "likely have existing native Kannada equivalents — find and document them"
    case "B" => "need suffix-derived coinages using the rules in the system prompt"
    case "C" => "need novel compounds or creative coinages — hardest tier"
    case _   => ""
  s"""Coin native Kannada equivalents for the following English words using DNS Bhat's methodology.
     |These are Category $category words: $catDesc
     |
     |For EACH word, output a JSON object on its own line with these fields:
     |  "english": the English word
     |  "kannada": your coined Kannada word in Kannada script
     |  "romanized": romanized form
     |  "formation": morphological breakdown (root + suffix/prefix)
     |  "category": semantic role (agent, action, result, instrument, quality, compound, etc.)
     |  "sanskrit_replaced": the Sanskrit borrowing this replaces (if applicable, else null)
     |  "analogous_existing": an existing Kannada word showing the same pattern
     |  "confidence": "high" / "medium" / "low"
     |
     |Words:
     |$wordList
     |
     |Output ONLY the JSON lines, no other text. One JSON object per line.""".stripMargin

def sendBatch(
    backend: SyncBackend,
    systemPrompt: String,
    words: Seq[String],
    category: String,
    batchIndex: Int
): PilotResult =
  val userPrompt = buildUserPrompt(words, category)
  val reqBody = ChatRequest(
    model = Config.model,
    messages = Seq(
      ChatMessage("system", systemPrompt),
      ChatMessage("user", userPrompt)
    ),
    temperature = Config.temperature,
    max_tokens = Config.maxTokens
  )

  val httpReq = basicRequest
    .post(uri"https://api.groq.com/openai/v1/chat/completions")
    .header("Authorization", s"Bearer ${Config.groqApiKey}")
    .body(reqBody.toJson)
    .response(asJson[ChatResponse])

  try
    val response = httpReq.send(backend)
    response.body match
      case Right(chatResp) =>
        val text  = chatResp.choices.headOption.map(_.message.content).getOrElse("")
        val usage = chatResp.usage.getOrElse(Usage(0, 0, 0))
        PilotResult(category, batchIndex, words, text, usage.prompt_tokens, usage.completion_tokens)
      case Left(err) =>
        System.err.println(s"    ✗ API error: $err")
        PilotResult(category, batchIndex, words, s"ERROR: $err", 0, 0)
  catch
    case e: Exception =>
      System.err.println(s"    ✗ Request failed: ${e.getMessage}")
      PilotResult(category, batchIndex, words, s"EXCEPTION: ${e.getMessage}", 0, 0)

def appendResult(result: PilotResult): Unit =
  val line = result.toJson + "\n"
  Files.write(
    Paths.get(Config.outputFile),
    line.getBytes(StandardCharsets.UTF_8),
    StandardOpenOption.CREATE,
    StandardOpenOption.APPEND
  )
