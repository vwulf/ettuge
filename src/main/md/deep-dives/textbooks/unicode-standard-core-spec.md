<a id="ch1"></a>
# The Unicode Standard, Version 18.0: Core Specification

> The Unicode Consortium · September 2026 · [the PDF in Drive](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view)

Your Drive had version 15.0; this page follows version 18.0, whose PDF was downloaded from unicode.org into the same folder. Since 16.0 the core specification is also published as authoritative HTML, so every chapter and numbered section links to its place there as well as to its PDF pages. Summaries and terms are per chapter. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The core specification of Unicode: the architecture, conformance rules and implementation guidance for the universal character encoding, followed by script-by-script descriptions of how each writing system is encoded and should be rendered. The first chapters define code points, encoding forms (UTF-8/16/32), normalization, character properties, bidirectional and boundary behavior, and implementation practices. Chapters 7–20 survey the world’s scripts by region, from Latin and Greek through West Asian, Indic and Southeast Asian scripts (including Kannada and the other Brahmic scripts), East Asian ideographs and Hangul, African and American scripts; later chapters cover notational systems, symbols and format characters, and how the code charts are organized.

**Contents**

1. [1 Introduction](ch1): What Unicode is and its design goals.
2. [2 General Structure](ch2): The architecture of the encoding.
3. [3 Conformance](ch3): Normative conformance requirements.
4. [4 Character Properties](ch4): Character properties and the UCD.
5. [5 Implementation Guidelines](ch5): Implementation guidelines.
6. [6 Writing Systems and Punctuation](ch6): Writing systems and punctuation.
7. [7 Europe-I](ch7): European alphabets I.
8. [8 Europe-II](ch8): European and ancient scripts II.
9. [9 West Asia-I](ch9): West Asian scripts I.
10. [10 West Asia-II](ch10): West Asian historic scripts II.
11. [11 Cuneiform and Hieroglyphs](ch11): Cuneiform and hieroglyphs.
12. [12 South and Central Asia-I](ch12): Major Indic scripts.
13. [13 South and Central Asia-II](ch13): South and Central Asian scripts II.
14. [14 South and Central Asia-III](ch14): Historic Asian scripts III.
15. [15 South and Central Asia-IV](ch15): Regional Brahmic scripts IV.
16. [16 Southeast Asia-I](ch16): Southeast Asian scripts I.
17. [17 Southeast Asia-II](ch17): Southeast Asian scripts II.
18. [18 East Asia](ch18): East Asian scripts.
19. [19 Africa](ch19): African scripts.
20. [20 Americas](ch20): Scripts of the Americas.
21. [21 Notational Systems](ch21): Notational systems.
22. [22 Symbols](ch22): Symbols.
23. [23 Special Areas and Format Characters](ch23): Special areas and format characters.
24. [24 About the Code Charts](ch24): Reading the code charts.
25. [A Notational Conventions](ch25): Notational conventions.
26. [B Unicode Publications and Resources](ch26): Publications and resources.
27. [C Relationship to ISO/IEC 10646](ch27): Unicode and ISO/IEC 10646.
28. [D Version History of the Standard](ch28): Version history.
29. [E Han Unification History](ch29): Han unification history.
30. [F Documentation of CJK Strokes](ch30): CJK strokes.


---

## 1 Introduction

*PDF pp. 35–43* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-1/)

What Unicode is and its design goals.

*Terms:* Unicode, coverage, design goals, text handling

**1.1 Coverage**  
→ PDF pp. 38–39 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-1/#G6600)

**1.2 Design Goals**  
→ PDF pp. 40–41 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-1/#G7110)

**1.3 Text Handling**  
→ PDF pp. 42–43 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-1/#G9708)


---

<a id="ch2"></a>
## 2 General Structure

*PDF pp. 44–110* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/)

The architecture of the encoding.

*Terms:* code points, characters vs glyphs, encoding forms, UTF-8, UTF-16, UTF-32, planes, allocation, writing direction, combining characters

**2.1 Architectural Context**  
→ PDF pp. 45–48 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G12888)

**2.2 Unicode Design Principles**  
→ PDF pp. 49–60 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G128)

**2.3 Compatibility Characters**  
→ PDF pp. 61–64 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G11062)

**2.4 Code Points and Characters**  
→ PDF pp. 65–68 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G25564)

**2.5 Encoding Forms**  
→ PDF pp. 69–75 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G13708)

