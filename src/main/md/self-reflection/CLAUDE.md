# Self-Reflection Directory — CLAUDE.md

This directory contains topic-based derivatives of `self.md`, a ≈1 MB personal notes file (24,500+ lines, 2021–2024) not stored in the repository. The derivatives are read-only thematic summaries for easier navigation.

---

## Structure

- **`index.md`** — Master navigation index listing all topic files with descriptions.
- **`YYYY-MM-DD_topic.md`** — Individual topic files, all derived from `self.md` on 2026-02-25.

### Current Topic Files

| File | Topic |
|------|-------|
| `2026-02-25_scala-functional-programming.md` | ZIO, Scala 3, Kyo, Haskell, functional effects, type theory |
| `2026-02-25_machine-learning-ai.md` | LLMs, RAG, fine-tuning, Indic LLMs, AI infrastructure |
| `2026-02-25_kannada-language-linguistics.md` | Kannada script, DNS Bhat grammar, Dravidian linguistics |
| `2026-02-25_indian-history-culture.md` | Harappan genetics, Indus script, ancient/medieval India |
| `2026-02-25_infrastructure-devops.md` | Nix, AWS, Kubernetes, CI tools, EVs |
| `2026-02-25_algorithms-data-structures.md` | LeetCode (Scala), Knight's Tour, system design |
| `2026-02-25_health-fitness.md` | VO2 max, climbing, martial arts, nutrition, Garmin data |
| `2026-02-25_mathematics-science.md` | Riemann hypothesis, Langlands, category theory, biology |
| `2026-02-25_data-engineering.md` | Spark, system design, Kannada data pipeline (alar.ink) |
| `2026-02-25_miscellaneous.md` | Books, travel, culture, personal notes |

---

## Rules for This Directory

1. **These files are read-only derivatives.** Do NOT edit them directly — re-derive from `self.md` if the source changes.
2. **Naming convention:** `YYYY-MM-DD_topic-slug.md` — date reflects when the file was derived, not when the notes were written.
3. **Cross-linking:** If a note fits multiple categories, it lives in the most specific file and is cross-linked from others.
4. **Uncategorisable entries** go in `miscellaneous.md`.
5. **`index.md`** must be kept in sync whenever new topic files are added.

---

## Adding New Topic Files

When deriving new files from updated `self.md` content:
1. Use the date of derivation as the filename prefix (`YYYY-MM-DD`).
2. Add a frontmatter block with `title`, `created`, and `source: self.md (not in repository)`.
3. Group by primary subject domain.
4. Add a row to the table in `index.md`.
5. Update this `CLAUDE.md` table above.