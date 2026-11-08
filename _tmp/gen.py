#!/usr/bin/env python3
"""Generate Books.md sections, per-book pages and Technical.md from spreadsheet data + written content."""
import json, re, os, glob, unicodedata, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BK = os.path.join(ROOT, "src/main/md/Books")
data = json.load(open(os.path.join(ROOT, "_tmp/books-data.json")))
out = {}
for f in glob.glob(os.path.join(ROOT, "_tmp/out/*.json")):
    for o in json.load(open(f)):
        out[o["id"]] = o
work = {}
for f in glob.glob(os.path.join(ROOT, "_tmp/work/*.json")):
    kind = os.path.basename(f).rstrip("0123456789.json")
    for w in json.load(open(f)):
        w["kind"] = kind
        work[w["id"]] = w

def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    s = re.split(r"[(:]", s)[0]
    s = re.sub(r"^(the|a|an) ", "", s.strip())
    return re.sub(r"[^a-z0-9]", "", s)

def slug(title):
    t = re.split(r"\s*\(", title)[0] if re.search(r"[\u0c80-\u0cff]", title) else title
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    t = re.split(r":", t)[0]
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:60].strip("-") or "book"

def cover(imgs, prefix="", w=70):
    if not imgs:
        return ""
    out_ = []
    for i in imgs[:3]:
        fn = i.replace(" ", "_") + ".jpg"
        if os.path.exists(os.path.join(BK, "covers", fn)):
            out_.append(f'<img src="{prefix}covers/{fn}" width="{w}" alt="cover">')
    return " ".join(out_)

def cell(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()

books = data["books"]
for i, b in enumerate(books):
    b["id"] = f"b{i}"
tech = data["technical"]
for i, t in enumerate(tech):
    t["id"] = f"t{i}"

# ---------------------------------------------------------------- existing influential: add covers
md = open(os.path.join(BK, "Books.md")).read()
already = [b for b in books if (b["status"] or "").startswith("Already on page")]
photo_by_norm = collections.defaultdict(list)
for b in already:
    key = norm(b["title"])
    if "ibis trilogy" in (b["title"] or "").lower():
        key = norm("Ibis Trilogy")
    photo_by_norm[re.sub(r"(.)\1", r"\1", key)] += b.get("imgs") or []

def add_cover_to_row(m):
    title, path, rest = m.group(1), m.group(2), m.group(3)
    imgs = list(dict.fromkeys(photo_by_norm.get(re.sub(r"(.)\1", r"\1", norm(title)), [])))
    c = cover(imgs)
    if not c or "covers/" in rest:
        return m.group(0)
    # also put cover on the individual page
    page = os.path.join(BK, path + ".md")
    if os.path.exists(page):
        p = open(page).read()
        if "covers/" not in p:
            p = re.sub(r"^(# .*\n(?:\*\*Author:\*\*.*\n)?)", lambda mm: mm.group(1) + "\n" + cover(imgs, "../", 140) + "\n", p, count=1)
            open(page, "w").write(p)
    return f"| [{title}]({path}.md)<br>{c} |{rest}"

md = re.sub(r"^\| \[([^\]]+)\]\((influential/[^)]+)\.md\) \|(.*)$", add_cover_to_row, md, flags=re.M)
_lim = md.index("## Read but Not That Influential")
def add_cover_plain(m):
    title, rest = m.group(1), m.group(2)
    if title.strip() in ("Book",) or title.startswith("-"):
        return m.group(0)
    c = cover(list(dict.fromkeys(photo_by_norm.get(re.sub(r"(.)\1", r"\1", norm(title)), []))))
    return f"| {title}<br>{c} |{rest}" if c else m.group(0)
md = re.sub(r"^\| ([^\[|<][^|]*?) \|(.*)$", add_cover_plain, md[:_lim], flags=re.M) + md[_lim:]

# ---------------------------------------------------------------- pages
TODO = "_To be written — Vishwas's personal takeaways._"

def write_page(folder, o, b, partial):
    s = slug(o["title"])
    path = os.path.join(BK, folder, s + ".md")
    n = 2
    while os.path.exists(path) and folder == "read" and s in written_slugs:
        path = os.path.join(BK, folder, f"{s}-{n}.md"); n += 1
    written_slugs.add(os.path.basename(path)[:-3])
    meta = f"**Author:** {o['author']}" + (f" | **Published:** {o['published']}" if o.get("published") else "")
    if partial:
        meta += " | **Status:** partially read"
    parts = [f"# {o['title']}", meta, "", cover(b.get("imgs"), "../", 140), "", "---", "", "## Summary", "", o["summary_md"].strip(), "",
             "---", "", "## Critical Takeaways", ""]
    parts += [f"- {c}" for c in o.get("critical", [])]
    parts += ["", "---", "", "## My Takeaways", "", TODO, ""]
    if o.get("sources"):
        parts += ["---", "", "## Footnotes", ""] + [f"- [{x['label']}]({x['url']})" for x in o["sources"]] + [""]
    open(path, "w").write("\n".join(p for p in parts if p is not None))
    return f"{folder}/{os.path.basename(path)[:-3]}"

written_slugs = set(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(BK, "influential/*.md")))
os.makedirs(os.path.join(BK, "read"), exist_ok=True)

