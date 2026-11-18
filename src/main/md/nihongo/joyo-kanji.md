---
title: Jōyō kanji (2,136)
parent: 日本語
nav_order: 2
---

# 常用漢字 — the 2,136 jōyō kanji
{: .no_toc }

Every kanji on the official list for everyday use, with its readings in kana, romaji, Eke and Kannada. Search by the character itself, by an English meaning, or by any reading (kana, romaji, Eke or ಕನ್ನಡ). Tiles are coloured by the school year in which the kanji is taught; switch to JLPT level if that is more useful. Click a tile for the full entry. In the entry, the big kanji, each English meaning and each kun'yomi word (学ぶ, 生きる…) link to Japanese Wiktionary, so you can browse other senses and related words; the line marked ಕನ್ನಡ ವಿಕ್ಷನರಿ links each English meaning to Kannada Wiktionary.

**Usual reading** is the one you are most likely to meet. When a kanji sits inside a compound word it is nearly always read with its *on'yomi* — the reading borrowed from Chinese — so for most kanji the usual reading is an on'yomi (shown in カタカナ). Kanji whose usual reading is native Japanese (*kun'yomi*) show it in ひらがな.

<div id="jk" class="jk">
  <div class="jk-bar">
    <input id="jk-q" type="search" placeholder="Search: 学 · study · まなぶ · gaku · ಗಕು" autocomplete="off" aria-label="Search kanji">
    <select id="jk-sort" aria-label="Sort">
      <option value="grade">Sort: grade, then common first</option>
      <option value="freq">Sort: most common first</option>
      <option value="strokes">Sort: strokes</option>
      <option value="kana">Sort: usual reading (あいうえお)</option>
    </select>
    <select id="jk-color" aria-label="Colour by">
      <option value="g">Colour: school grade</option>
      <option value="j">Colour: JLPT level</option>
    </select>
    <button id="jk-view" type="button">Table view</button>
  </div>
  <div class="jk-chips" id="jk-chips"></div>
  <div class="jk-status" id="jk-status">Loading…</div>
  <div id="jk-out"></div>
</div>

<div id="jk-detail" class="jk-detail" hidden>
  <div class="jk-card" role="dialog" aria-modal="true" aria-labelledby="jk-d-k">
    <button class="jk-close" type="button" aria-label="Close">×</button>
    <div id="jk-d-body"></div>
  </div>
</div>

## How the columns are written
{: .no_toc }

- **Kun'yomi** — the kana written after the kanji (*okurigana*) is shown in brackets: か(つ) means the word is written 勝つ. A leading or trailing hyphen marks a prefix or suffix form.
- **Romaji** — Hepburn, with long vowels as ō, ū.
- **Eke** — `c` = ch (ಚ), `S` = sh (ಶ), `j` = j (ಜ), `ts` = ts (ತ್ಸ), `v` = w (ವ); a capital vowel is long (`kO` = こう); a small っ doubles the next consonant. This follows the [kana ↔ akshara table](akSaragaLukana).
- **ಕನ್ನಡ** — an approximate spelling: ん is ಂ (ನ್ before a vowel or y), z is ಜ಼, f is ಫ಼.
- **Usual reading** — WaniKani's primary reading where it has one, otherwise the first on'yomi, otherwise the first kun'yomi.
- **Grade** — the MEXT table in force since April 2020: 1,026 kanji in primary school (grades 1–6) and 1,110 in secondary school.
- **JLPT** — the unofficial N5–N1 lists. **Frequency** is the rank among the ~2,500 most common kanji in newspapers.

The raw data behind this page is [joyo-kanji.json](joyo-kanji.json).

**Sources:** [KANJIDIC2](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project) (EDRDG, CC BY-SA 4.0) via [davidluzgouveia/kanji-data](https://github.com/davidluzgouveia/kanji-data), which adds JLPT levels and WaniKani readings; Mandarin readings from Unicode Unihan via [mozillazg/pinyin-data](https://github.com/mozillazg/pinyin-data). KANJIDIC lists some readings that are not on the official jōyō list.

<style>
.jk { --g1:#d9ead3; --g2:#cfe2f3; --g3:#d9d2e9; --g4:#fce5cd; --g5:#f4cccc; --g6:#fff2cc; --g8:#ececec;
      --j5:#d9ead3; --j4:#cfe2f3; --j3:#fff2cc; --j2:#fce5cd; --j1:#f4cccc; --j0:#ececec; }
.jk-bar { display:flex; flex-wrap:wrap; gap:.5rem; margin:1rem 0 .5rem; }
.jk-bar input { flex:1 1 16rem; padding:.5rem .7rem; font-size:1rem; border:1px solid #bbb; border-radius:6px; }
.jk-bar select, .jk-bar button { padding:.45rem .6rem; border:1px solid #bbb; border-radius:6px; background:#fff; font-size:.85rem; cursor:pointer; }
.jk-chips { display:flex; flex-wrap:wrap; gap:.35rem; margin:.25rem 0 .5rem; }
.jk-chip { border:1px solid #999; border-radius:999px; padding:.15rem .65rem; font-size:.8rem; cursor:pointer; user-select:none; }
.jk-chip.off { opacity:.35; text-decoration:line-through; }
.jk-chip b { font-weight:600; margin-left:.25rem; color:#555; }
.jk-status { font-size:.8rem; color:#666; margin:.25rem 0 .75rem; }
.jk-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(4.6rem,1fr)); gap:.35rem; }
.jk-tile { border:1px solid rgba(0,0,0,.12); border-radius:6px; padding:.25rem .15rem .3rem; text-align:center; cursor:pointer; line-height:1.15; }
.jk-tile:hover, .jk-tile:focus { outline:2px solid #555; outline-offset:-1px; }
.jk-tile .k { font-size:2rem; font-family:"Hiragino Mincho ProN","Yu Mincho","Noto Serif JP",serif; }
.jk-tile .r { font-size:.72rem; color:#333; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.jk-tile .m { font-size:.64rem; color:#666; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.jk-table { width:100%; border-collapse:collapse; font-size:.8rem; }
.jk-table th { position:sticky; top:0; background:#f5f5f5; text-align:left; }
.jk-table td, .jk-table th { padding:.25rem .4rem; border-bottom:1px solid #e5e5e5; vertical-align:top; }
.jk-table td.k { font-size:1.4rem; cursor:pointer; }
.jk-wrap { overflow-x:auto; max-height:75vh; }
.jk-more { margin:1rem auto; display:block; padding:.4rem 1rem; border:1px solid #bbb; border-radius:6px; background:#fff; cursor:pointer; }
.jk-detail { position:fixed; inset:0; background:rgba(0,0,0,.35); display:flex; align-items:flex-start; justify-content:center; z-index:1000; overflow-y:auto; padding:5vh 1rem; }
.jk-detail[hidden] { display:none; }
.jk-card { background:#fff; border-radius:10px; max-width:40rem; width:100%; padding:1.25rem 1.5rem; position:relative; box-shadow:0 10px 30px rgba(0,0,0,.25); }
.jk-close { position:absolute; top:.4rem; right:.6rem; border:0; background:none; font-size:1.6rem; cursor:pointer; color:#666; }
.jk-head { display:flex; gap:1.25rem; align-items:center; }
.jk-big { font-size:5rem; line-height:1; padding:.5rem .9rem; border-radius:8px; font-family:"Hiragino Mincho ProN","Yu Mincho","Noto Serif JP",serif; }
a.jk-big { color:inherit; text-decoration:none; }
a.jk-big:hover { outline:2px solid #555; }
.jk-meta { font-size:.8rem; color:#555; }
.jk-meta .kn-mean { margin:-.1rem 0 .35rem; font-size:.8rem; }
.jk-meta .mean a, .jk-meta .kn-mean a, .jk-card td a { color:inherit; text-decoration:underline dotted; text-underline-offset:3px; }
.jk-meta .mean { font-size:1.05rem; color:#111; margin-bottom:.3rem; }
.jk-card table { width:100%; border-collapse:collapse; font-size:.85rem; margin-top:.75rem; }
.jk-card th { text-align:left; font-weight:600; color:#555; width:7rem; }
.jk-card td, .jk-card th { padding:.25rem .4rem; border-bottom:1px solid #eee; vertical-align:top; }
.jk-card h4 { margin:1rem 0 0; font-size:.85rem; text-transform:uppercase; letter-spacing:.04em; color:#777; }
.jk-tag { display:inline-block; border-radius:4px; padding:0 .35rem; font-size:.75rem; margin-right:.3rem; border:1px solid rgba(0,0,0,.15); }
.jk-links a { margin-right:.75rem; font-size:.8rem; }
</style>

<script>
(function () {
  const GRADES = [[1,"Grade 1"],[2,"Grade 2"],[3,"Grade 3"],[4,"Grade 4"],[5,"Grade 5"],[6,"Grade 6"],[8,"Secondary"]];
  const JLPT = [[5,"N5"],[4,"N4"],[3,"N3"],[2,"N2"],[1,"N1"],[0,"No JLPT"]];
  const PAGE = 300;
  const $ = id => document.getElementById(id);
  let data = [], shown = [], limit = PAGE, table = false;
  const onG = new Set(GRADES.map(g => g[0])), onJ = new Set(JLPT.map(j => j[0]));

  const k2h = s => s.replace(/[ァ-ヶ]/g, c => String.fromCharCode(c.charCodeAt(0) - 0x60));
  const demac = s => s.replace(/ā/g,"a").replace(/ī/g,"i").replace(/ū/g,"u").replace(/ē/g,"e").replace(/ō/g,"o");
  const longv = s => s.replace(/ō/g,"ou").replace(/ū/g,"uu").replace(/ā/g,"aa").replace(/ī/g,"ii").replace(/ē/g,"ee");
  const clean = s => s.replace(/[()\-.'’]/g, "");
  const gName = g => GRADES.find(x => x[0] === g)[1];
  const colour = r => $("jk-color").value === "g" ? `var(--g${r.g})` : `var(--j${r.j || 0})`;

  function index(r) {
    const roma = [r.uR, ...r.onR, ...r.kunR].filter(Boolean).map(clean);
    r._q = [
      r.k, r.m.join(" | ").toLowerCase(),
      ...[r.u, ...r.on, ...r.kun].filter(Boolean).map(s => k2h(clean(s))),
      ...roma, ...roma.map(demac), ...roma.map(longv),
      ...[r.uE, ...r.onE, ...r.kunE].filter(Boolean).map(clean),
      ...[r.uK, ...r.onK, ...r.kunK].filter(Boolean).map(clean),
      (r.py || "").toLowerCase()
    ].join(" \u0001 ");
    r._kana = k2h(clean(r.u || ""));
  }

  function matches(r, q) {
    if (!q) return true;
    if (q.length === 1 && /[㐀-鿿]/.test(q)) return r.k === q;
    const terms = q.split(/\s+/).filter(Boolean);
    return terms.every(t => {
      if (/[㐀-鿿]/.test(t)) return t.includes(r.k);
      const tq = /[a-z]/i.test(t) ? t.toLowerCase() : k2h(t);
      return r._q.includes(tq) || r._q.includes(demac(tq));
    });
  }

  function chips() {
    const c = $("jk-chips"); c.innerHTML = "";
    const mode = $("jk-color").value;
    const list = mode === "g" ? GRADES : JLPT, set = mode === "g" ? onG : onJ, key = mode === "g" ? "g" : "j";
    list.forEach(([v, label]) => {
      const n = data.filter(r => (r[key] || 0) === v).length;
      const el = document.createElement("span");
      el.className = "jk-chip" + (set.has(v) ? "" : " off");
      el.style.background = mode === "g" ? `var(--g${v})` : `var(--j${v})`;
      el.innerHTML = `${label}<b>${n}</b>`;
      el.title = "Click to hide or show; double-click to show only this";
      el.onclick = () => { set.has(v) ? set.delete(v) : set.add(v); limit = PAGE; chips(); render(); };
      el.ondblclick = () => { set.clear(); set.add(v); limit = PAGE; chips(); render(); };
      c.appendChild(el);
    });
  }

  function sorted(rows) {
    const s = $("jk-sort").value, f = r => r.f || 9999;
    const by = {
      grade: (a, b) => a.n - b.n,
      freq: (a, b) => f(a) - f(b) || a.s - b.s,
      strokes: (a, b) => a.s - b.s || f(a) - f(b),
      kana: (a, b) => a._kana.localeCompare(b._kana, "ja") || f(a) - f(b)
    }[s];
    return rows.slice().sort(by);
  }

  function render() {
    const q = $("jk-q").value.trim();
    shown = sorted(data.filter(r => onG.has(r.g) && onJ.has(r.j || 0) && matches(r, q)));
    $("jk-status").textContent = `${shown.length} of ${data.length} kanji`;
    const out = $("jk-out"), rows = shown.slice(0, limit);
    if (table) {
      out.innerHTML = `<div class="jk-wrap"><table class="jk-table"><thead><tr>
        <th>Kanji</th><th>Meaning</th><th>Usual</th><th>On'yomi</th><th>Kun'yomi</th><th>Eke (usual)</th><th>ಕನ್ನಡ (usual)</th><th>Grade</th><th>JLPT</th><th>Pinyin</th></tr></thead><tbody>${
        rows.map(r => `<tr style="background:${colour(r)}"><td class="k" data-k="${r.k}">${r.k}</td><td>${r.m.slice(0,3).join("; ")}</td>
        <td>${r.u || ""}<br><small>${r.uR || ""}</small></td><td>${r.on.join("、")}</td><td>${r.kun.slice(0,4).join("、")}</td>
        <td>${r.uE || ""}</td><td>${r.uK || ""}</td><td>${gName(r.g)}</td><td>${r.j ? "N" + r.j : ""}</td><td>${r.py || ""}</td></tr>`).join("")
      }</tbody></table></div>`;
    } else {
      out.innerHTML = `<div class="jk-grid">${rows.map(r =>
        `<div class="jk-tile" tabindex="0" data-k="${r.k}" style="background:${colour(r)}" title="${r.m.slice(0,3).join("; ")}">
          <div class="k">${r.k}</div><div class="r">${r.u || ""}</div><div class="m">${r.m[0] || ""}</div></div>`).join("")}</div>`;
    }
    if (shown.length > limit) {
      const b = document.createElement("button");
      b.className = "jk-more"; b.textContent = `Show ${Math.min(PAGE, shown.length - limit)} more`;
      b.onclick = () => { limit += PAGE; render(); };
      out.appendChild(b);
    }
  }

  const JAWIKT = "https://ja.wiktionary.org/wiki/";
  const KNWIKT = "https://kn.wiktionary.org/wiki/";
  const wl = (term, text, title) =>
    `<a href="${JAWIKT}${encodeURIComponent(term)}" target="_blank" rel="noopener" title="${title || term + " — Wiktionary (日本語)"}">${text}</a>`;
  // kun'yomi entry -> written word: まな(ぶ) -> 学ぶ ; ひと- -> 一 ; -び -> 日
  const kunWord = (k, kun) => { const m = kun.replace(/-/g, "").match(/\(([^)]*)\)/); return k + (m ? m[1] : ""); };

  function rowsFor(kana, roma, ek, kn, word) {
    return kana.map((x, i) => `<tr><td style="font-size:1.05rem">${word ? wl(word(x), x, word(x) + " — Wiktionary (日本語)") : x}</td><td>${roma[i]}</td><td><code>${ek[i]}</code></td><td>${kn[i]}</td></tr>`).join("");
  }

  function detail(k) {
    const r = data.find(x => x.k === k); if (!r) return;
    const bg = colour(r);
    $("jk-d-body").innerHTML = `
      <div class="jk-head"><a class="jk-big" id="jk-d-k" style="background:${bg}" href="${JAWIKT}${encodeURIComponent(r.k)}" target="_blank" rel="noopener" title="${r.k} — Wiktionary (日本語)">${r.k}</a>
        <div class="jk-meta"><div class="mean">${r.m.map(m => wl(m.toLowerCase(), m, `“${m.toLowerCase()}” — Japanese words for this meaning on Wiktionary (日本語)`)).join("; ")}</div>
          <div class="kn-mean">ಕನ್ನಡ ವಿಕ್ಷನರಿ: ${r.m.map(m => `<a href="${KNWIKT}${encodeURIComponent(m.toLowerCase())}" target="_blank" rel="noopener" title="“${m.toLowerCase()}” — Kannada Wiktionary">${m.toLowerCase()}</a>`).join(" · ")}</div>
          <span class="jk-tag" style="background:var(--g${r.g})">${gName(r.g)}</span>
          ${r.j ? `<span class="jk-tag" style="background:var(--j${r.j})">JLPT N${r.j}</span>` : ""}
          <span class="jk-tag">${r.s} strokes</span>
          ${r.f ? `<span class="jk-tag">#${r.f} in newspapers</span>` : ""}
          ${r.kj ? `<span class="jk-tag">kokuji — made in Japan</span>` : ""}</div></div>
      <h4>Usual reading (${r.ut === "on" ? "on'yomi" : "kun'yomi"})</h4>
      <table><tr><th>Kana</th><td style="font-size:1.2rem">${r.u || "—"}</td></tr>
        <tr><th>Romaji</th><td>${r.uR || "—"}</td></tr><tr><th>Eke</th><td><code>${r.uE || "—"}</code></td></tr>
        <tr><th>ಕನ್ನಡ</th><td>${r.uK || "—"}</td></tr></table>
      ${r.on.length ? `<h4>On'yomi — Chinese-derived, used in compounds</h4><table><tr><th>カナ</th><th>Romaji</th><th>Eke</th><th>ಕನ್ನಡ</th></tr>${rowsFor(r.on, r.onR, r.onE, r.onK)}</table>` : ""}
      ${r.kun.length ? `<h4>Kun'yomi — native Japanese</h4><table><tr><th>かな</th><th>Romaji</th><th>Eke</th><th>ಕನ್ನಡ</th></tr>${rowsFor(r.kun, r.kunR, r.kunE, r.kunK, x => kunWord(r.k, x))}</table>` : ""}
      <h4>Mandarin</h4><table><tr><th>Pinyin</th><td>${r.py || "—"}</td></tr></table>
      <p class="jk-links" style="margin-top:1rem">
        ${wl(r.k, "ウィクショナリー " + r.k)}
        <a href="https://ja.wiktionary.org/w/index.php?search=${encodeURIComponent("intitle:" + r.k)}&ns0=1&fulltext=1" target="_blank" rel="noopener">Wiktionary words with ${r.k}</a>
        <a href="https://jisho.org/search/${encodeURIComponent(r.k + " #kanji")}" target="_blank" rel="noopener">Jisho</a>
        <a href="https://jisho.org/search/${encodeURIComponent("*" + r.k + "*")}" target="_blank" rel="noopener">Words using ${r.k}</a>
        <a href="https://en.wiktionary.org/wiki/${encodeURIComponent(r.k)}" target="_blank" rel="noopener">Wiktionary</a></p>`;
    $("jk-detail").hidden = false;
    history.replaceState(null, "", "#" + encodeURIComponent(r.k));
  }
  function close() { $("jk-detail").hidden = true; history.replaceState(null, "", location.pathname + location.search); }

  $("jk-out").addEventListener("click", e => { const t = e.target.closest("[data-k]"); if (t) detail(t.dataset.k); });
  $("jk-out").addEventListener("keydown", e => { const t = e.target.closest("[data-k]"); if (t && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); detail(t.dataset.k); } });
  $("jk-detail").addEventListener("click", e => { if (e.target.id === "jk-detail" || e.target.classList.contains("jk-close")) close(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape" && !$("jk-detail").hidden) close(); });
  let timer; $("jk-q").addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(() => { limit = PAGE; render(); }, 120); });
  $("jk-sort").addEventListener("change", () => { limit = PAGE; render(); });
  $("jk-color").addEventListener("change", () => { chips(); render(); });
  $("jk-view").addEventListener("click", () => { table = !table; $("jk-view").textContent = table ? "Tile view" : "Table view"; render(); });

  fetch("joyo-kanji.json").then(r => r.json()).then(rows => {
    data = rows; data.forEach(index); chips(); render();
    const h = decodeURIComponent(location.hash.slice(1)); if (h) detail(h);
  }).catch(() => { $("jk-status").textContent = "Could not load joyo-kanji.json."; });
})();
</script>
