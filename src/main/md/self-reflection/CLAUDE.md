# Self-Reflection Directory — CLAUDE.md

This directory contains topic-based derivatives of `self.md` and `self-1.md`, personal notes files (Signal channel "self" export, 2021–2026) not stored in the repository. Each entry has been enriched with a 2–4 sentence prose description and a `[→ category]` routing hint.

---

## Structure

- **`README.md`** — Project recap covering the three phases: cleanup → categorize → enrich+split.
- **`index.md`** — Master navigation index listing all topic files with descriptions.
- **`YYYY-MM-DD_topic.md`** — Individual topic files, all derived from `self.md`/`self-1.md` on 2026-02-25.

### Current Topic Files

| File | Topic |
|------|-------|
| `2026-02-25_scala-functional-programming.md` | ZIO, Scala 3, Kyo, Haskell, functional effects, type theory |
| `2026-02-25_machine-learning-ai.md` | LLMs, RAG, fine-tuning, Indic LLMs, AI infrastructure |
| `2026-02-25_kannada-language-linguistics.md` | Kannada script, DNS Bhat grammar, Dravidian linguistics, Karnataka culture |
| `2026-02-25_indian-history-culture.md` | Harappan genetics, Indus script, ancient/medieval India, prehistory |
| `2026-02-25_infrastructure-devops.md` | Nix, AWS, Kubernetes, CI tools, EVs |
| `2026-02-25_algorithms-data-structures.md` | LeetCode (Scala), Knight's Tour, system design |
| `2026-02-25_health-fitness.md` | VO2 max, climbing, martial arts, nutrition, cold exposure |
| `2026-02-25_mathematics-science.md` | Riemann hypothesis, Langlands, category theory, biology, geology |
| `2026-02-25_data-engineering.md` | Spark, system design, Kannada data pipeline (alar.ink) |
| `2026-02-25_books-literature.md` | Books read, reading lists, literary essays, reviews |
| `2026-02-25_arts-music-film.md` | Music, cinema, documentaries, visual art, performance |
| `2026-02-25_travel-outdoors.md` | Hiking, adventure sports, Bay Area food, extreme sports |
| `2026-02-25_cricket-sports.md` | Match commentary, IPL analysis, player profiles, sports analytics |
| `2026-02-25_current-events-politics.md` | US/India politics, immigration, geopolitics, civil rights |
| `2026-02-25_career-personal.md` | Career, self-development, personal philosophy, PKM, AI tools |
| `2026-02-25_miscellaneous.md` | **Retired stub** — all content redistributed to the 16 files above |

---

## Rules for This Directory

1. **Enrichment format:** each entry = `**Bold heading**` → 2–4 sentence prose → `**[→ category; cross-link → other-category]**` → URL.
2. **Naming convention:** `YYYY-MM-DD_topic-slug.md` — date reflects when the file was derived.
3. **Cross-linking:** if a note fits multiple categories, it lives in the most specific file and cross-links to others using the `[→]` tag.
4. **`miscellaneous.md`** is retired — all residual entries have been moved to the 16 topic files.
5. **`index.md`** must be kept in sync whenever new topic files are added.

---

## Adding New Topic Files

When deriving new files from updated `self.md`/`self-1.md` content:
1. Use the date of derivation as the filename prefix (`YYYY-MM-DD`).
2. Add a frontmatter block with `title`, `created`, and `source`.
3. Group by primary subject domain.
4. Add a row to the table in `index.md` and this `CLAUDE.md` table above.