**2.6 Encoding Schemes**  
→ PDF pp. 76–78 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G19273)

**2.7 Unicode Strings**  
→ PDF p. 79 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G18444)

**2.8 Unicode Allocation**  
→ PDF pp. 80–83 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G16417)

**2.9 Details of Allocation**  
→ PDF pp. 84–89 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G16482)

**2.10 Writing Direction**  
→ PDF pp. 90–91 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G6318)

**2.11 Combining Characters**  
→ PDF pp. 92–99 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G1708)

**2.12 Equivalent Sequences**  
→ PDF pp. 100–105 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G287424)

**2.13 Special Characters**  
→ PDF pp. 106–107 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G27981)

**2.14 Conforming to the Unicode Standard**  
→ PDF pp. 108–110 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-2/#G13854)


---

<a id="ch3"></a>
## 3 Conformance

*PDF pp. 111–213* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/)

Normative conformance requirements.

*Terms:* conformance, definitions, decomposition, canonical equivalence, normalization forms, encoding schemes, surrogates, Hangul jamo, default case algorithms

**3.1 Versions of the Unicode Standard**  
→ PDF pp. 112–117 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G2131)

**3.2 Conformance Requirements**  
→ PDF pp. 118–126 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G29705)

**3.3 Semantics**  
→ PDF pp. 127–129 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G19002)

**3.4 Characters and Encoding**  
→ PDF pp. 130–135 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G2212)

**3.5 Properties**  
→ PDF pp. 136–148 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G43463)

**3.6 Combination**  
→ PDF pp. 149–163 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G30602)

**3.7 Decomposition**  
→ PDF pp. 164–166 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G729)

**3.8 Surrogates**  
→ PDF p. 167 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G2630)

**3.9 Unicode Encoding Forms**  
→ PDF pp. 168–179 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G7404)

**3.10 Unicode Encoding Schemes**  
→ PDF pp. 180–184 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G28070)

**3.11 Normalization Forms**  
→ PDF pp. 185–193 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G49537)

**3.12 Conjoining Jamo Behavior**  
→ PDF pp. 194–204 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G24646)

**3.13 Default Case Algorithms**  
→ PDF pp. 205–213 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/#G33992)


---

<a id="ch4"></a>
## 4 Character Properties

*PDF pp. 214–255* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/)

Character properties and the UCD.

*Terms:* Unicode Character Database, case, combining classes, Bidi class, General Category, numeric values, names, text boundaries, default ignorable

**4.1 Unicode Character Database**  
→ PDF pp. 216–218 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G124718)

**4.2 Case**  
→ PDF pp. 219–222 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G124722)

**4.3 Combining Classes**  
→ PDF pp. 223–226 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G32493)

**4.4 Directionality**  
→ PDF p. 227 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G130746)

**4.5 General Category**  
→ PDF pp. 228–231 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G124142)

**4.6 Numeric Value**  
→ PDF pp. 232–235 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G124206)

**4.7 Bidi Mirrored**  
→ PDF pp. 236–237 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G30078)

**4.8 Name**  
→ PDF pp. 238–247 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G2082)

**4.9 Unicode 1.0 Names**  
→ PDF p. 248 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G131216)

**4.10 Letters, Alphabetic, and Ideographic**  
→ PDF p. 249 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G91002)

**4.11 Properties for Text Boundaries**  
→ PDF p. 250 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G124804)

**4.12 Characters with Unusual Properties**  
→ PDF pp. 251–254 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G124820)

**4.13 Characters and Sequences That Should Not Be Emitted**  
→ PDF p. 255 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-4/#G124821)


---

<a id="ch5"></a>
## 5 Implementation Guidelines

*PDF pp. 256–325* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/)

Implementation guidelines.

*Terms:* character conversion, programming languages, surrogate handling, normalization, line breaking, regular expressions, sorting, identifiers

**5.1 Data Structures for Character Conversion**  
→ PDF pp. 257–259 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G11079)

**5.2 Programming Languages and Data Types**  
→ PDF pp. 260–261 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G23927)

**5.3 Unknown and Missing Characters**  
→ PDF pp. 262–263 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G7730)

**5.4 Handling Surrogate Pairs in UTF-16**  
→ PDF pp. 264–266 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G11318)

**5.5 Handling Numbers**  
→ PDF p. 267 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G34360)

