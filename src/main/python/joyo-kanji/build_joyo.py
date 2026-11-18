"""Build the full 2,136 jōyō kanji dataset (JSON) for ettuge.

Sources
- davidluzgouveia/kanji-data  kanji-jouyou.json  (KANJIDIC2 + JLPT + WaniKani; MIT)
- mozillazg/pinyin-data        kMandarin.txt / pinyin.txt (Unihan; MIT)
- MEXT 2017 gakunenbetsu table (in force from 2020) for grades 4–6 (grades2020.py)
"""
import json, re, sys
from grades2020 import G4, G5, G6

KD = "/home/claude/davidluzgouveia/kanji-data/kanji-jouyou.json"
PY = "/home/claude/mozillazg/pinyin-data"

# ---------------------------------------------------------------- kana parsing
def kata2hira(s):
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)

def hira2kata(s):
    return "".join(chr(ord(c) + 0x60) if "ぁ" <= c <= "ゖ" else c for c in s)

# mora table: kana -> (consonant, vowel) in a neutral phoneme notation
# consonants: k g s sh z j t ch ts d n h f b p m y r w ''  ; y-glide handled via 'ky' etc.
BASE = {}
def add(row, cons):
    for kana, v in zip(row, "aiueo"):
        if kana != "_":
            BASE[kana] = (cons, v)
add("あいうえお", "")
add("かきくけこ", "k"); add("がぎぐげご", "g")
add("さ_すせそ", "s"); BASE["し"] = ("sh", "i")
add("ざ_ずぜぞ", "z"); BASE["じ"] = ("j", "i")
add("た__てと", "t"); BASE["ち"] = ("ch", "i"); BASE["つ"] = ("ts", "u")
add("だ__でど", "d"); BASE["ぢ"] = ("j", "i"); BASE["づ"] = ("z", "u")
add("なにぬねの", "n")
add("は__へほ", "h"); BASE["ひ"] = ("h", "i"); BASE["ふ"] = ("f", "u")
add("ばびぶべぼ", "b"); add("ぱぴぷぺぽ", "p")
add("まみむめも", "m")
BASE.update({"や": ("y", "a"), "ゆ": ("y", "u"), "よ": ("y", "o")})
add("らりるれろ", "r")
BASE.update({"わ": ("w", "a"), "ゐ": ("w", "i"), "ゑ": ("w", "e"), "を": ("w", "o")})
SMALL_Y = {"ゃ": "a", "ゅ": "u", "ょ": "o"}
SMALL_V = {"ぁ": "a", "ぃ": "i", "ぅ": "u", "ぇ": "e", "ぉ": "o"}

def parse(kana):
    """hiragana string -> list of tokens: ('m', cons, vowel, long) | ('N',) | ('Q',) | ('sep', ch)"""
    s = kata2hira(kana)
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "ん":
            out.append(("N",)); i += 1; continue
        if c == "っ":
            out.append(("Q",)); i += 1; continue
        if c == "ー" and out and out[-1][0] == "m":
            m = out[-1]; out[-1] = ("m", m[1], m[2], True); i += 1; continue
        if c in BASE:
            cons, v = BASE[c]; i += 1
            if i < len(s) and s[i] in SMALL_Y and v == "i" and cons:
                v = SMALL_Y[s[i]]
                cons = {"sh": "sh", "j": "j", "ch": "ch"}.get(cons, cons + "y"); i += 1
            elif i < len(s) and s[i] in SMALL_V:
                v = SMALL_V[s[i]]; i += 1
            out.append(("m", cons, v, False)); continue
        out.append(("sep", c)); i += 1
    # long vowels: ou, oo, uu, aa, ii, ee (not ei) inside one morpheme
    res = []
    for t in out:
        if (t[0] == "m" and t[1] == "" and res and res[-1][0] == "m" and not res[-1][3]):
            p = res[-1]
            if (p[2], t[2]) in {("o", "u"), ("o", "o"), ("u", "u"), ("a", "a"), ("i", "i"), ("e", "e")}:
                res[-1] = ("m", p[1], p[2], True); continue
        res.append(t)
    return res

# ---------------------------------------------------------------- romanisers
HEP_C = {"sh": "sh", "ch": "ch", "ts": "ts", "j": "j", "f": "f"}
MAC = {"a": "ā", "i": "ī", "u": "ū", "e": "ē", "o": "ō"}

