# Textbook breakdowns

Tooling for `src/main/md/deep-dives/textbooks/`. Each book there is broken down book → chapter → section, and each section points to its page range in the Drive PDF.

1. `tool.py extract SLUG PDF` caches per-page text and the PDF outline.
2. `tool.py outline SLUG`, `heads SLUG`, `pages SLUG A B N` show the structure; `tool.py build SLUG [skip titles]` turns the outline into `structure.json` (or write it by hand).
3. `tool.py digest SLUG` prints a short digest per section to write summaries from.
4. `assemble(slug, meta, chapter_summaries, section_summaries)` (in `tool.py`) writes `book.json` and renders the page.
5. Add the book to `registry.json` (slug, work dir, subject, title, author, one-line blurb) and its Drive file ID to `ids.json`, then run `publish.py` from the repo root to copy pages and regenerate the hub.

Summaries are always in our own words; no book text is reproduced.

## Queue

Order: smallest first, text-extractable before scans. DNS Bhat books are excluded (covered in full elsewhere on the site).

Needs OCR (deferred): uchinaaguchi-martial-arts-handbook-v1, Sato's Algebraic Topology, Schey's Div Grad Curl, Ramanujan's Kannada grammar, hu2, Shilov's Linear Algebra, Cohn's Universal Algebra, the Rig-Veda scan, slpj-book-1987, Pierce's ATTAPL.
