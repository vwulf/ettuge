# Brief: writing book entries for Vishwas's reading catalog (ettuge site)

You are writing content for a personal reading catalog at https://vwulf.github.io/ettuge/Books/Books.html
(source: src/main/md/Books/Books.md). Read src/main/md/Books/Books.md and two files in
src/main/md/Books/influential/ (e.g. disgrace.md, the-language-instinct.md) first to match tone and depth.

Your input is a JSON list of items (id, author, title, and maybe partial/format) at the path given in your task.
Titles/authors came from OCR of photos and can be slightly off — correct them to the real, canonical title and
author (e.g. "Prabha Duneja" stays, "Atavakriagita" -> "Ashtavakra Gita"). Some are Kannada books (keep the
Kannada script name in parentheses, e.g. "Kavalu (ಕವಲು)"), martial-arts manuals, small booklets, field guides.

## Accuracy rules (most important)
- Write only what you are confident is true. No invented plot points, quotes, awards, dates, or reviewers.
- For obscure items (local Kannada titles, booklets, regional guides, self-published martial arts books) keep it
  short and general, and say plainly when critical coverage is limited ("Little published criticism exists; ...").
- Use WebSearch to check any item you are not sure about (author, year, what the book is). Don't guess.
- Never write first-person takeaways or opinions as Vishwas. Critics' views = the book's published reception
  and the main points reviewers/scholars make, attributed generally ("Reviewers praised...", "Critics note...").
- If an item is not actually a book or is clearly a duplicate of another item in your list, set "skip": true with a "skip_reason".

## Output
Write ONE JSON file (a list, same order as input, one object per input id) to the output path in your task,
using the Write tool. Validate it parses (python3 -c "import json;json.load(open(PATH))").
Keep "id" exactly as given. Common fields for every object:
- "id", "title" (canonical), "author" (canonical), "published" (year as string, or "" if unsure)
- "skip" (bool, default false), "skip_reason" (string, optional)

Books categories (use exactly one for "category"):
Fiction (World Literature) | Indian Fiction in English | Kannada Literature | Indian Classical and Spiritual Texts |
D. N. Shankara Bhat and Kannada Linguistics | Science and Biology | History and Biography | Indian History and Society |
Mathematical and Computing Thought | Martial Arts and Physical Practice | Outdoors, Climbing and Travel |
Economics, Politics, and Ideas | Business, Self-help and Psychology | Language Study and Reference | Comics and Humor |
Food and Lifestyle

### Kind "full" (influential/read books get their own page)
- "category"
- "index_summary": 2–4 sentences, like the Summary cells in Books.md (what the book is + why it matters).
- "summary_md": 2–3 paragraphs of markdown (like the "## Summary" section in the influential files).
- "critical": list of 4–5 strings, each "**Short label:** one or two sentences" (objective critical analysis /
  reception, like "## Critical Takeaways").
- "sources": list of {"label","url"} — only URLs you are confident exist (Wikipedia article for the book or
  author, publisher page, Goodreads search is OK as "https://www.goodreads.com/search?q=TITLE+AUTHOR" urlencoded).

### Kind "critics" (unread books — index row only)
- "category"
- "critics_take": 2–3 sentences: what the book is, then how critics/readers received it. No first person.

### Kind "tech" (textbooks / technical books)
- "path": two-level subject path as a list, top level one of:
  Mathematics | Computer Science | AI and Machine Learning | Physics and Engineering | Linguistics and Languages | Other
  Second level, e.g. Mathematics: Foundations and Logic, Algebra, Category Theory, Topology and Geometry,
  Analysis and Linear Algebra, Discrete Mathematics and Combinatorics, Probability and Statistics, Recreational Mathematics;
  Computer Science: Programming Languages and Type Theory, Functional Programming, Compilers and Language Implementation,
  Algorithms and Data Structures, Theory of Computation, Operating Systems and Systems Programming,
  Networks and Security, Distributed and Data Systems, Computer Architecture and Parallelism, Software Design and Engineering,
  Interviews and Career; AI and Machine Learning: Foundations, Deep Learning, Applied ML; etc. Keep second levels few and reusable.
- "summary": 1–2 sentences: what it covers and its standing (e.g. "the standard graduate text", "known for ...").
- "edition": edition string if the input mentions one, else "".
- If an item is not technical at all (a novel, a memoir), still fill it with path ["Other","Not technical"].