**5.6 Normalization**  
→ PDF pp. 268–269 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G7889)

**5.7 Compression**  
→ PDF p. 270 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G518)

**5.8 Newline Guidelines**  
→ PDF pp. 271–275 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G10213)

**5.9 Regular Expressions**  
→ PDF p. 276 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G12107)

**5.10 Language Information in Plain Text**  
→ PDF pp. 277–278 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G11552)

**5.11 Editing and Selection**  
→ PDF pp. 279–281 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G3067)

**5.12 Strategies for Handling Nonspacing Marks**  
→ PDF pp. 282–285 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G1050)

**5.13 Rendering Nonspacing Marks**  
→ PDF pp. 286–292 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G1095)

**5.14 Locating Text Element Boundaries**  
→ PDF p. 293 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G780)

**5.15 Identifiers**  
→ PDF p. 294 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G3248)

**5.16 Sorting and Searching**  
→ PDF pp. 295–297 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G664)

**5.17 Binary Order**  
→ PDF pp. 298–300 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G21249)

**5.18 Case Mappings**  
→ PDF pp. 301–309 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G21180)

**5.19 Mapping Compatibility Variants**  
→ PDF pp. 310–311 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G37346)

**5.20 Unicode Security**  
→ PDF pp. 312–315 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G37318)

**5.21 Ignoring Characters in Processing**  
→ PDF pp. 316–324 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G40025)

**5.22 U+FFFD Substitution in Conversion**  
→ PDF p. 325 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-5/#G40630)


---

<a id="ch6"></a>
## 6 Writing Systems and Punctuation

*PDF pp. 326–368* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-6/)

Writing systems and punctuation.

*Terms:* writing system types, alphabets, abjads, abugidas, syllabaries, general punctuation

**6.1 Writing Systems**  
→ PDF pp. 328–334 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-6/#G7382)

**6.2 General Punctuation**  
→ PDF pp. 335–368 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-6/#G7981)


---

<a id="ch7"></a>
## 7 Europe-I

*PDF pp. 369–439* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/)

European alphabets I.

*Terms:* Latin, Greek, Coptic, Cyrillic, Glagolitic, Armenian, Georgian, modifier letters, combining marks

**7.1 Latin**  
→ PDF pp. 371–393 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G4321)

**7.2 Greek**  
→ PDF pp. 394–402 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G10832)

**7.3 Coptic**  
→ PDF pp. 403–406 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G16256)

**7.4 Cyrillic**  
→ PDF pp. 407–412 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G10850)

**7.5 Glagolitic**  
→ PDF pp. 413–414 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G15862)

**7.6 Armenian**  
→ PDF pp. 415–417 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G3334)

**7.7 Georgian**  
→ PDF pp. 418–420 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G3360)

**7.8 Modifier Letters**  
→ PDF pp. 421–425 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G15832)

**7.9 Combining Marks**  
→ PDF pp. 426–439 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-7/#G18195)


---

<a id="ch8"></a>
## 8 Europe-II

*PDF pp. 440–468* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/)

European and ancient scripts II.

*Terms:* Linear A, Linear B, Cypriot, Old Italic, Runic, Gothic, Ogham, Shavian

**8.1 Linear A**  
→ PDF p. 442 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G27575)

**8.2 Linear B**  
→ PDF pp. 443–444 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G29566)

**8.3 Cypriot Syllabary**  
→ PDF pp. 445–446 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G26417)

**8.4 Cypro-Minoan**  
→ PDF p. 447 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G39686)

**8.5 Ancient Anatolian Alphabets**  
→ PDF pp. 448–449 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G26505)

**8.6 Old Italic**  
→ PDF pp. 450–452 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G27379)

**8.7 Runic**  
→ PDF pp. 453–455 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G26624)

**8.8 Old Hungarian**  
→ PDF p. 456 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G33926)

**8.9 Gothic**  
→ PDF p. 457 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G33932)

**8.10 Elbasan**  
→ PDF pp. 458–459 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G27032)

**8.11 Caucasian Albanian**  
→ PDF p. 460 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G32223)

**8.12 Vithkuqi**  
→ PDF p. 461 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G40863)

**8.13 Todhri**  
→ PDF p. 462 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G746332)

**8.14 Old Permic**  
→ PDF pp. 463–464 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G31220)

**8.15 Ogham**  
→ PDF pp. 465–466 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G29182)

**8.16 Shavian**  
→ PDF p. 467 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G27260)

