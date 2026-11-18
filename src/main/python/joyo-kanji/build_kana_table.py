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
    ("c", "ಚ", ["ちゃ", "ち", "ちゅ", "ちぇ", "ちょ"]),
    ("j", "ಜ", ["じゃ", "じ", "じゅ", "じぇ", "じょ"]),
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
    ("v", "ವ", ["わ", "[ウィ]", None, "[ウェ]", "[ウォ]"]),
    ("S", "ಶ", ["しゃ", "し", "しゅ", "しぇ", "しょ"]),
    ("s", "ಸ", ["さ", "[スィ]", "す", "せ", "そ"]),
    ("z", "ಜ಼", ["ざ", "[ズィ]", "ず", "ぜ", "ぞ"]),
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
            idx.setdefault(s, []).append((r["f"] or 9999, r["k"]))
    return {s: [k for _, k in sorted(v)] for s, v in idx.items()}

IDX = load_index()

def kanji_for(hira):
    if hira is None:
        return X
    if hira in HAND:
        return HAND[hira]
    return ", ".join(IDX.get(hira, [])[:2])

def cells(raw, v):
    """raw cell -> (hiragana, katakana, hiragana-for-lookup) for short and long"""
    if raw is None:
        return (X, X, None), (X, X, None)
    if raw.startswith("["):
        kata = raw.strip("[]")
        return (X, kata, None), (X, kata + "ー", None)
    short_h = raw
    long_h = raw + LONG_KANA[v]
    return (short_h, h2k(short_h), short_h), (long_h, h2k(raw) + "ー", long_h)

def kn_syl(base, v, long):
    return base + (KN_SIGN_L if long else KN_SIGN)[v]

def block(eke, base, raw5, label=None):
    ek, hi, ka, kj, kn = [], [], [], [], []
    for v, raw in zip(VOW, raw5):
        for long in (False, True):
            h, k, look = cells(raw, v)[long]
            ek.append(eke + (v.upper() if long else v))
            hi.append(h); ka.append(k); kj.append(kanji_for(look))
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
        ["kAnji", X, X] + [kanji_for(s) for s in ["あ", "ああ", "い", "いい", "う", "うう", "え", "えい", "お", "おお"]],
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
            "- ❌ — Japanese has no such sound. Kannada's retroflexes ಟ ಡ ಣ ಳ have no kana; Japanese has a single *r* (ら行) that covers both ರ and ಲ.",
            "- Katakana in a cell with ❌ under hiragana (ティ, ファ, ウォ…) is a loanword-only spelling, used for foreign words.",
            "- Long vowels: katakana adds ー (カー). Hiragana doubles the vowel for *a i u* (かあ きい くう) but usually writes long *e* as えい (けい) and long *o* as おう (こう); ええ and おお also occur (ねえ, 大 おお).",
            "- ふ is between ಹು and ಫ಼ು (a soft *f* made with both lips), so it sits in the *f* block; ホゥ is the loanword spelling for a true *hu*.",
            "- ತ್ಸ (つ), ಫ಼ (ふ) and ಜ಼ (ざ行) have no native Kannada akshara; Eke reserves *f* and *z* for such borrowed sounds.",
            "- kAnji: a common kanji read with exactly that kana; empty where no jōyō kanji has that reading. See the [jōyō kanji page](joyo-kanji) for every kanji.",
            ""]
    # yoon
    out += ["## ಯ ottu — contracted sounds (yōon)", "",
            "Small ゃ ゅ ょ after an *i*-row kana gives the ಯ ottu: き + ゃ = きゃ = ಕ್ಯ.", "",
            md_row(["**Eke**", "**hiragAna**", "**katakAna**", "**kAnji**", "**kannaDa**"]), "|---|---|---|---|---|"]
    for eke, base, row in [("ky", "ಕ", "き"), ("gy", "ಗ", "ぎ"), ("ny", "ನ", "に"), ("hy", "ಹ", "ひ"),
                           ("by", "ಬ", "び"), ("py", "ಪ", "ぴ"), ("my", "ಮ", "み"), ("ry", "ರ", "り")]:
        for v, sm in zip("auo", "ゃゅょ"):
            for long in (False, True):
                hira = row + sm + (LONG_KANA[v] if long else "")
                kata = h2k(row + sm) + ("ー" if long else "")
                out.append(md_row([eke + (v.upper() if long else v), hira, kata, kanji_for(hira),
                                   base + "್ಯ" + (KN_SIGN_L if long else KN_SIGN)[v]]))
    out += ["", "ちゃ じゃ しゃ (c, j, S) are in the main table — Kannada ಚ ಜ ಶ already carry the *y* glide.", ""]
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
        out.append(md_row([before, sound, eke, ex, kn]))
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
        out.append(md_row([eke, hira, h2k(hira), kn, ex]))
    out += ["", "っ doubles only *k s S t c ts p*. Kannada also doubles ಗ ಜ ದ ಬ ನ ಮ ಲ (ಅಗ್ಗ, ಅಮ್ಮ…), which Japanese writes only in loanwords (ベッド *beddo*, バッグ *baggu*) or with ん + kana (*mm* = んま: あんま).", ""]
    open(OUT, "w", encoding="utf8").write("\n".join(out))
    print("wrote", OUT)

if __name__ == "__main__":
    main()