def group_rows(items):
    g = collections.OrderedDict()
    for it in sorted(items, key=lambda x: (x[0], x[1])):
        g.setdefault(it[0], []).append(it[2])
    return g

new_inf, read_rows, unread_rows, skipped = [], [], [], []
for b in books:
    w = work.get(b["id"])
    if not w:
        continue
    o = out.get(b["id"])
    if not o:
        skipped.append((b["title"], "no content")); continue
    if o.get("skip"):
        skipped.append((b["title"], o.get("skip_reason", ""))); continue
    partial = (b["read"] or "").strip() == "R (partial)"
    tag = " *(partially read)*" if partial else ""
    lib = " *(library copy)*" if "Library checkout" in (b["status"] or "") else ""
    c = cover(b.get("imgs"))
    c = f"<br>{c}" if c else ""
    if w["kind"] in ("inf", "read"):
        folder = "influential" if w["kind"] == "inf" else "read"
        link = write_page(folder, o, b, partial)
        if w["kind"] == "inf":
            row = f"| [{cell(o['title'])}]({link}.md){tag}<br>*{cell(o['author'])}*{c} | {cell(o['index_summary'])} |"
            new_inf.append((o["category"], o["title"], row))
        else:
            row = f"| [{cell(o['title'])}]({link}.md){tag}{lib}{c} | {cell(o['author'])} | {cell(o['index_summary'])} |"
            read_rows.append((o["category"], o["title"], row))
    else:
        row = f"| {cell(o['title'])}{lib}{c} | {cell(o['author'])} | {cell(o['critics_take'])} |"
        unread_rows.append((o["category"], o["title"], row))

def render(groups, head):
    s = []
    for cat, rows in groups.items():
        s += [f"### {cat}", "", head, "|------|--------|---------|"] + rows + ["", "---", ""]
    return "\n".join(s)

HEAD_ALIAS = {"Indian Classical and Spiritual Texts": "Indian Classical Texts",
              "D. N. Shankara Bhat and Kannada Linguistics": "D. N. Shankara Bhat"}
inf_block = ""
for cat, title, row in sorted(new_inf, key=lambda x: (x[0], x[1])):
    h = HEAD_ALIAS.get(cat, cat)
    lim = md.index("## Read but Not That Influential")
    m = re.search(rf"^### {re.escape(h)}\n\n\| Book \| Summary \|\n\|[-|]+\|\n((?:\|.*\n)+)", md[:lim], flags=re.M)
    if m:
        md = md[:m.end()] + row + "\n" + md[m.end():]
    else:
        md = md[:lim] + f"### {h}\n\n| Book | Summary |\n|------|---------|\n{row}\n\n---\n\n" + md[lim:]

read_block = ("## Read but Not That Influential\n\n"
    "Books I have read (or partly read) and valued, but which haven't reshaped how I think the way the books above have. "
    "Each links to a page with a summary and the critics' take; personal takeaways are still to be written.\n\n---\n\n"
    + render(group_rows(read_rows), "| Book | Author | Summary |"))