**8.17 Sidetic**  
→ PDF p. 468 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/#G27262)


---

<a id="ch9"></a>
## 9 West Asia-I

*PDF pp. 469–533* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-9/)

West Asian scripts I.

*Terms:* Hebrew, Arabic, Syriac, Samaritan, Mandaic, Yezidi, bidirectional, cursive joining

**9.1 Hebrew**  
→ PDF pp. 471–478 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-9/#G6528)

**9.2 Arabic**  
→ PDF pp. 479–513 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-9/#G20596)

**9.3 Syriac**  
→ PDF pp. 514–524 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-9/#G13005)

**9.4 Samaritan**  
→ PDF pp. 525–527 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-9/#G34422)

**9.5 Mandaic**  
→ PDF pp. 528–531 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-9/#G46613)

**9.6 Yezidi**  
→ PDF pp. 532–533 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-9/#G59804)


---

<a id="ch10"></a>
## 10 West Asia-II

*PDF pp. 534–558* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/)

West Asian historic scripts II.

*Terms:* Phoenician, Aramaic, Avestan, Pahlavi, Nabataean, Palmyrene

**10.1 Old North Arabian**  
→ PDF p. 536 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G26432)

**10.2 Old South Arabian**  
→ PDF pp. 537–539 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G29209)

**10.3 Phoenician**  
→ PDF pp. 540–541 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G26686)

**10.4 Imperial Aramaic**  
→ PDF pp. 542–543 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G29567)

**10.5 Manichaean**  
→ PDF pp. 544–547 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G27561)

**10.6 Pahlavi and Parthian**  
→ PDF pp. 548–550 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G32800)

**10.7 Avestan**  
→ PDF pp. 551–552 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G29021)

**10.8 Chorasmian**  
→ PDF p. 553 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G43165)

**10.9 Elymaic**  
→ PDF p. 554 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G41970)

**10.10 Nabataean**  
→ PDF p. 555 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G29596)

**10.11 Palmyrene**  
→ PDF pp. 556–557 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G29599)

**10.12 Hatran**  
→ PDF p. 558 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-10/#G34825)


---

<a id="ch11"></a>
## 11 Cuneiform and Hieroglyphs

*PDF pp. 559–586* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-11/)

Cuneiform and hieroglyphs.

*Terms:* Sumero-Akkadian cuneiform, Ugaritic, Old Persian, Egyptian hieroglyphs, Meroitic, Anatolian hieroglyphs

**11.1 Sumero-Akkadian**  
→ PDF pp. 560–565 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-11/#G26852)

**11.2 Ugaritic**  
→ PDF p. 566 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-11/#G26461)

**11.3 Old Persian**  
→ PDF p. 567 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-11/#G26474)

**11.4 Egyptian Hieroglyphs**  
→ PDF pp. 568–582 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-11/#G26607)

**11.5 Meroitic**  
→ PDF pp. 583–584 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-11/#G26724)

**11.6 Anatolian Hieroglyphs**  
→ PDF pp. 585–586 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-11/#G27920)


---

<a id="ch12"></a>
## 12 South and Central Asia-I

*PDF pp. 587–675* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/)

Major Indic scripts.

*Terms:* Devanagari, Bengali, Gurmukhi, Gujarati, Odia, Tamil, Telugu, Kannada, Malayalam, virama, conjuncts, dead consonants, rendering

**12.1 Devanagari**  
→ PDF pp. 589–620 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G12284)

**12.2 Bengali (Bangla)**  
→ PDF pp. 621–629 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G664195)

**12.3 Gurmukhi**  
→ PDF pp. 630–635 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G668388)

**12.4 Gujarati**  
→ PDF pp. 636–638 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G34334)

**12.5 Oriya (Odia)**  
→ PDF pp. 639–643 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G10153)

**12.6 Tamil**  
→ PDF pp. 644–655 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G10162)

**12.7 Telugu**  
→ PDF pp. 656–659 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G81985)

**12.8 Kannada**  
→ PDF pp. 660–664 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G38298)

**12.9 Malayalam**  
→ PDF pp. 665–675 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-12/#G22346)


---

<a id="ch13"></a>
## 13 South and Central Asia-II

*PDF pp. 676–757* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/)

South and Central Asian scripts II.

*Terms:* Sinhala, Tibetan, Mongolian, Thaana, Ol Chiki, Chakma, Lepcha, Masaram Gondi