def hepburn(kana):
    toks, out = parse(kana), []
    for n, t in enumerate(toks):
        if t[0] == "m":
            cons = t[1]
            if cons == "sh" and t[2] != "i": cons = "sh"
            out.append(cons + (MAC[t[2]] if t[3] else t[2]))
        elif t[0] == "N":
            nxt = toks[n + 1] if n + 1 < len(toks) else None
            out.append("n'" if nxt and nxt[0] == "m" and (nxt[1] in ("", "y")) else "n")
        elif t[0] == "Q":
            nxt = toks[n + 1] if n + 1 < len(toks) else None
            if nxt and nxt[0] == "m" and nxt[1]:
                out.append("t" if nxt[1] == "ch" else nxt[1][0])
        else:
            out.append(t[1])
    return "".join(out)

# Eke: c = ch (ಚ), S = sh (ಶ), j = j, v = w (ವ), capital vowel = long
EKE_C = {"sh": "S", "ch": "c", "ts": "ts", "w": "v", "shy": "S", "chy": "c"}
EKE_V = {"a": "A", "i": "I", "u": "U", "e": "E", "o": "O"}

def eke(kana):
    toks, out = parse(kana), []
    for n, t in enumerate(toks):
        if t[0] == "m":
            cons = EKE_C.get(t[1], t[1])
            out.append(cons + (EKE_V[t[2]] if t[3] else t[2]))
        elif t[0] == "N":
            nxt = toks[n + 1] if n + 1 < len(toks) else None
            out.append("m" if nxt and nxt[0] == "m" and nxt[1] in ("p", "b", "m") else "n")
        elif t[0] == "Q":
            nxt = toks[n + 1] if n + 1 < len(toks) else None
            if nxt and nxt[0] == "m" and nxt[1]:
                c = EKE_C.get(nxt[1], nxt[1])
                out.append("t" if c == "ts" else c[0])
        else:
            out.append(t[1])
    return "".join(out)

# Kannada approximation
KN_C = {"": "", "k": "ಕ", "g": "ಗ", "s": "ಸ", "sh": "ಶ", "z": "ಜ಼", "j": "ಜ", "t": "ತ",
        "ch": "ಚ", "ts": "ತ್ಸ", "d": "ದ", "n": "ನ", "h": "ಹ", "f": "ಫ಼", "b": "ಬ", "p": "ಪ",
        "m": "ಮ", "y": "ಯ", "r": "ರ", "w": "ವ"}
for c in "kgnhbpmr":
    KN_C[c + "y"] = KN_C[c] + "್ಯ"
KN_IND = {"a": "ಅ", "i": "ಇ", "u": "ಉ", "e": "ಎ", "o": "ಒ"}
KN_IND_L = {"a": "ಆ", "i": "ಈ", "u": "ಊ", "e": "ಏ", "o": "ಓ"}
KN_SIGN = {"a": "", "i": "ಿ", "u": "ು", "e": "ೆ", "o": "ೊ"}
KN_SIGN_L = {"a": "ಾ", "i": "ೀ", "u": "ೂ", "e": "ೇ", "o": "ೋ"}

def kannada(kana):
    toks, out = parse(kana), []
    for n, t in enumerate(toks):
        if t[0] == "m":
            cons, v, L = t[1], t[2], t[3]
            if not cons:
                out.append((KN_IND_L if L else KN_IND)[v])
            else:
                out.append(KN_C[cons] + (KN_SIGN_L if L else KN_SIGN)[v])
        elif t[0] == "N":
            nxt = toks[n + 1] if n + 1 < len(toks) else None
            out.append("ನ್" if nxt and nxt[0] == "m" and nxt[1] in ("", "y") else "ಂ")
        elif t[0] == "Q":
            nxt = toks[n + 1] if n + 1 < len(toks) else None
            if nxt and nxt[0] == "m" and nxt[1]:
                base = KN_C[nxt[1]]
                out.append(base[0] + "್")  # first consonant + virama => gemination
            else:
                out.append("್")
        else:
            out.append(t[1])
    return "".join(out)

# ---------------------------------------------------------------- readings
def kun_display(r):
    """KANJIDIC 'か.つ' / 'ひと-' -> 'か(つ)' / 'ひと-'"""
    if "." in r:
        a, b = r.split(".", 1)
        return f"{a}({b})"
    return r

