---
name: ettuge-content-qa
description: >
  Answers questions about Vishwas's personal knowledge base across three sections
  of the ettuge site: Books (89+ influential books with full summaries), Functional
  Programming (Haskell, Scala, ZIO, category theory notes), and Reflection (20
  topic files covering AI/ML, Kannada, mathematics, history, health, martial arts,
  cricket, travel, and more — distilled from years of Signal bookmarks).
  Use this skill when asked about: books Vishwas has read, book recommendations
  on a topic, what the FP notes say about Haskell/Scala/ZIO/category theory,
  or any question about topics in the Reflection notes (what do your notes say
  about X, recommend something from your reading on Y, what have you saved about Z).
  Triggers on phrases like: "what books", "recommend a book on", "your notes on",
  "what did you save about", "your reflection on", "books you've read about",
  "FP notes", "Haskell question", "what's in your knowledge base about".
---

# ettuge Content Q&A

You answer questions about Vishwas's personal knowledge base in the ettuge
repository at `~/code/ettuge/src/main/md/`. The three sections are Books, FP,
and Reflection.

## Repository Root

`/Users/vishwas/code/ettuge/src/main/md/`

---

## Section 1 — Books

**Index files:**
- `Books/Books.md` — master index, books by author with inline summaries
- `Books/Books-Top.md` — Modern Library Top 100 novels list with summaries

**Individual book files** (89+ files):
- `Books/influential/<slug>.md` — each has: Summary, Critical Takeaways, My Takeaways

**How to answer Books questions:**

1. For "what books have you read about X?" — grep `Books/Books.md` for the topic,
   then read the matching influential/ file for depth.
2. For "tell me about [book title]" — glob `Books/influential/` for the slug,
   read the file.
3. For "recommend a book on X" — search `Books/Books.md` for thematic matches,
   surface 2–3 with their summaries and why they're relevant.
4. Always cite: title, author, and at least one "My Takeaway" if available.

**Categories in Books.md:** Western Fiction, Kannada/Indian Literature, Indian
Classical Texts, D. N. Shankara Bhat linguistics works, Science & Biology,
History & Biography, Math & Computing, Martial Arts & Physical Practice,
Economics & Ideas.

---

## Section 2 — Functional Programming (FP)

**Primary files:**
- `pl/FP.md` — main FP essay: personal journey from C++ templates → Lisp → ML →
  Haskell → Scala; covers SICP, ZIO, Kyo, category theory
- `haskell/reflection.md` — Haskell reflection session notes
- `haskell/hsom.md` — Haskell School of Music notes
- `haskell/monoids-and-semigroups.md` — algebraic structures in Haskell
- `haskell/qsortof.md`, `haskell/qsortof-part2.md` — quicksort exploration
- `haskell/rangapura-conversation.md` — music/Haskell composition conversation
- `haskell/ಕಳ್ಳ.md` — Kannada-named Haskell file (small programs)
- `pl/ॐλ.md` — lambda calculus / philosophy note

**How to answer FP questions:**

1. Read `pl/FP.md` for the overall journey and Scala/ZIO/Kyo perspective.
2. Read the specific `haskell/` file for Haskell-specific questions.
3. For category theory questions, check `haskell/monoids-and-semigroups.md`
   and `pl/FP.md`.
4. Answer in the context of Vishwas's actual experience — he has TA'd Haskell
   courses, worked with ZIO/Kyo professionally, and approaches FP through the
   lens of effect systems and type theory.

---

## Section 3 — Reflection Notes

**All files:** `self-reflection/2026-02-25_<topic>.md`

**Published topics (20):**

| File | Title | Content |
|------|-------|---------|
| `kannada.md` | Kannada | DNS Bhat grammar, Dravidian linguistics, Karnataka culture |
| `japanese.md` | Japanese | Language, script systems, grammar, resources |
| `linguistics.md` | Linguistics | Typology, phonology, historical linguistics |
| `sanskrit.md` | Sanskrit | Grammar, literature, subhāṣitas |
| `indian-history-culture.md` | Indian History | Harappan, ancient/medieval India, genetics |
| `scala-functional-programming.md` | Scala & FP | ZIO, Scala 3, Kyo, Haskell, code snippets |
| `machine-learning-ai.md` | ML & AI | LLMs, RAG, transformers, Indic LLMs |
| `mathematics.md` | Mathematics | Pure math, proofs, number theory |
| `mathematics-science.md` | Math & Science | Applied math, physics, biology, geology |
| `world-history-archaeology.md` | World History | Global prehistory, ancient civilisations |
| `algorithms-data-structures.md` | Algorithms | LeetCode (Scala), CRDTs, compiler design |
| `infrastructure-devops.md` | Infra & DevOps | Nix, Kubernetes, Terraform, Rust CLI |
| `data-engineering.md` | Data Engineering | Spark, Flink, Hudi, lakehouse |
| `health-fitness.md` | Health & Fitness | VO2 max, climbing, nutrition, cold exposure |
| `martial-arts.md` | Martial Arts | Okinawan karate, judo, grappling, kata |
| `books-literature.md` | Books & Literature | Reading lists, literary essays |
| `arts-music-film.md` | Arts, Music & Film | Music, cinema, visual art |
| `cricket-sports.md` | Cricket & Sports | IPL, match analysis, players |
| `travel-outdoors.md` | Travel & Outdoors | Treks, adventure sports, Bay Area |
| `miscellaneous.md` | Miscellaneous | Retired stub |

**Also available (not published publicly):**
- `career-personal.md` — Career, PKM, personal philosophy
- `current-events-politics.md` — US/India politics, geopolitics

**Entry format in each file:**
```
**Bold heading** — 2–4 sentence prose description.
**[→ primary-category; cross-link → other-category]**
URL
```

**How to answer Reflection questions:**

1. Identify the right topic file(s) from the table above.
2. Read the file and search for relevant entries (grep for keywords).
3. Surface 2–4 matching entries with their prose descriptions.
4. If the topic spans multiple files, read all relevant ones.
5. Always include the URL from the entry so Vishwas can follow up.

---

## Answering Strategy

1. **Identify the section** — is this a Books, FP, or Reflection question?
2. **Read the right files** — use Read/Glob/Grep on the paths above.
3. **Be specific** — quote summaries, My Takeaways, or entry descriptions directly.
4. **Give the GitHub Pages link** where relevant:
   - Books: `https://vwulf.github.io/ettuge/Books/`
   - FP: `https://vwulf.github.io/ettuge/FP/`
   - Reflection: `https://vwulf.github.io/ettuge/Reflection/<topic>.html`
5. **For cross-section questions** — e.g. "books AND notes on X" — search both.
6. **Cite your source** — say which file you read and where in it you found the answer.

---

## Example Interactions

**Q: "What books have you read about India?"**
→ Grep `Books.md` for "India", "Indian", "Harappan"; read matching influential/ files; return 3–5 with author + My Takeaway.

**Q: "What do your notes say about Nix?"**
→ Read `self-reflection/2026-02-25_infrastructure-devops.md`; grep for "Nix"; return matching entries with URLs.

**Q: "Tell me about your FP journey"**
→ Read `pl/FP.md` in full; summarize the arc from C++ → Lisp → ML → Haskell → ZIO/Kyo.

**Q: "Recommend something on Haskell music"**
→ Read `haskell/hsom.md` and `haskell/rangapura-conversation.md`; surface relevant content.

**Q: "What have you saved about cold exposure?"**
→ Read `self-reflection/2026-02-25_health-fitness.md`; grep for "cold"; return entries.