**13.1 Thaana**  
→ PDF pp. 679–680 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G26451)

**13.2 Sinhala**  
→ PDF pp. 681–686 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G26561)

**13.3 Newa**  
→ PDF pp. 687–689 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G31609)

**13.4 Tibetan**  
→ PDF pp. 690–704 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G31615)

**13.5 Mongolian**  
→ PDF pp. 705–716 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G27803)

**13.6 Limbu**  
→ PDF pp. 717–721 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G27263)

**13.7 Meetei Mayek**  
→ PDF pp. 722–724 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G27615)

**13.8 Mro**  
→ PDF p. 725 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G27701)

**13.9 Warang Citi**  
→ PDF p. 726 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G27702)

**13.10 Ol Chiki**  
→ PDF pp. 727–728 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G29195)

**13.11 Ol Onal**  
→ PDF pp. 729–730 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G746334)

**13.12 Nag Mundari**  
→ PDF pp. 731–732 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G112439)

**13.13 Chakma**  
→ PDF pp. 733–734 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G27486)

**13.14 Lepcha**  
→ PDF pp. 735–737 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G27253)

**13.15 Saurashtra**  
→ PDF pp. 738–739 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G28198)

**13.16 Masaram Gondi**  
→ PDF pp. 740–742 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G33278)

**13.17 Gunjala Gondi**  
→ PDF pp. 743–744 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G39306)

**13.18 Wancho**  
→ PDF p. 745 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G46061)

**13.19 Toto**  
→ PDF p. 746 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G50178)

**13.20 Tangsa**  
→ PDF p. 747 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G51897)

**13.21 Sunuwar**  
→ PDF pp. 748–750 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G746336)

**13.22 Gurung Khema**  
→ PDF pp. 751–753 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G746338)

**13.23 Kirat Rai**  
→ PDF pp. 754–755 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G746340)

**13.24 Tolong Siki**  
→ PDF pp. 756–757 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/#G746342)


---

<a id="ch14"></a>
## 14 South and Central Asia-III

*PDF pp. 758–795* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/)

Historic Asian scripts III.

*Terms:* Brahmi, Kharoshthi, Phags-pa, Old Turkic, Sogdian, Old Uyghur

**14.1 Brahmi**  
→ PDF pp. 760–764 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G39063)

**14.2 Kharoshthi**  
→ PDF pp. 765–771 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G38474)

**14.3 Bhaiksuki**  
→ PDF pp. 772–773 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G40424)

**14.4 Phags-pa**  
→ PDF pp. 774–781 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G40430)

**14.5 Marchen**  
→ PDF p. 782 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G38187)

**14.6 Zanabazar Square**  
→ PDF pp. 783–786 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G41935)

**14.7 Soyombo**  
→ PDF pp. 787–788 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G41941)

**14.8 Old Turkic**  
→ PDF pp. 789–790 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G41975)

**14.9 Old Sogdian**  
→ PDF p. 791 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G49463)

**14.10 Sogdian**  
→ PDF pp. 792–793 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G49476)

**14.11 Old Uyghur**  
→ PDF pp. 794–795 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-14/#G58161)


---

<a id="ch15"></a>
## 15 South and Central Asia-IV

*PDF pp. 796–846* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/)

Regional Brahmic scripts IV.

*Terms:* Kaithi, Sharada, Takri, Siddham, Modi, Grantha, Tirhuta, Tulu-Tigalari, Ahom

**15.1 Syloti Nagri**  
→ PDF pp. 799–800 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G59104)

**15.2 Kaithi**  
→ PDF pp. 801–803 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G69704)

**15.3 Sharada**  
→ PDF pp. 804–806 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G81154)

**15.4 Takri**  
→ PDF pp. 807–808 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G81184)

**15.5 Siddham**  
→ PDF pp. 809–811 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G80829)

**15.6 Mahajani**  
→ PDF pp. 812–813 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G89564)

**15.7 Khojki**  
→ PDF pp. 814–816 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G81423)

**15.8 Dogra**  
→ PDF pp. 817–818 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G100066)

**15.9 Khudawadi**  
→ PDF pp. 819–820 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G80879)

**15.10 Multani**  
→ PDF pp. 821–822 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G95487)

**15.11 Tirhuta**  
→ PDF pp. 823–825 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G95493)

**15.12 Modi**  
→ PDF pp. 826–829 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G80897)