def conv_kun(r, f):
    lead = "-" if r.startswith("-") else ""
    tail = "-" if r.endswith("-") else ""
    core = r.strip("-")
    if "." in core:
        a, b = core.split(".", 1)
        return f"{lead}{f(a)}({f(b)}){tail}"
    return f"{lead}{f(core)}{tail}"

def clean_wk(lst):
    return [x for x in (lst or []) if not x.startswith(("^", "!"))]

def strip_wk(lst):
    return [x.lstrip("^!") for x in (lst or [])]

# ---------------------------------------------------------------- pinyin
def load_pinyin():
    pm = {}
    for fn in ("pinyin.txt", "kMandarin.txt"):
        for line in open(f"{PY}/{fn}", encoding="utf8"):
            m = re.match(r"U\+([0-9A-F]+):\s*([^#]+)#", line)
            if m:
                ch = chr(int(m.group(1), 16))
                pm.setdefault(ch, m.group(2).strip().replace(",", ", "))
    return pm

def main():
    d = json.load(open(KD, encoding="utf8"))
    pm = load_pinyin()
    g2020 = {c: 4 for c in G4} | {c: 5 for c in G5} | {c: 6 for c in G6}
    rows = []
    for k, v in d.items():
        grade = v["grade"] if v["grade"] in (1, 2, 3) else g2020.get(k, 8)
        kokuji = any("kokuji" in m.lower() for m in v["meanings"])
        meanings = [m for m in v["meanings"] if "radical" not in m.lower() and "kokuji" not in m.lower()] or v["meanings"]
        on = v["readings_on"] or []
        kun = v["readings_kun"] or []
        # usual reading: WaniKani's primary (unprefixed) reading if any, else first on'yomi, else kun
        wk_on, wk_kun = clean_wk(v.get("wk_readings_on")), clean_wk(v.get("wk_readings_kun"))
        usual, utype = None, None
        if wk_on and (wk_on[0] in on or not wk_kun):
            usual, utype = wk_on[0], "on"
        elif wk_kun:
            usual, utype = wk_kun[0], "kun"
        elif on:
            usual, utype = on[0], "on"
        elif kun:
            usual, utype = kun[0].split(".")[0].strip("-"), "kun"
        # if WaniKani lists on'yomi first among all its readings, prefer on
        if utype == "kun" and v.get("wk_readings_on") is not None and not wk_kun:
            pass
        if utype == "kun":
            full = next((r for r in kun if r.split(".")[0].strip("-") == usual), None)
            if full:
                usual = full.strip("-").replace(".", "")
                u_kana = kun_display(full.strip("-"))
            else:
                u_kana = usual
        else:
            u_kana = hira2kata(usual)
        row = {
            "k": k,
            "g": grade,
            "j": v["jlpt_new"],
            "s": v["strokes"],
            "f": v["freq"],
            "m": meanings,
            "on": [hira2kata(r) for r in on],
            "onR": [hepburn(r) for r in on],
            "onE": [eke(r) for r in on],
            "onK": [kannada(r) for r in on],
            "kun": [kun_display(r) for r in kun],
            "kunR": [conv_kun(r, hepburn) for r in kun],
            "kunE": [conv_kun(r, eke) for r in kun],
            "kunK": [conv_kun(r, kannada) for r in kun],
            "u": u_kana, "ut": utype,
            "uR": hepburn(usual) if usual else None,
            "uE": eke(usual) if usual else None,
            "uK": kannada(usual) if usual else None,
            "py": ", ".join((pm.get(k) or "").split(", ")[:3]) or None,
            "kj": kokuji,
        }
        rows.append(row)
    # order: grade, then newspaper frequency (rare/unranked last), then strokes
    rows.sort(key=lambda r: (r["g"], r["f"] or 9999, r["s"]))
    for i, r in enumerate(rows, 1):
        r["n"] = i
    json.dump(rows, open(sys.argv[1], "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
    import collections
    print(len(rows), collections.Counter(r["g"] for r in rows))
    print("no pinyin:", "".join(r["k"] for r in rows if not r["py"]))
    print("usual types:", collections.Counter(r["ut"] for r in rows))

if __name__ == "__main__":
    main()
