# Textbook breakdowns

Tooling for `src/main/md/deep-dives/textbooks/`. Each book there is broken down book → chapter → section, and each section points to its page range in the Drive PDF.

1. `tool.py extract SLUG PDF` caches per-page text and the PDF outline.
2. `tool.py outline SLUG`, `heads SLUG`, `pages SLUG A B N` show the structure; `tool.py build SLUG [skip titles]` turns the outline into `structure.json` (or write it by hand).
3. `tool.py digest SLUG` prints a short digest per section to write summaries from.
4. `assemble(slug, meta, chapter_summaries, section_summaries)` (in `tool.py`) writes `book.json` and renders the page.
5. Add the book to `registry.json` (slug, work dir, subject, title, author, one-line blurb) and its Drive file ID to `ids.json`, then run `publish.py` from the repo root to copy pages and regenerate the hub.

Summaries are always in our own words; no book text is reproduced.

## What to include

- **Superseded books are skipped.** When a newer edition or version is on the shelf, only that one is broken down (Lean 4 books over *Programming in Lean* for Lean 3; Harper's second edition over the first).
- **Marketing samples are skipped.** Publisher previews and free samples with only a chapter or two of a long book add little (dropped so far: Barendregt's *Lambda Calculus* preview, the *Thinking with Types* sample, the opening of Yanofsky's *Monoidal Category Theory*). Substantial excerpts and unfinished drafts are kept and marked as partial.
- **Terms per section.** Every section gets a short list of the terms a question would use (named results, methods, notation). These feed the subject skills.

## Subject skills (planned)

One skill per subject, not per book: its SKILL.md routes between the books (which book for which kind of question, at what level), and a generated reference file per book carries the chapter/section table, terms, page ranges, Drive ID and caveats, from `books/<slug>.json`. The book text stays in Drive, so answering from a passage means opening that page range in the PDF.

## Queue

Order: smallest first, text-extractable before scans. DNS Bhat books are excluded (covered in full elsewhere on the site).

Needs OCR (deferred): uchinaaguchi-martial-arts-handbook-v1, Dravidian Gods in Modern Hinduism (spaced-out OCR layer), Sato's Algebraic Topology, Schey's Div Grad Curl, Ramanujan's Kannada grammar, hu2, Shilov's Linear Algebra, Cohn's Universal Algebra, the Rig-Veda scan, slpj-book-1987, Pierce's ATTAPL.
