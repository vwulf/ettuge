import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
rows=json.load(open('joyo.json'))
GRADE={1:("Grade 1","D9EAD3"),2:("Grade 2","CFE2F3"),3:("Grade 3","D9D2E9"),4:("Grade 4","FCE5CD"),
       5:("Grade 5","F4CCCC"),6:("Grade 6","FFF2CC"),8:("Secondary","EFEFEF")}
wb=Workbook(); ws=wb.active; ws.title="Jōyō Kanji 2136"
hdr=["#","Kanji","Grade","JLPT","Strokes","Freq rank","Meaning",
     "Usual reading","Usual (type)","Usual (romaji)","Usual (Eke)","Usual (ಕನ್ನಡ)",
     "On'yomi (カナ)","On'yomi (romaji)","On'yomi (Eke)","On'yomi (ಕನ್ನಡ)",
     "Kun'yomi (かな)","Kun'yomi (romaji)","Kun'yomi (Eke)","Kun'yomi (ಕನ್ನಡ)","Mandarin (pinyin)","Kokuji"]
ws.append(hdr)
F=Font(name="Arial",size=10); FB=Font(name="Arial",size=10,bold=True,color="FFFFFF")
for c in ws[1]:
    c.font=FB; c.fill=PatternFill("solid",fgColor="434343"); c.alignment=Alignment(vertical="center",wrap_text=True)
J=lambda x:"、".join(x); C=lambda x:", ".join(x)
for r in rows:
    ws.append([r["n"],r["k"],GRADE[r["g"]][0],f"N{r['j']}" if r["j"] else "",r["s"],r["f"],"; ".join(r["m"][:4]),
               r["u"],r["ut"],r["uR"],r["uE"],r["uK"],
               J(r["on"]),C(r["onR"]),C(r["onE"]),C(r["onK"]),
               J(r["kun"]),C(r["kunR"]),C(r["kunE"]),C(r["kunK"]),r["py"] or "","yes" if r["kj"] else ""])
    fill=PatternFill("solid",fgColor=GRADE[r["g"]][1])
    for c in ws[ws.max_row]:
        c.font=F; c.fill=fill; c.alignment=Alignment(vertical="top",wrap_text=False)
    ws.cell(ws.max_row,2).font=Font(name="Arial",size=16)
widths=[6,7,10,6,7,8,30,12,8,12,12,12,16,18,18,18,26,30,30,30,16,7]
for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
ws.freeze_panes="C2"; ws.auto_filter.ref=f"A1:{get_column_letter(len(hdr))}{ws.max_row}"
ws.row_dimensions[1].height=30
lg=wb.create_sheet("Legend")
lg.append(["Jōyō kanji (常用漢字) — all 2,136, with readings in kana, romaji, Eke and Kannada"]); lg["A1"].font=Font(name="Arial",size=13,bold=True)
lg.append([])
lg.append(["Grade","Colour","Count"])
for i,(g,(name,col)) in enumerate(GRADE.items()):
    lg.append([name,"",f"=COUNTIF('Jōyō Kanji 2136'!C:C,A{lg.max_row+1})"])
    lg.cell(lg.max_row,2).fill=PatternFill("solid",fgColor=col)
lg.append(["Total","",f"=SUM(C4:C{lg.max_row})"])
notes=["",
"Columns",
"Usual reading — the reading you are most likely to meet. Taken from WaniKani's primary reading where it has one, else the first on'yomi, else the first kun'yomi. 'on' = Chinese-derived (used in most compounds), 'kun' = native Japanese.",
"Kun'yomi — okurigana (kana written after the kanji) shown in brackets: か(つ) = 勝つ. A leading/trailing hyphen marks a prefix/suffix form.",
"Romaji — Hepburn, long vowels with macrons (ō, ū).",
"Eke — c = ch (ಚ), S = sh (ಶ), j = j (ಜ), ts = ts (ತ್ಸ), v = w (ವ), capital vowel = long vowel (kO = こう). Small っ doubles the next consonant.",
"ಕನ್ನಡ — approximate Kannada spelling: ん = ಂ (ನ್ before a vowel or y), z = ಜ಼, f = ಫ಼, long vowels with ಾ ೀ ೂ ೇ ೋ.",
"Freq rank — rank among the ~2,500 most common kanji in newspapers (KANJIDIC); blank = not ranked.",
"JLPT — level in the current N5–N1 scheme (unofficial lists); blank = not assigned.",
"Grade — school year per the MEXT 2017 table in force from April 2020 (1,026 primary + 1,110 secondary).",
"Default sort: grade, then frequency. Use the filter buttons to sort or filter by any column.",
"",
"Sources",
"KANJIDIC2 (EDRDG, CC BY-SA 4.0) via davidluzgouveia/kanji-data (MIT), with JLPT and WaniKani data — https://github.com/davidluzgouveia/kanji-data",
"Mandarin readings: Unicode Unihan via mozillazg/pinyin-data (MIT) — https://github.com/mozillazg/pinyin-data",
"Grades 4–6: MEXT gakunenbetsu kanji haitōhyō (2017 revision), as listed on Wikipedia 'Kyōiku kanji'.",
"Readings are KANJIDIC's, which include some readings beyond the official jōyō list."]
for n in notes:
    lg.append([n]); lg.cell(lg.max_row,1).font=Font(name="Arial",size=10,bold=n in("Columns","Sources"))
for row in lg.iter_rows(min_row=3,max_row=11):
    for c in row: c.font=Font(name="Arial",size=10,bold=c.row==3)
lg.column_dimensions["A"].width=14; lg.column_dimensions["B"].width=10; lg.column_dimensions["C"].width=10
wb.save("joyo_kanji_2136.xlsx")