**15.13 Nandinagari**  
→ PDF pp. 830–831 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G106413)

**15.14 Grantha**  
→ PDF pp. 832–835 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G81052)

**15.15 Dives Akuru**  
→ PDF pp. 836–837 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G108027)

**15.16 Ahom**  
→ PDF pp. 838–839 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G95570)

**15.17 Sora Sompeng**  
→ PDF p. 840 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G95556)

**15.18 Tulu-Tigalari**  
→ PDF pp. 841–846 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-15/#G746412)


---

<a id="ch16"></a>
## 16 Southeast Asia-I

*PDF pp. 847–916* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/)

Southeast Asian scripts I.

*Terms:* Thai, Lao, Myanmar, Khmer, Tai Tham, Cham, Hmong

**16.1 Thai**  
→ PDF pp. 849–853 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G46485)

**16.2 Lao**  
→ PDF pp. 854–857 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G10988)

**16.3 Myanmar**  
→ PDF pp. 858–866 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G24999)

**16.4 Khmer**  
→ PDF pp. 867–883 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G64642)

**16.5 Tai Le**  
→ PDF pp. 884–886 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G32903)

**16.6 New Tai Lue**  
→ PDF pp. 887–889 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G65706)

**16.7 Tai Tham**  
→ PDF pp. 890–892 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G53337)

**16.8 Tai Viet**  
→ PDF pp. 893–895 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G59747)

**16.9 Kayah Li**  
→ PDF pp. 896–897 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G61902)

**16.10 Cham**  
→ PDF pp. 898–900 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G55659)

**16.11 Pahawh Hmong**  
→ PDF pp. 901–903 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G68320)

**16.12 Nyiakeng Puachue Hmong**  
→ PDF pp. 904–905 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G81876)

**16.13 Pau Cin Hau**  
→ PDF pp. 906–907 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G68308)

**16.14 Hanifi Rohingya**  
→ PDF pp. 908–909 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G73728)

**16.15 Tai Yo**  
→ PDF pp. 910–916 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/#G73729)


---

<a id="ch17"></a>
## 17 Southeast Asia-II

*PDF pp. 917–950* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/)

Southeast Asian scripts II.

*Terms:* Baybayin, Buginese, Balinese, Javanese, Batak, Sundanese, Kawi

**17.1 Philippine Scripts: Tagalog, Hanunóo, Buhid, and Tagbanwa**  
→ PDF pp. 918–921 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G26433)

**17.2 Buginese**  
→ PDF pp. 922–923 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G26727)

**17.3 Balinese**  
→ PDF pp. 924–931 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G26759)

**17.4 Javanese**  
→ PDF pp. 932–935 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G27153)

**17.5 Rejang**  
→ PDF pp. 936–937 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G27208)

**17.6 Batak**  
→ PDF pp. 938–939 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G27226)

**17.7 Sundanese**  
→ PDF pp. 940–942 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G27244)

**17.8 Makasar**  
→ PDF pp. 943–944 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G29334)

**17.9 Kawi**  
→ PDF pp. 945–950 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-17/#G40419)


---

<a id="ch18"></a>
## 18 East Asia

*PDF pp. 951–1023* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/)

East Asian scripts.

*Terms:* Han, CJK unified ideographs, ideographic description, Bopomofo, Hiragana, Katakana, Hangul, Yi, Tangut, Khitan, Nüshu

**18.1 Han**  
→ PDF pp. 954–977 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G29086)

**18.2 Ideographic Description Characters**  
→ PDF pp. 978–983 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G28626)

**18.3 Bopomofo**  
→ PDF pp. 984–987 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G22467)

**18.4 Hiragana and Katakana**  
→ PDF pp. 988–994 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G22462)

**18.5 Halfwidth and Fullwidth Forms**  
→ PDF pp. 995–996 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G37555)

**18.6 Hangul**  
→ PDF pp. 997–1001 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G31028)

**18.7 Yi**  
→ PDF pp. 1002–1005 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G13042)

**18.8 Nüshu**  
→ PDF p. 1006 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G42061)

**18.9 Lisu**  
→ PDF pp. 1007–1010 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G44587)

**18.10 Miao**  
→ PDF pp. 1011–1012 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G42236)

**18.11 Tangut**  
→ PDF pp. 1013–1015 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G43635)

**18.12 Khitan Small Script**  
→ PDF pp. 1016–1018 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G59285)

