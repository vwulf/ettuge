"""Generate src/main/md/nihongo/akSaragaLukana.md — kana beside Kannada aksharas.

Run from the repo root:  python3 src/main/python/joyo-kanji/build_kana_table.py
Kanji examples: hand-picked ones are kept; empty cells are filled from
joyo-kanji.json (most frequent jōyō kanji whose reading is exactly that kana).
"""
import json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
OUT = os.path.join(ROOT, "src/main/md/nihongo/akSaragaLukana.md")
DATA = os.path.join(ROOT, "src/main/md/nihongo/joyo-kanji.json")

VOW = "aiueo"
KN_IND = dict(zip(VOW, "ಅಇಉಎಒ")); KN_IND_L = dict(zip(VOW, "ಆಈಊಏಓ"))
KN_SIGN = {"a": "", "i": "ಿ", "u": "ು", "e": "ೆ", "o": "ೊ"}
KN_SIGN_L = {"a": "ಾ", "i": "ೀ", "u": "ೂ", "e": "ೇ", "o": "ೋ"}
LONG_KANA = {"a": "あ", "i": "い", "u": "う", "e": "い", "o": "う"}  # かあ きい くう けい こう

def h2k(s):
    return "".join(chr(ord(c) + 0x60) if "ぁ" <= c <= "ゖ" else c for c in s)

def k2h(s):
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)