unread_block = ("## On the Shelf — Not Yet Read\n\n"
    "Books I own (or borrowed) but haven't read yet. For these I note only what critics and readers have said.\n\n---\n\n"
    + render(group_rows(unread_rows), "| Book | Author | Critics' Take |"))

start = md.index("## Read but Not That Influential")
end = md.index("## Want to Read")
md = md[:start] + inf_block.replace("### Added", "### Added", 1) + read_block + unread_block + md[end:]
# move the new-influential block to sit inside the Influential section (it already is: just before Read section)
md = md.replace("A cataloged index of books that have shaped how I think, organized by author.",
    "A cataloged index of my books, in three groups: **Influential** books that have shaped how I think, "
    "**Read** books that I valued but that were less formative, and books **On the Shelf** that I haven't read yet. "
    "Textbooks have their own catalog: [Technical](Technical.md).\n\nWithin the influential section, books are organized by author.", 1)
md = md.replace("*See also: [Books-Top.md](Books-Top)", "*See also: [Technical](Technical.md) — textbooks, physical and digital. [Books-Top.md](Books-Top)", 1)
open(os.path.join(BK, "Books.md"), "w").write(md)

# ---------------------------------------------------------------- Technical.md
tree = collections.OrderedDict()
TOP = ["Mathematics", "Computer Science", "AI and Machine Learning", "Physics and Engineering", "Linguistics and Languages", "Other"]
for t in tech:
    o = out.get(t["id"])
    if not o or o.get("skip"):
        if o: skipped.append((t["title"], o.get("skip_reason", "")))
        continue
    top, sub = (o.get("path") or ["Other", "Miscellaneous"]) + ["Miscellaneous"] * (2 - len(o.get("path") or []))
    fmt = work[t["id"]]["format"]
    tree.setdefault(top, collections.OrderedDict()).setdefault(sub, []).append((o, t, fmt))
merged = collections.defaultdict(dict)  # merge same title physical+digital
lines = ["# Technical", "",
    "My textbooks and technical books — the ones on the shelf and the ones in the Google Drive *Books* folder — "
    "arranged top-down by subject. Textbooks are never really *finished*, so there is no read/unread status here; "
    "each entry notes what the book covers and how it is regarded.", "",
    "**Format:** 📕 physical copy · 💾 digital (PDF) · 📕💾 both", "", "---", "", "## Overview", ""]
order = [k for k in TOP if k in tree] + [k for k in tree if k not in TOP]
for top in order:
    n = sum(len(v) for v in tree[top].values())
    lines.append(f"- **[{top}](#{re.sub(r'[^a-z0-9]+', '-', top.lower()).strip('-')})** ({n})")
    for sub in sorted(tree[top]):
        lines.append(f"  - [{sub}](#{re.sub(r'[^a-z0-9]+', '-', sub.lower()).strip('-')}) ({len(tree[top][sub])})")
lines += ["", "---", ""]
for top in order:
    lines += [f"## {top}", ""]
    for sub in sorted(tree[top]):
        lines += [f"### {sub}", "", "| Book | Author | Format | About |", "|------|--------|:------:|-------|"]
        seen = {}
        for o, t, fmt in sorted(tree[top][sub], key=lambda x: x[0]["title"]):
            k = norm(o["title"])
            if k in seen:
                seen[k][2].add(fmt); seen[k][3].extend(t.get("imgs") or []); continue
            seen[k] = [o, t, {fmt}, list(t.get("imgs") or [])]
        for o, t, fmts, imgs in seen.values():
            f = ("📕" if "physical" in fmts else "") + ("💾" if "digital" in fmts else "")
            c = cover(imgs, w=60)
            ed = f", {o['edition']}" if o.get("edition") and o["edition"] not in o["title"] else ""
            lines.append(f"| **{cell(o['title'])}**{cell(ed)}{'<br>' + c if c else ''} | {cell(o['author'])} | {f} | {cell(o['summary'])} |")
        lines += [""]
    lines += ["---", ""]
lines += ["*See also: [Books](Books.md)*", ""]
open(os.path.join(BK, "Technical.md"), "w").write("\n".join(lines))

print("new influential", len(new_inf), "read pages", len(read_rows), "unread rows", len(unread_rows))
print("skipped", skipped)