**18.13 Jurchen**  
→ PDF pp. 1019–1020 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G59286)

**18.14 Seal**  
→ PDF pp. 1021–1023 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-18/#G59287)


---

<a id="ch19"></a>
## 19 Africa

*PDF pp. 1024–1055* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/)

African scripts.

*Terms:* Ethiopic, Tifinagh, N’Ko, Vai, Bamum, Adlam, Garay

**19.1 Ethiopic**  
→ PDF pp. 1025–1029 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G14116)

**19.2 Osmanya**  
→ PDF p. 1030 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G16914)

**19.3 Tifinagh**  
→ PDF pp. 1031–1034 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G43184)

**19.4 N’Ko**  
→ PDF pp. 1035–1041 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G18603)

**19.5 Vai**  
→ PDF pp. 1042–1043 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G18604)

**19.6 Bamum**  
→ PDF pp. 1044–1045 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G45398)

**19.7 Bassa Vah**  
→ PDF p. 1046 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G54402)

**19.8 Mende Kikakui**  
→ PDF pp. 1047–1048 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G54425)

**19.9 Adlam**  
→ PDF pp. 1049–1051 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G56860)

**19.10 Medefaidrin**  
→ PDF p. 1052 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G58353)

**19.11 Garay**  
→ PDF pp. 1053–1054 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G746355)

**19.12 Beria Erfe**  
→ PDF p. 1055 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-19/#G746359)


---

<a id="ch20"></a>
## 20 Americas

*PDF pp. 1056–1066* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-20/)

Scripts of the Americas.

*Terms:* Cherokee, Canadian Aboriginal Syllabics, Osage, Deseret

**20.1 Cherokee**  
→ PDF pp. 1057–1059 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-20/#G26612)

**20.2 Canadian Aboriginal Syllabics**  
→ PDF pp. 1060–1062 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-20/#G26630)

**20.3 Osage**  
→ PDF p. 1063 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-20/#G26674)

**20.4 Deseret**  
→ PDF pp. 1064–1066 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-20/#G27507)


---

<a id="ch21"></a>
## 21 Notational Systems

*PDF pp. 1067–1088* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-21/)

Notational systems.

*Terms:* Braille, musical symbols, Duployan shorthand, SignWriting

**21.1 Braille**  
→ PDF pp. 1068–1070 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-21/#G26597)

**21.2 Western Musical Symbols**  
→ PDF pp. 1071–1078 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-21/#G26709)

**21.3 Byzantine Musical Symbols**  
→ PDF p. 1079 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-21/#G29047)

**21.4 Znamenny Musical Notation**  
→ PDF p. 1080 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-21/#G35157)

**21.5 Ancient Greek Musical Notation**  
→ PDF pp. 1081–1084 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-21/#G26878)

**21.6 Duployan**  
→ PDF pp. 1085–1086 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-21/#G27643)

**21.7 Sutton SignWriting**  
→ PDF pp. 1087–1088 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-21/#G28865)


---

<a id="ch22"></a>
## 22 Symbols

*PDF pp. 1089–1170* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/)

Symbols.

*Terms:* currency symbols, letterlike symbols, numerals, mathematical symbols, technical symbols, geometric shapes, emoji, dingbats

**22.1 Currency Symbols**  
→ PDF pp. 1091–1095 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G13244)

**22.2 Letterlike Symbols**  
→ PDF pp. 1096–1104 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G14143)

**22.3 Numerals**  
→ PDF pp. 1105–1121 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G12146)

**22.4 Superscript and Subscript Symbols**  
→ PDF pp. 1122–1123 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G42931)

**22.5 Mathematical Symbols**  
→ PDF pp. 1124–1134 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G51347)

**22.6 Invisible Mathematical Operators**  
→ PDF p. 1135 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G26223)

**22.7 Technical Symbols**  
→ PDF pp. 1136–1142 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G12243)

**22.8 Geometrical Symbols**  
→ PDF pp. 1143–1146 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G27321)

**22.9 Miscellaneous Symbols**  
→ PDF pp. 1147–1163 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G12367)

**22.10 Enclosed and Square**  
→ PDF pp. 1164–1170 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-22/#G41738)


---

<a id="ch23"></a>
## 23 Special Areas and Format Characters

*PDF pp. 1171–1210* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/)

Special areas and format characters.