X = "❌"
# (Eke consonant, Kannada base consonant, [5 cells for a i u e o])
# a cell is hiragana, "[カタカナ]" for a loanword-only (gairaigo) spelling, or None
ROWS = [
    ("k", "ಕ", ["か", "き", "く", "け", "こ"]),
    ("g", "ಗ", ["が", "ぎ", "ぐ", "げ", "ご"]),
    ("G", "ಙ", [None] * 5),
    ("c", "ಚ", ["ちゃ", "ち", "ちゅ", "ちぇ", "ちょ"]),
    ("j", "ಜ", ["じゃ", "じ・ぢ", "じゅ", "じぇ", "じょ"]),
    ("Y", "ಞ", ["にゃ", "に", "にゅ", "[ニェ]", "にょ"]),
    ("T", "ಟ", [None] * 5),
    ("D", "ಡ", [None] * 5),
    ("N", "ಣ", [None] * 5),
    ("t", "ತ", ["た", "[ティ]", "[トゥ]", "て", "と"]),
    ("ts", "ತ್ಸ", ["[ツァ]", "[ツィ]", "つ", "[ツェ]", "[ツォ]"]),
    ("d", "ದ", ["だ", "[ディ]", "[ドゥ]", "で", "ど"]),
    ("n", "ನ", ["な", "に", "ぬ", "ね", "の"]),
    ("p", "ಪ", ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"]),
    ("f", "ಫ಼", ["[ファ]", "[フィ]", "ふ", "[フェ]", "[フォ]"]),
    ("b", "ಬ", ["ば", "び", "ぶ", "べ", "ぼ"]),
    ("m", "ಮ", ["ま", "み", "む", "め", "も"]),
    ("y", "ಯ", ["や", None, "ゆ", "[イェ]", "よ"]),
    ("r", "ರ", ["ら", "り", "る", "れ", "ろ"]),
    ("l", "ಲ", [None] * 5),
    ("v", "ವ", [("わ", "ワ・ヴァ"), ("ゐ", "ヰ・ウィ・ヴィ"), (None, "ヴ"), ("ゑ", "ヱ・ウェ・ヴェ"), ("を", "ヲ・ウォ・ヴォ")]),
    ("S", "ಶ", ["しゃ", "し", "しゅ", "しぇ", "しょ"]),
    ("s", "ಸ", ["さ", "[スィ]", "す", "せ", "そ"]),
    ("z", "ಜ಼", ["ざ", "[ズィ]", "ず・づ", "ぜ", "ぞ"]),
    ("h", "ಹ", ["は", "ひ", "[ホゥ]", "へ", "ほ"]),
    ("L", "ಳ", [None] * 5),
]

# kanji the table already had (by hiragana cell); kept as-is
HAND = {
    "あ": "亜, 阿", "ああ": "嗚呼", "い": "胃, 違, 伊", "う": "雨", "え": "絵", "おお": "大",
    "か": "火", "かあ": "母", "き": "木", "きい": "紀伊", "く": "九, 区", "くう": "空, 食う",
    "け": "毛", "こ": "子", "が": "画, 蛾", "ぎ": "義", "げ": "外", "ご": "五",
    "ちゃ": "茶", "ち": "血", "ちゅう": "中, 注, 宙", "じ": "自", "じゅう": "十", "じょ": "女",
}

def load_index():
    rows = json.load(open(DATA, encoding="utf8"))
    idx = {}
    for r in rows:
        reads = {k2h(x) for x in r["on"]}
        for kun in r["kun"]:
            if "(" not in kun and "-" not in kun:
                reads.add(kun)
        for s in reads:
            idx.setdefault(s, []).append((r["f"] or 9999, r["g"], r["k"]))
    return {s: [k for *_, k in sorted(v)] for s, v in idx.items()}

IDX = load_index()
JOYO = {r["k"] for r in json.load(open(DATA, encoding="utf8"))}

def link(text):
    """wrap every jōyō kanji in a link to its entry on the jōyō kanji page"""
    return "".join(f"[{c}](joyo-kanji#{c})" if c in JOYO else c for c in text)

SHOW = 5          # kanji shown in a table cell; the rest are in the full list below
FULL = []         # (anchor, kana, eke, [kanji]) in table order, for the full list

def kanji_for(hira, eke=None):
    """All jōyō kanji whose reading is exactly `hira` (a string, or a list of spellings).
    The cell shows the SHOW most frequent; a '+N' link jumps to the full list."""
    if hira is None:
        return X
    spellings = hira if isinstance(hira, list) else [hira]
    found = []
    for sp in spellings:
        for k in IDX.get(sp, []):
            if k not in found:
                found.append(k)
    extra = [h for h in HAND.get(spellings[0], "").split(", ") if h and h not in found]
    if not found and not extra:
        return " "
    cell = " ".join(link(k) for k in found[:SHOW])
    if len(found) > SHOW:
        anchor = "r-" + eke
        FULL.append((anchor, "・".join(spellings), eke, found))
        cell += f" [+{len(found) - SHOW}](#{anchor})"
    if extra:
        cell += (" · " if found else "") + ", ".join(link(e) for e in extra)
    return cell

ARCHAIC = set("ゐゑを")

def cells(raw, v):
    """raw cell -> ((hira, kata, lookup), (hira, kata, lookup)) for the short and long vowel.
    raw is hiragana (alternates joined by ・), "[カタカナ]" for loanword-only kana,
    a (hiragana or None, katakana) pair, or None."""
    if raw is None:
        return (X, X, None), (X, X, None)
    if isinstance(raw, str) and raw.startswith("["):
        raw = (None, raw.strip("[]"))
    if isinstance(raw, str):
        raw = (raw, "・".join(h2k(x) for x in raw.split("・")))
    hira, kata = raw
    kl = "・".join(x + "ー" for x in kata.split("・") if x not in ("ヰ", "ヱ", "ヲ"))
    if not hira:
        return (X, kata, None), (X, kl, None)
    alts = hira.split("・")
    if ARCHAIC & set(hira):
        return (hira, kata, alts), (X, kl, None)
    long_alts = [x + LONG_KANA[v] for x in alts]
    return (hira, kata, alts), ("・".join(long_alts), kl, long_alts)

def kn_syl(base, v, long):
    return base + (KN_SIGN_L if long else KN_SIGN)[v]

def block(eke, base, raw5, label=None):
    ek, hi, ka, kj, kn = [], [], [], [], []
    for v, raw in zip(VOW, raw5):
        for long in (False, True):
            h, k, look = cells(raw, v)[long]
            ek.append(eke + (v.upper() if long else v))
            hi.append(h); ka.append(k); kj.append(kanji_for(look, eke + (v.upper() if long else v)))
            kn.append(kn_syl(base, v, long))
    ottu = "್" + base if len(base) == 1 else X
    head = [
        ["Eke", eke, eke] + ek,
        ["hiragAna", X, X] + hi,
        ["katakAna", X, X] + ka,
        ["kAnji", X, X] + kj,
        ["kannaDa", ottu, base + "್"] + kn,
    ]
    return head

def md_row(cells):
    return "| " + " | ".join(c if c else " " for c in cells) + " |"

def main():
    hdr = ["**Script**", "**ottu**", "**್**"] + [f"**{c}**" for c in "ಅಆಇಈಉಊಎಏಒಓ"]
    out = ["---", "title: Kana and Kannada aksharas", "parent: 日本語", "nav_order: 1", "---", "",
           "# Kana and ಕನ್ನಡ aksharas", "",
           "Every Japanese kana set beside the Kannada akshara that sounds closest, with its Eke spelling and a kanji read that way. "
           "One block per Kannada consonant, in varNamAle order; Japanese consonants that Kannada lacks (ts, f, z) sit next to their nearest relatives.", "",
           md_row(hdr), "|" + "|".join(["---"] * len(hdr)) + "|"]
    vowel_block = [
        ["Eke", X, X] + ["a", "A", "i", "I", "u", "U", "e", "E", "o", "O"],
        ["hiragAna", X, X] + ["あ", "ああ", "い", "いい", "う", "うう", "え", "ええ・えい", "お", "おお・おう"],
        ["katakAna", X, X] + ["ア", "アー", "イ", "イー", "ウ", "ウー", "エ", "エー", "オ", "オー"],
        ["kAnji", X, X] + [kanji_for(sp, e) for sp, e in zip(["あ", "ああ", "い", "いい", "う", "うう", "え", ["ええ", "えい"], "お", ["おお", "おう"]], ["a", "A", "i", "I", "u", "U", "e", "E", "o", "O"])],
        ["kannaDa", X, X] + list("ಅಆಇಈಉಊಎಏಒಓ"),
    ]
    blank = md_row([""] * len(hdr))
    for r in vowel_block:
        out.append(md_row(r))
    for eke, base, raw5 in ROWS:
        out.append(blank)
        for r in block(eke, base, raw5):
            out.append(md_row(r))
    out += ["", "**Reading the table**", "",
            "- ❌ — Japanese has no such sound. ಋ, the visarga ಃ and the aspirated mahaprANa letters (ಖ ಘ ಛ ಝ ಠ ಢ ಥ ಧ ಫ ಭ) have no kana at all, since Japanese has no aspirated consonants. ಙ appears only as ん before *k*/*g* (see ん below). Kannada's retroflexes ಟ ಡ ಣ ಳ have no kana; Japanese has a single *r* (ら行) that covers both ರ and ಲ.",
            "- Katakana in a cell with ❌ under hiragana (ティ, ファ, ウォ…) is a loanword-only spelling, used for foreign words.",
            "- Long vowels: katakana adds ー (カー). Hiragana doubles the vowel for *a i u* (かあ きい くう) but usually writes long *e* as えい (けい) and long *o* as おう (こう); ええ and おお also occur (ねえ, 大 おお).",
            "- ぢ and づ are spelling variants of じ and ず, used where the sound comes from ち/つ (鼻血 はなぢ, 続く つづく).",
            "- ವ row: ヴ (ヴァ ヴィ ヴェ ヴォ) spells a true *v* in loanwords; ゐ ゑ (ヰ ヱ) are archaic *wi*/*we*; を is the object particle, now said *o*.",
            "- ಞ: Japanese に is palatal, so に and にゃ にゅ にょ are ಞಿ and ಞ ಞು ಞೊ.",
            "- ふ is between ಹು and ಫ಼ು (a soft *f* made with both lips), so it sits in the *f* block; ホゥ is the loanword spelling for a true *hu*.",
            "- ತ್ಸ (つ), ಫ಼ (ふ) and ಜ಼ (ざ行) have no native Kannada akshara; Eke reserves *f* and *z* for such borrowed sounds.",
            "- kAnji: every jōyō kanji read with exactly that kana — the most common first; **+N** jumps to the full list at the bottom of the page. Empty where no jōyō kanji has that reading. Kanji after a · are earlier hand picks that are not exact jōyō readings (お母さん's 母 for かあ, 紀伊 for きい). Click a kanji to open its entry on the [jōyō kanji page](joyo-kanji).",
            ""]
    # yoon
    out += ["## ಯ ottu — contracted sounds (yōon)", "",
            "Small ゃ ゅ ょ after an *i*-row kana gives the ಯ ottu: き + ゃ = きゃ = ಕ್ಯ.", "",
            md_row(["**Eke**", "**hiragAna**", "**katakAna**", "**kAnji**", "**kannaDa**"]), "|---|---|---|---|---|"]
    for eke, base, row in [("ky", "ಕ", "き"), ("gy", "ಗ", "ぎ"), ("hy", "ಹ", "ひ"),
                           ("by", "ಬ", "び"), ("py", "ಪ", "ぴ"), ("my", "ಮ", "み"), ("ry", "ರ", "り")]:
        for v, sm in zip("auo", "ゃゅょ"):
            for long in (False, True):
                hira = row + sm + (LONG_KANA[v] if long else "")
                kata = h2k(row + sm) + ("ー" if long else "")
                out.append(md_row([eke + (v.upper() if long else v), hira, kata, kanji_for(hira, eke + (v.upper() if long else v)),
                                   base + "್ಯ" + (KN_SIGN_L if long else KN_SIGN)[v]]))
    out += ["", "ちゃ じゃ しゃ (c, j, S) and にゃ (ಞ) are in the main table: Kannada ಚ ಜ ಶ ಞ already carry the *y* glide. "
            "Japanese に is itself palatal, so にゃ にゅ にょ are ಞ ಞು ಞೊ rather than ನ್ಯ.", ""]
    # n
    out += ["## ん — the moraic nasal (ಂ)", "",
            "ん takes the place of a nasal before the next sound, just like the anusvAra ಂ, and Eke writes it the same way.", "",
            md_row(["**Before**", "**Sounds like**", "**Eke**", "**Example**", "**kannaDa**"]), "|---|---|---|---|---|"]
    for before, sound, eke, ex, kn in [
        ("p b m", "m", "m", "散歩 さんぽ · sampo", "ಸಂಪೊ"),
        ("k g", "ŋ (ಙ)", "n", "銀行 ぎんこう · ginkO", "ಗಿಂಕೋ"),
        ("t d n ts c j r", "n", "n", "本当 ほんとう · hontO", "ಹೊಂತೋ"),
        ("a vowel, y, w", "nasal vowel", "n", "金曜 きんよう · kinyO", "ಕಿನ್ಯೋ"),
        ("end of word", "ɴ", "n", "本 ほん · hon", "ಹೊಂ"),
    ]:
        out.append(md_row([before, sound, eke, link(ex), kn]))
    out.append("")
    # gemination
    out += ["## っ — doubled consonants (ottu of the same letter)", "",
            "A small っ (ッ) doubles the consonant after it — the Kannada ottu of the same letter: ಕ್ಕ, ತ್ತ, ಪ್ಪ.", "",
            md_row(["**Eke**", "**hiragAna**", "**katakAna**", "**kannaDa**", "**Example**"]), "|---|---|---|---|---|"]
    for eke, hira, kn, ex in [
        ("kk", "っか っき っく っけ っこ", "ಕ್ಕ ಕ್ಕಿ ಕ್ಕು ಕ್ಕೆ ಕ್ಕೊ", "学校 がっこう · gakkO · ಗಕ್ಕೋ"),
        ("ss", "っさ っす っせ っそ", "ಸ್ಸ ಸ್ಸು ಸ್ಸೆ ಸ್ಸೊ", "達成 たっせい · tassei · ತಸ್ಸೆಇ"),
        ("SS", "っしゃ っし っしゅ っしょ", "ಶ್ಶ ಶ್ಶಿ ಶ್ಶು ಶ್ಶೊ", "雑誌 ざっし · zaSSi · ಜ಼ಶ್ಶಿ"),
        ("tt", "った って っと", "ತ್ತ ತ್ತೆ ತ್ತೊ", "切手 きって · kitte · ಕಿತ್ತೆ"),
        ("cc", "っちゃ っち っちゅ っちょ", "ಚ್ಚ ಚ್ಚಿ ಚ್ಚು ಚ್ಚೊ", "一致 いっち · icci · ಇಚ್ಚಿ"),
        ("tts", "っつ", "ತ್ತ್ಸು", "三つ みっつ · mittsu · ಮಿತ್ತ್ಸು"),
        ("pp", "っぱ っぴ っぷ っぺ っぽ", "ಪ್ಪ ಪ್ಪಿ ಪ್ಪು ಪ್ಪೆ ಪ್ಪೊ", "一杯 いっぱい · ippai · ಇಪ್ಪಇ"),
    ]:
        out.append(md_row([eke, hira, h2k(hira), kn, link(ex)]))
    out += ["", "っ doubles only *k s S t c ts p*. Kannada also doubles ಗ ಜ ದ ಬ ನ ಮ ಲ (ಅಗ್ಗ, ಅಮ್ಮ…), which Japanese writes only in loanwords (ベッド *beddo*, バッグ *baggu*) or with ん + kana (*mm* = んま: あんま).", ""]
    # ai / au
    out += ["## ಐ and ಔ — two kana in Japanese", "",
            "Japanese has no single kana for ಐ or ಔ: it writes the two vowels separately (あい, あお/あう), each a beat of its own.", "",
            md_row(["**Eke**", "**hiragAna**", "**katakAna**", "**kAnji**", "**kannaDa**"]), "|---|---|---|---|---|"]
    A_ROW = [("", "", "あ"), ("k", "ಕ", "か"), ("g", "ಗ", "が"), ("s", "ಸ", "さ"), ("z", "ಜ಼", "ざ"), ("t", "ತ", "た"),
             ("d", "ದ", "だ"), ("n", "ನ", "な"), ("h", "ಹ", "は"), ("b", "ಬ", "ば"), ("p", "ಪ", "ぱ"), ("m", "ಮ", "ま"),
             ("y", "ಯ", "や"), ("r", "ರ", "ら"), ("v", "ವ", "わ")]
    for eke, base, a in A_ROW:
        kj = kanji_for([a + "い"], eke + "ai")
        if eke and not kj.strip():
            continue
        out.append(md_row([eke + "ai", a + "い", h2k(a) + "イ", kj, base + "ೈ" if base else "ಐ"]))
    for eke, base, a in A_ROW:
        kj = kanji_for([a + "お", a + "う"], eke + "au")
        if eke and not kj.strip():
            continue
        out.append(md_row([eke + "au", a + "お・" + a + "う", h2k(a) + "オ・" + h2k(a) + "ウ", kj, base + "ೌ" if base else "ಔ"]))
    out += ["", "Japanese *au* inside a word became *ō* long ago (かう → こう), so ಔ survives mostly across word parts: 青 あお, 顔 かお, 会う あう.", ""]
    # rare loanword kana
    out += ["## Rarer kana", "",
            md_row(["**Kana**", "**Eke**", "**kannaDa**", "**Used in**"]), "|---|---|---|---|"]
    for kana, eke, kn, use in [
        ("クァ クィ クェ クォ", "kva kvi kve kvo", "ಕ್ವ ಕ್ವಿ ಕ್ವೆ ಕ್ವೊ", "foreign names (クォーク *quark*)"),
        ("グァ", "gva", "ಗ್ವ", "グァム *Guam*"),
        ("テュ・デュ", "tyu dyu", "ತ್ಯು ದ್ಯು", "デュエット *duet*"),
        ("フュ・ヴュ", "fyu vyu", "ಫ಼್ಯು ವ್ಯು", "フュージョン *fusion*"),
        ("ヵ ヶ", "ka ka/ga", "ಕ", "counters: 一ヶ月 *ikkagetsu* (one month), 霞ヶ関 *kasumigaseki*"),
        ("ゝ ゞ ヽ ヾ", "—", "—", "repeat the kana before (ゞ adds voicing): いすゞ *isuzu*, こゝろ *kokoro*"),
        ("々", "—", "—", "repeat the kanji before: 人々 *hitobito*, 時々 *tokidoki*"),
    ]:
        out.append(md_row([kana, f"`{eke}`" if eke != "—" else eke, kn, use]))
    out.append("")
    out += ["## Every jōyō kanji by exact reading", "",
            f"Where a sound has more than {SHOW} kanji, the table shows the {SHOW} most common and links here for the rest. "
            "Each list is every jōyō kanji with exactly that reading (an on'yomi, or a kun'yomi that is a whole word), most common first. "
            "Readings come from KANJIDIC, which also lists rare readings beyond the official jōyō table, so a few kanji appear under unusual sounds (区 under こう).", ""]
    for anchor, kana, eke, ks in FULL:
        out.append(f'<a id="{anchor}"></a>**{kana}** `{eke}` ({len(ks)}): ' + " ".join(link(k) for k in ks))
        out.append("")
    open(OUT, "w", encoding="utf8").write("\n".join(out))
    print("wrote", OUT)

if __name__ == "__main__":
    main()