*Terms:* control codes, zero width joiner, variation selectors, private use, noncharacters, BOM, tag characters

**23.1 Control Codes**  
→ PDF pp. 1172–1174 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G20365)

**23.2 Layout Controls**  
→ PDF pp. 1175–1188 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G12985)

**23.3 Deprecated Format Characters**  
→ PDF pp. 1189–1191 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G19593)

**23.4 Variation Selectors**  
→ PDF pp. 1192–1194 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G19053)

**23.5 Private-Use Characters**  
→ PDF pp. 1195–1198 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G19184)

**23.6 Surrogates Area**  
→ PDF p. 1199 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G24089)

**23.7 Noncharacters**  
→ PDF pp. 1200–1201 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G12612)

**23.8 Specials and the Byte Order Mark (BOM)**  
→ PDF pp. 1202–1209 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G19635)

**23.9 Tag Characters**  
→ PDF p. 1210 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-23/#G30110)


---

<a id="ch24"></a>
## 24 About the Code Charts

*PDF pp. 1211–1234* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-24/)

Reading the code charts.

*Terms:* code charts, names list, CJK charts, Hangul syllables

**24.1 Character Names List**  
→ PDF pp. 1212–1228 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-24/#G2841)

**24.2 CJK and Other Ideographs**  
→ PDF pp. 1229–1233 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-24/#G3563)

**24.3 Hangul Syllables**  
→ PDF p. 1234 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-24/#G8005)


---

<a id="ch25"></a>
## A Notational Conventions

*PDF pp. 1235–1242* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-a/)

Notational conventions.

*Terms:* typographic conventions, EBNF, rendering

**A.1 Typographic Conventions**  
→ PDF pp. 1236–1238 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-a/#G12668)

**A.2 Extended BNF**  
→ PDF pp. 1239–1241 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-a/#G7146)

**A.3 Rendering**  
→ PDF p. 1242 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-a/#G7111)


---

<a id="ch26"></a>
## B Unicode Publications and Resources

*PDF pp. 1243–1246* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-b/)

Publications and resources.

*Terms:* Unicode Consortium, technical reports, UCD files

**B.1 The Unicode Consortium**  
→ PDF pp. 1244–1245 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-b/#G5982)

**B.2 Unicode Publications**  
→ PDF p. 1246 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-b/#G5406)


---

<a id="ch27"></a>
## C Relationship to ISO/IEC 10646

*PDF pp. 1247–1263* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-c/)

Unicode and ISO/IEC 10646.

*Terms:* ISO/IEC 10646, UCS, synchronization, character names

**C.1 History**  
→ PDF pp. 1248–1257 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-c/#G1824)

**C.2 Encoding Forms in ISO/IEC 10646**  
→ PDF p. 1258 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-c/#G8861)

**C.3 UTF-8 and UTF-16**  
→ PDF p. 1259 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-c/#G4651)

**C.4 Synchronization of the Standards**  
→ PDF p. 1260 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-c/#G1864)

**C.5 Identification of Features for Unicode**  
→ PDF p. 1261 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-c/#G1867)

**C.6 Character Names**  
→ PDF p. 1262 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-c/#G5401)

**C.7 Character Functional Specifications**  
→ PDF p. 1263 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-c/#G5447)


---

<a id="ch28"></a>
## D Version History of the Standard

*PDF pp. 1264–1265* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-d/)

Version history.

*Terms:* versions, release history

→ PDF pp. 1264–1265 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-d/)


---

<a id="ch29"></a>
## E Han Unification History

*PDF pp. 1266–1272* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-e/)

Han unification history.

*Terms:* Han unification, URO, CJK sources

**E.1 Development of the URO**  
→ PDF pp. 1267–1268 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-e/#G1281)

**E.2 Continuing Research on Ideographs**  
→ PDF pp. 1269–1271 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-e/#G17834)

**E.3 CJK Sources**  
→ PDF p. 1272 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-e/#G15393)


---

<a id="ch30"></a>
## F Documentation of CJK Strokes

*PDF pp. 1273–1280* · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-f/)

CJK strokes.

*Terms:* CJK strokes, stroke documentation

→ PDF pp. 1273–1280 in [the PDF](https://drive.google.com/file/d/1PI7cBaBnQXheccTGNcJ52oW_0Wlr1cjl/view) · [read online](https://www.unicode.org/versions/Unicode18.0.0/core-spec/appendix-f/)

