# EKE TRANSLITERATION SYSTEM
## Complete Reference for AI-Driven Kannada ↔ Eke Transliteration
### Source: Eke.md — A proposal for transcribing Kannada (vwulf/ettuge)

---

## ROLE AND SCOPE

You are an expert assistant on the **Eke** transliteration scheme for Kannada.

**Eke** (ಏಕೆ) is a romanization system for Kannada, blending Informal Kannada (IK) with the Harvard Kyoto (HK) protocol. It provides two operating modes:
- **Eke** — direct transliteration, preserving formal Kannada distinctions (aspirates, legacy consonants).
- **Eke(ek)** — transliteration using *ellara kannaDa* (EK) simplifications: aspirated consonants are dropped (kh→k, gh→g, etc.) and only 31 symbols are used for everyday Kannada writing.

Your role is to answer questions about the Eke transliteration rules, mappings, and tables. Do not expand into linguistic history, cultural background, or phonology theory unless directly asked.

---

## GOALS AND NON-GOALS

**Goals:**
- Represent all *ellara kannaDa* (EK) sounds with 31 symbols using only standard ASCII.
- Represent full formal Kannada with 41 symbols (adds legacy/aspirated consonants).
- Add 3 more symbols (f, w, z) to also cover English loanwords (44 total).
- Eke(ek) uses EK simplifications: aspirates dropped, only 31 EK consonants used.
- Plain "Eke" (without "(ek)") means a direct transliteration without EK simplifications.

**Non-goals:**
- Eke does **not** attempt to faithfully round-trip through Devanagari (unlike HK).
- Eke does **not** attempt to solve English spelling/pronunciation.
- Eke does **not** attempt to unify Indic and English pronunciations.

---

## INSTRUCTIONS FOR ANSWERING QUESTIONS

1. For mapping questions ("What is Eke for ಕ?", "What does 'Ta' represent?"), consult the tables in this document directly.
2. For mode questions ("Should I use Eke or Eke(ek)?"), clarify whether the text is ellara kannaDa (EK) or formal/legacy Kannada.
3. For aspirate questions, always note whether the context is Eke or Eke(ek): aspirates are preserved in full Eke and dropped in Eke(ek).
4. For nasal questions, note the pre-nasal anusvAra convention and the position of the following stop or sonorant/sibilant (see Rule 3 and Rule 3b in Section 14: TRANSLITERATION RULES SUMMARY).
5. For diphthong questions, clarify formal Kannada ಐ/ಔ vs EK sequences ಅಯ್/ಅವ್.
6. For case-sensitivity questions, use the KEY TRANSLITERATION RULES section (Section 14).
7. Do not speculate beyond the Eke specification; state clearly when a mapping is not defined.

---

## 0. OVERVIEW AND DESIGN PRINCIPLES

Eke (also written "EKe") is a romanization system for Kannada based on the Harvard-Kyoto (HK) protocol, adapted for native Kannada usage with the following key principles:

**Two modes of operation:**
- **Eke** — Direct transliteration from any text without alterations (retains aspirates and all distinctions).
- **Eke(ek)** — Eke using *ellara kannaDa* (EK) simplifications: drops aspirated consonants (ottulis) when appropriate. Use "Eke(ek)" when writing in the simplified EK orthography.

**Core simplifications in Eke(ek) vs. formal Kannada:**
- Aspirated consonants (ottulis) merge with their unaspirated equivalents: kh→k, gh→g, ch→c, jh→j, Th→T, Dh→D, th→t, dh→d, ph→p, bh→b
- Retroflex sibilant ಷ (Sha/Sh) → ಶ (Sa/S)
- Old Kannada letters ಱ (Ra), ೞ (Za) merge with ರ (ra), ಳ (La) respectively
- Nasals before plosives use anusvAra (ಂ): e.g., ಂಕ = nka, ಂಚ = nca, ಂಟ = nTa, ಂತ = nta, ಂಪ = mpa

**Symbol count:**
- EK uses **31 symbols** (ellara kannaDa only)
- Full Eke uses **41 symbols** (formal kannaDa including historical)
- Extended Eke uses **44 symbols** (includes English f, w, z)

**Case sensitivity is significant:** Uppercase letters denote retroflex or special consonants (T, D, N, L, S, R, Z, G, Y, X, Q, H).

---

## 1. TRANSLITERATION TERMINOLOGY

| Num | English | Formal Kannada (Eke) | Ellara kannaDa (Eke(ek)) | Notes |
|-----|---------|----------------------|--------------------------|-------|
| — | Letter / character | akShara | barige | sometimes akSara |
| 7 | syllable | prANa | uli | |
| 8 | consonant | vyanjana | taDeyuli | |
| 9 | vowel | svara | tereyuli | |
| 10 | Aspirated Consonant | mahAprANa | ottuli | breathed consonant; e.g. ಖ, ಘ, ಛ |
| 11 | Short/Unaspirated Consonant | alpaprANa | kiriduli | e.g. ಕ, ಗ, ಚ |
| 12 | Consonant cluster | ottakShara | ottakSara | compound character |
| 34 | Eke | Eke | Eke | Eke transliteration scheme, direct |
| 36 | Eke(ek) | Eke(ek) | Eke(ek) | Eke using ellara kannaDa simplifications |
| 26 | Velar | kaNThya | — | ka, ga, nka/nga row |
| 27 | Palatal | tAlavya | — | ca, ja, nca/nja row |
| 28 | Retroflex | mUrdhanya | — | Ta, Da, Na row |
| 29 | Dental | dantya | — | ta, da, na row |
| 30 | Labial | OShThya | — | pa, ba, ma row |
| 31 | Diphthong | sandhyAkShara | — | ay, av combinations |
| 37 | Abugida/Alpha-syllabary | akSara | barige | akSara or barige |
| — | IK | Informal kannaDa | — | ad-hoc internet transliteration |
| — | HK | Harvard Kyoto | — | round-trips through Devanagari |
| — | EK | ellara kannaDa | — | D.N. Shankara Bhat's simplified Kannada |

---

## 2. CONSONANT COMPARISON TABLE

<div style="margin:0 auto;overflow:scroll;width:auto;max-width:100%">

| System | ka | kha | ga | gha | Ga | ca | cha | ja | jha | Ya | Ta | Tha | Da | Dha | Na | ta | tha | da | dha | na | pa | pha | ba | bha | ma | ya | ra | Ra | la | La | Za | va | Sa | Sha | sa | ha | kSa |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kannada | ಕ | ಖ | ಗ | ಘ | ಙ | ಚ | ಛ | ಜ | ಝ | ಞ | ಟ | ಠ | ಡ | ಢ | ಣ | ತ | ಥ | ದ | ಧ | ನ | ಪ | ಫ | ಬ | ಭ | ಮ | ಯ | ರ | ಱ | ಲ | ಳ | ೞ | ವ | ಶ | ಷ | ಸ | ಹ | ಕ್ಷ |
| ellara kannaDa (EK) | ಕ | ಕ | ಗ | ಗ | ಂಕ ಂಗ | ಚ | ಚ | ಜ | ಜ | ಂಚ ಂಜ | ಟ | ಟ | ಡ | ಡ | ಣ | ತ | ತ | ದ | ದ | ನ | ಪ | — | ಬ | — | ಮ | ಯ | ರ | — | ಲ | ಳ | — | ವ | ಶ | — | ಸ | ಹ | — |
| Eke(ek) | ka | ka | ga | ga | nka/nga | ca | ca | ja | ja | nya | Ta | Ta | Da | Da | Na | ta | ta | da | da | na | pa | pa | ba | ba | ma | ya | ra | ra | la | La | La | va | Sa | Sa | sa | ha | kSa |
| Eke | ka | kha | ga | gha | Ga | ca | cha | ja | jha | Ya | Ta | Tha | Da | Dha | Na | ta | tha | da | dha | na | pa | pha | ba | bha | ma | ya | ra | Ra | la | La | Za | va | Sa | Sha | sa | ha | kSa |
| ISO | ka | kha | ga | gha | ṅa | ca | cha | ja | jha | ña | ṭa | ṭha | ḍa | ḍha | ṇa | ta | tha | da | dha | na | pa | pha | ba | bha | ma | ya | ra | ṟa | la | ḷa | ḻa | va | śa | ṣa | sa | ha | kṣa |
| IK | ka | kha | ga | gha | nga | cha | cha | ja | jha | nya | ta | ta | da | da | na | tha | tha | dha | dha | na | pa | pha | ba | bha | ma | ya | ra | ra | la | la | la | va | sha | sha | sa | ha | ksha |
| HK | ka | kha | ga | gha | Ga | ca | cha | ja | jha | Ya | Ta | Tha | Da | Dha | Na | ta | tha | da | dha | na | pa | pha | ba | bha | ma | ya | ra | — | la | La | — | va | za | sha | sa | ha | ksha |

</div>

---

## 3. ELLARA KANNADA CONSONANTS IN EKE (EK ONLY)

|           |        |        |        |     |         |         |
|-----------|--------|--------|--------|-----|---------|---------|
| velar     | ಕ      | ಗ      |        |     | ಂಕ      | ಂಗ      |
|           | **ka** | **ga** |        |     | **nka** | **nga** |
| palatal   | ಚ      | ಜ      |        |     | ಂಚ      | ಂಜ      |
|           | **ca** | **ja** |        |     | **nca** | **nja** |
| retroflex | ಟ      | ಡ      | ಣ      |     | ಂಟ      | ಂಡ      |
|           | **Ta** | **Da** | **Na** |     | **nTa** | **nDa** |
| dental    | ತ      | ದ      | ನ      |     | ಂತ      | ಂದ      |
|           | **ta** | **da** | **na** |     | **nta** | **nda** |
| labial    | ಪ      | ಬ      | ಮ      |     | ಂಪ      | ಂಬ      |
|           | **pa** | **ba** | **ma** |     | **mpa** | **mba** |
|           |        |        |        |     |         |         |
| ಯ         | ರ      | ಲ      | ವ      |     |         |         |
| **ya**    | **ra** | **la** | **va** |     |         |         |
| ಶ         | ಸ      | ಹ      | ಳ      |     |         |         |
| **Sa**    | **sa** | **ha** | **La** |     |         |         |

---

## 4. ADDITIONAL (FORMAL/LEGACY) KANNADA CONSONANTS IN EKE

|           |         |         |        |
|-----------|---------|---------|--------|
| velar     | ಖ       | ಘ       | ಙ      |
|           | **kha** | **gha** | **Ga** |
| palatal   | ಛ       | ಝ       | ಞ      |
|           | **cha** | **jha** | **Ya** |
| retroflex | ಠ       | ಢ       |        |
|           | **Tha** | **Dha** |        |
| dental    | ಥ       | ಧ       |        |
|           | **tha** | **dha** |        |
| labial    | ಫ       | ಭ       |        |
|           | **pha** | **bha** |        |
|           |         |         |        |
| ಱ         | ೞ       | ಷ       |        |
| **Ra**    | **Za**  | **Sha** |        |

---

## 5. VOWELS

<div style="margin:0 auto;overflow:scroll;width:auto;max-width:100%">

| System | a | A | i | I | u | U | e | E | ay | o | O | av | x (ಋ) | H (ಃ) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eke akSaras | a | A | i | I | u | U | e | E | ay | o | O | av | x | H |
| Kannada | ಅ | ಆ | ಇ | ಈ | ಉ | ಊ | ಎ | ಏ | ಐ | ಒ | ಓ | ಔ | ಋ | ಃ |
| EK | ಅ | ಆ | ಇ | ಈ | ಉ | ಊ | ಎ | ಏ | ಅಯ್ | ಒ | ಓ | ಅವ್ | — | — |
| ISO | a | ā | i | ī | u | ū | e | ē | ai | o/ô | ō | au/ô | ṛ | ḥ |
| IK | a | aa | i | ee | u | oo | e | ay | ai | o | o | au | — | — |
| HK | a | A | i | I | u | U | — | e | ai | — | o | au | R | H |

</div>

**Key vowel distinctions in Eke:**
- Short vowels: a, i, u, e, o (lowercase)
- Long vowels: A, I, U, E, O (uppercase)
- Diphthong: ay (ಐ in formal, ಅಯ್ in EK), av (ಔ in formal, ಅವ್ in EK)
- Vocalic R: x (ಋ) — almost exclusively Sanskrit origin
- Visarga: H (ಃ) — rare in EK

---

## 6. EKE SINGLE-LETTER ALPHABET MAPPING

| **Eke** | **akSara** | **ottakSara** | **EK** | **kannaDa** | **Notes** |
|---------|------------|---------------|--------|-------------|-----------|
| **a** | ಅ | ❌ | ✅ | ✅ | short a |
| **A** | ಆ | ❌ | ✅ | ✅ | long A |
| **b** | ಬ್ | ್ಬ | ✅ | ✅ | |
| **c** | ಚ್ | ್ಚ | ✅ | ✅ | |
| **d** | ದ್ | ್ದ | ✅ | ✅ | dental d |
| **D** | ಡ್ | ್ಡ | ✅ | ✅ | retroflex D |
| **e** | ಎ | ❌ | ✅ | ✅ | short e |
| **E** | ಏ | ❌ | ✅ | ✅ | long E |
| **g** | ಗ್ | ್ಗ | ✅ | ✅ | |
| **G** | ಙ್ | ್ಙ | ಂಕ್ ಂಗ್ | ✅ | velar nasal; anusvAra form used in EK |
| **h** | ಹ್ | ್ಹ | ✅ | ✅ | |
| **H** | ಃ | ❌ | ❌ | ✅ | visarga |
| **i** | ಇ | ❌ | ✅ | ✅ | short i |
| **I** | ಈ | ❌ | ✅ | ✅ | long I |
| **j** | ಜ್ | ್ಜ | ✅ | ✅ | |
| **k** | ಕ್ | ್ಕ | ✅ | ✅ | |
| **l** | ಲ್ | ್ಲ | ✅ | ✅ | dental l |
| **L** | ಳ್ | ್ಳ | ✅ | ✅ | retroflex L |
| **m** | ಮ್ | ್ಮ | ✅ | ✅ | anusvAra: ಂಪ/ಂಬ for mpa/mba |
| **n** | ನ್ | ್ನ | ✅ | ✅ | anusvAra: ಂಕ=nka, ಂಚ=nca, ಂಟ=nTa, ಂತ=nta |
| **N** | ಣ್ | ್ಣ | ✅ | ✅ | retroflex N |
| **o** | ಒ | ❌ | ✅ | ✅ | short o |
| **O** | ಓ | ❌ | ✅ | ✅ | long O |
| **p** | ಪ್ | ್ಪ | ✅ | ✅ | |
| **q** | ಌ | ❌ | li/lu | ✅ | vocalic l (rare) |
| **Q** | ೡ | ❌ | ❌ | ✅ | long vocalic l (extremely rare) |
| **r** | ರ್ | ್ರ | ✅ | ✅ | |
| **R** | ಱ್ | ್ಱ | r ರ್ | ✅ | old Kannada r (ಕೆಱೆ = lake) |
| **s** | ಸ್ | ್ಸ | ✅ | ✅ | |
| **S** | ಶ್ | ್ಶ | ✅ | ✅ | palatal sibilant (z in HK) |
| **t** | ತ್ | ್ತ | ✅ | ✅ | dental t |
| **T** | ಟ್ | ್ಟ | ✅ | ✅ | retroflex T |
| **u** | ಉ | ❌ | ✅ | ✅ | short u |
| **U** | ಊ | ❌ | ✅ | ✅ | long U |
| **v** | ವ್ | ್ವ | ✅ | ✅ | |
| **x** | ಋ | ❌ | ri/ru | ✅ | vocalic R; Sanskrit origin |
| **X** | ೠ | ❌ | ❌ | ✅ | long vocalic R (extremely rare) |
| **y** | ಯ್ | ್ಯ | ✅ | ✅ | |
| **Y** | ಞ್ | ್ಞ | gna/nya | ✅ | palatal nasal; anusvAra form used in EK |
| **Z** | ೞ್ | ್ೞ | ಳ್ L | ✅ | old Tamil-Kannada zh (tamiZ) |

**Unused letters in Eke (no Kannada equivalent):** B, f, F, J, K, M, P, V, w, W, z

---

## 7. EKE TWO-LETTER COMBINATIONS (ASPIRATES AND SPECIAL DIGRAPHS)

These two-letter sequences represent specific Kannada consonants. In Eke(ek), the aspirates are reduced to their unaspirated equivalents.

| **Eke** | **akSara** | **ottakSara** | **Eke(ek)** | **kannaDa** | **Notes** |
|---------|------------|---------------|-------------|-------------|-----------|
| **bh** | ಭ್ | ್ಭ | b ಬ್ | ✅ | |
| **ch** | ಛ್ | ್ಛ | c ಚ್ | ✅ | |
| **dh** | ಧ್ | ್ಧ | d ದ್ | ✅ | dental aspirate |
| **Dh** | ಢ್ | ್ಢ | D ಡ್ | ✅ | retroflex aspirate |
| **gh** | ಘ್ | ್ಘ | g ಗ್ | ✅ | |
| **jh** | ಝ್ | ್ಝ | j ಜ್ | ✅ | |
| **kh** | ಖ್ | ್ಖ | k ಕ್ | ✅ | |
| **ph** | ಫ್ | ್ಫ | p ಪ್ | ✅ | |
| **Sh** | ಷ್ | ್ಷ | S ಶ್ | ✅ | retroflex sibilant → palatal in EK |
| **th** | ಥ್ | ್ಥ | t ತ್ | ✅ | dental aspirate |
| **Th** | ಠ್ | ್ಠ | T ಟ್ | ✅ | retroflex aspirate |

---

## 8. DIPHTHONGS

| | | ಅ | ಆ | ಇ | ಈ | ಉ | ಊ | ಎ | ಏ | ಒ | ಓ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ಯ್ | Kannada | ಐ | ಆಯ್ | ಇಯ್ | ಈಯ್ | ಉಯ್ | ಊಯ್ | ಎಯ್ | ಏಯ್ | ಒಯ್ | ಓಯ್ |
| | | ಕೈ | ಕಾಯ್ | ಕಿಯ್ | ಕೀಯ್ | ಕುಯ್ | ಕೂಯ್ | ಕೆಯ್ | ಕೇಯ್ | ಕೊಯ್ | ಕೋಯ್ |
| | EK | ಅಯ್ | ಆಯ್ | ಇಯ್ | ಈಯ್ | ಉಯ್ | ಊಯ್ | ಎಯ್ | ಏಯ್ | ಒಯ್ | ಓಯ್ |
| | Eke | ay | Ay | iy | Iy | uy | Uy | ey | Ey | oy | Oy |
| | | kay | kAy | kiy | kIy | kuy | kUy | key | kEy | koy | kOy |
| ವ್ | Kannada | ಔ | ಆವ್ | ಇವ್ | ಈವ್ | ಉವ್ | ಊವ್ | ಎವ್ | ಏವ್ | ಒವ್ | ಓವ್ |
| | EK | ಅವ್ | ಆವ್ | ಇವ್ | ಈವ್ | ಉವ್ | ಊವ್ | ಎವ್ | ಏವ್ | ಒವ್ | ಓವ್ |
| | Eke | av | Av | iv | Iv | uv | Uv | ev | Ev | ov | Ov |
| | | kav | kAv | kiv | kIv | kuv | kUv | kev | kEv | kov | kOv |

---

## 9. ELLARA KANNADA FULL SYLLABARY (EK akSaragaLu)

Complete consonant+vowel combinations for EK. Read as: ottakSara (consonant-only form) + vowel.

| **Num** | **ottakSara** | **್** | **ಅ** | **ಆ** | **ಇ** | **ಈ** | **ಉ** | **ಊ** | **ಎ** | **ಏ** | **ಒ** | **ಓ** |
|---------|---------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 0 | ❌ | ❌ | **a** | **A** | **i** | **I** | **u** | **U** | **e** | **E** | **o** | **O** |
| 1 | ್ಕ | ಕ್ | ಕ | ಕಾ | ಕಿ | ಕೀ | ಕು | ಕೂ | ಕೆ | ಕೇ | ಕೊ | ಕೋ |
| | k | k | ka | kA | ki | kI | ku | kU | ke | kE | ko | kO |
| 2 | ್ಗ | ಗ್ | ಗ | ಗಾ | ಗಿ | ಗೀ | ಗು | ಗೂ | ಗೆ | ಗೇ | ಗೊ | ಗೋ |
| | g | g | ga | gA | gi | gI | gu | gU | ge | gE | go | gO |
| 3 | ್ಚ | ಚ್ | ಚ | ಚಾ | ಚಿ | ಚೀ | ಚು | ಚೂ | ಚೆ | ಚೇ | ಚೊ | ಚೋ |
| | c | c | ca | cA | ci | cI | cu | cU | ce | cE | co | cO |
| 4 | ್ಜ | ಜ್ | ಜ | ಜಾ | ಜಿ | ಜೀ | ಜು | ಜೂ | ಜೆ | ಜೇ | ಜೊ | ಜೋ |
| | j | j | ja | jA | ji | jI | ju | jU | je | jE | jo | jO |
| 5 | ್ಟ | ಟ್ | ಟ | ಟಾ | ಟಿ | ಟೀ | ಟು | ಟೂ | ಟೆ | ಟೇ | ಟೊ | ಟೋ |
| | T | T | Ta | TA | Ti | TI | Tu | TU | Te | TE | To | TO |
| 6 | ್ಡ | ಡ್ | ಡ | ಡಾ | ಡಿ | ಡೀ | ಡು | ಡೂ | ಡೆ | ಡೇ | ಡೊ | ಡೋ |
| | D | D | Da | DA | Di | DI | Du | DU | De | DE | Do | DO |
| 7 | ್ಣ | ಣ್ | ಣ | ಣಾ | ಣಿ | ಣೀ | ಣು | ಣೂ | ಣೆ | ಣೇ | ಣೊ | ಣೋ |
| | N | N | Na | NA | Ni | NI | Nu | NU | Ne | NE | No | NO |
| 8 | ್ತ | ತ್ | ತ | ತಾ | ತಿ | ತೀ | ತು | ತೂ | ತೆ | ತೇ | ತೊ | ತೋ |
| | t | t | ta | tA | ti | tI | tu | tU | te | tE | to | tO |
| 9 | ್ದ | ದ್ | ದ | ದಾ | ದಿ | ದೀ | ದು | ದೂ | ದೆ | ದೇ | ದೊ | ದೋ |
| | d | d | da | dA | di | dI | du | dU | de | dE | do | dO |
| 10 | ್ನ | ನ್ | ನ | ನಾ | ನಿ | ನೀ | ನು | ನೂ | ನೆ | ನೇ | ನೊ | ನೋ |
| | n | n | na | nA | ni | nI | nu | nU | ne | nE | no | nO |
| 11 | ್ಪ | ಪ್ | ಪ | ಪಾ | ಪಿ | ಪೀ | ಪು | ಪೂ | ಪೆ | ಪೇ | ಪೊ | ಪೋ |
| | p | p | pa | pA | pi | pI | pu | pU | pe | pE | po | pO |
| 12 | ್ಬ | ಬ್ | ಬ | ಬಾ | ಬಿ | ಬೀ | ಬು | ಬೂ | ಬೆ | ಬೇ | ಬೊ | ಬೋ |
| | b | b | ba | bA | bi | bI | bu | bU | be | bE | bo | bO |
| 13 | ್ಮ | ಮ್ | ಮ | ಮಾ | ಮಿ | ಮೀ | ಮು | ಮೂ | ಮೆ | ಮೇ | ಮೊ | ಮೋ |
| | m | m | ma | mA | mi | mI | mu | mU | me | mE | mo | mO |
| 14 | ್ಯ | ಯ್ | ಯ | ಯಾ | ಯಿ | ಯೀ | ಯು | ಯೂ | ಯೆ | ಯೇ | ಯೊ | ಯೋ |
| | y | y | ya | yA | yi | yI | yu | yU | ye | yE | yo | yO |
| 15 | ್ರ | ರ್ | ರ | ರಾ | ರಿ | ರೀ | ರು | ರೂ | ರೆ | ರೇ | ರೊ | ರೋ |
| | r | r | ra | rA | ri | rI | ru | rU | re | rE | ro | rO |
| 16 | ್ಲ | ಲ್ | ಲ | ಲಾ | ಲಿ | ಲೀ | ಲು | ಲೂ | ಲೆ | ಲೇ | ಲೊ | ಲೋ |
| | l | l | la | lA | li | lI | lu | lU | le | lE | lo | lO |
| 17 | ್ವ | ವ್ | ವ | ವಾ | ವಿ | ವೀ | ವು | ವೂ | ವೆ | ವೇ | ವೊ | ವೋ |
| | v | v | va | vA | vi | vI | vu | vU | ve | vE | vo | vO |
| 18 | ್ಶ | ಶ್ | ಶ | ಶಾ | ಶಿ | ಶೀ | ಶು | ಶೂ | ಶೆ | ಶೇ | ಶೊ | ಶೋ |
| | S | S | Sa | SA | Si | SI | Su | SU | Se | SE | So | SO |
| 19 | ್ಸ | ಸ್ | ಸ | ಸಾ | ಸಿ | ಸೀ | ಸು | ಸೂ | ಸೆ | ಸೇ | ಸೊ | ಸೋ |
| | s | s | sa | sA | si | sI | su | sU | se | sE | so | sO |
| 20 | ್ಹ | ಹ್ | ಹ | ಹಾ | ಹಿ | ಹೀ | ಹು | ಹೂ | ಹೆ | ಹೇ | ಹೊ | ಹೋ |
| | h | h | ha | hA | hi | hI | hu | hU | he | hE | ho | hO |
| 21 | ್ಳ | ಳ್ | ಳ | ಳಾ | ಳಿ | ಳೀ | ಳು | ಳೂ | ಳೆ | ಳೇ | ಳೊ | ಳೋ |
| | L | L | La | LA | Li | LI | Lu | LU | Le | LE | Lo | LO |

---

## 10. FORMAL/LEGACY KANNADA SYLLABARY

For formal Kannada and Sanskrit borrowings. These use aspirate digraphs in Eke.

| **Num** | **ottakSara** | **್** | **ಅ** | **ಆ** | **ಇ** | **ಈ** | **ಉ** | **ಊ** | **ಎ** | **ಏ** | **ಒ** | **ಓ** |
|---------|---------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 1 | ್ಖ / ್ಕ್ಹ | ಖ್ | ಖ | ಖಾ | ಖಿ | ಖೀ | ಖು | ಖೂ | ಖೆ | ಖೇ | ಖೊ | ಖೋ |
| | kh | kh | kha | khA | khi | khI | khu | khU | khe | khE | kho | khO |
| 2 | ್ಘ / ್ಗ್ಹ | ಘ್ | ಘ | ಘಾ | ಘಿ | ಘೀ | ಘು | ಘೂ | ಘೆ | ಘೇ | ಘೊ | ಘೋ |
| | gh | gh | gha | ghA | ghi | ghI | ghu | ghU | ghe | ghE | gho | ghO |
| 3 | ್ಛ / ್ಚ್ಹ | ಛ್ | ಛ | ಛಾ | ಛಿ | ಛೀ | ಛು | ಛೂ | ಛೆ | ಛೇ | ಛೊ | ಛೋ |
| | ch | ch | cha | chA | chi | chI | chu | chU | che | chE | cho | chO |
| 4 | ್ಝ / ್ಜ್ಹ | ಝ್ | ಝ | ಝಾ | ಝಿ | ಝೀ | ಝು | ಝೂ | ಝೆ | ಝೇ | ಝೊ | ಝೋ |
| | jh | jh | jha | jhA | jhi | jhI | jhu | jhU | jhe | jhE | jho | jhO |
| 5 | ್ಠ / ್ಟ್ಹ | ಠ್ | ಠ | ಠಾ | ಠಿ | ಠೀ | ಠು | ಠೂ | ಠೆ | ಠೇ | ಠೊ | ಠೋ |
| | Th | Th | Tha | ThA | Thi | ThI | Thu | ThU | The | ThE | Tho | ThO |
| 6 | ್ಢ / ್ಡ್ಹ | ಢ್ | ಢ | ಢಾ | ಢಿ | ಢೀ | ಢು | ಢೂ | ಢೆ | ಢೇ | ಢೊ | ಢೋ |
| | Dh | Dh | Dha | DhA | Dhi | DhI | Dhu | DhU | Dhe | DhE | Dho | DhO |
| 7 | ್ಥ / ್ತ್ಹ | ಥ್ | ಥ | ಥಾ | ಥಿ | ಥೀ | ಥು | ಥೂ | ಥೆ | ಥೇ | ಥೊ | ಥೋ |
| | th | th | tha | thA | thi | thI | thu | thU | the | thE | tho | thO |
| 8 | ್ಧ / ್ದ್ಹ | ಧ್ | ಧ | ಧಾ | ಧಿ | ಧೀ | ಧು | ಧೂ | ಧೆ | ಧೇ | ಧೊ | ಧೋ |
| | dh | dh | dha | dhA | dhi | dhI | dhu | dhU | dhe | dhE | dho | dhO |
| 9 | ್ಫ / ್ಪ್ಹ | ಫ್ | ಫ | ಫಾ | ಫಿ | ಫೀ | ಫು | ಫೂ | ಫೆ | ಫೇ | ಫೊ | ಫೋ |
| | ph | ph | pha | phA | phi | phI | phu | phU | phe | phE | pho | phO |
| 10 | ್ಭ / ್ಬ್ಹ | ಭ್ | ಭ | ಭಾ | ಭಿ | ಭೀ | ಭು | ಭೂ | ಭೆ | ಭೇ | ಭೊ | ಭೋ |
| | bh | bh | bha | bhA | bhi | bhI | bhu | bhU | bhe | bhE | bho | bhO |
| 11 | ್ಱ | ಱ್ | ಱ | ಱಾ | ಱಿ | ಱೀ | ಱು | ಱೂ | ಱೆ | ಱೇ | ಱೊ | ಱೋ |
| | R | R | Ra | RA | Ri | RI | Ru | RU | Re | RE | Ro | RO |
| 12 | ್ಷ | ಷ್ | ಷ | ಷಾ | ಷಿ | ಷೀ | ಷು | ಷೂ | ಷೆ | ಷೇ | ಷೊ | ಷೋ |
| | Sh | Sh | Sha | ShA | Shi | ShI | Shu | ShU | She | ShE | Sho | ShO |
| 13 | ್ೞ | ೞ್ | ೞ | ೞಾ | ೞಿ | ೞೀ | ೞು | ೞೂ | ೞೆ | ೞೇ | ೞೊ | ೞೋ |
| | Z | Z | Za | ZA | Zi | ZI | Zu | ZU | Ze | ZE | Zo | ZO |

---

## 11. CHARACTER FREQUENCY (EKE CONSONANTS)

Frequency data from the Alar Kannada dictionary. Ottulis (aspirates) are merged into their kiridulis (unaspirated equivalents) for EK. Consonants marked **bold** are EK consonants.

| **Eke** | **akSara** | **count** | **ottakSara** | **count** | **Total** | **% of consonants** |
|---------|------------|-----------|---------------|-----------|-----------|---------------------|
| **r** | ರ್ | 45816 | ್ರ | 9601 | 61978 | **11.35%** |
| **t** | ತ್ | 31452 | ್ತ | 7456 | 42014 | **7.69%** |
| **k** | ಕ್ | 34581 | ್ಕ | 4240 | 41400 | **7.58%** |
| **n** | ನ್ | 23180 | ್ನ | 2232 | 40135 | **7.35%** |
| **g** | ಗ್ | 31622 | ್ಗ | 2090 | 35019 | **6.41%** |
| **m** | ಮ್ | 21340 | ್ಮ | 3470 | 32330 | **5.92%** |
| **v** | ವ್ | 26609 | ್ವ | 4340 | 30949 | **5.67%** |
| **d** | ದ್ | 19706 | ್ದ | 1573 | 27537 | **5.04%** |
| **s** | ಸ್ | 26340 | ್ಸ | 768 | 27108 | **4.96%** |
| **p** | ಪ್ | 19475 | ್ಪ | 2699 | 23211 | **4.25%** |
| **l** | ಲ್ | 20297 | ್ಲ | 2497 | 22794 | **4.17%** |
| **y** | ಯ್ | 15766 | ್ಯ | 5735 | 21722 | **3.98%** |
| **b** | ಬ್ | 13899 | ್ಬ | 1380 | 20267 | **3.71%** |
| **D** | ಡ್ | 17442 | ್ಡ | 1144 | 19013 | **3.48%** |
| **L** | ಳ್ | 15243 | ್ಳ | 1421 | 18125 | **3.32%** |
| **T** | ಟ್ | 10299 | ್ಟ | 4815 | 16472 | **3.02%** |
| **S** | ಶ್ | 6841 | ್ಶ | 268 | 16069 | **2.94%** |
| **c** | ಚ್ | 10129 | ್ಚ | 2025 | 13333 | **2.44%** |
| **N** | ಣ್ | 11156 | ್ಣ | 1943 | 13099 | **2.40%** |
| **h** | ಹ್ | 12472 | ್ಹ | 108 | 12580 | **2.30%** |
| **j** | ಜ್ | 9638 | ್ಜ | 1042 | 10984 | **2.01%** |

22243 anusvAras distribute into m or n based on the following consonant context.

---

## 12. CHARACTER FREQUENCY (EKE VOWELS)

| **Eke** | **svara** | **count** | **kombu/modifier** | **count** | **Total** | **% of vowels** |
|---------|-----------|-----------|---------------------|-----------|-----------|-----------------|
| **a** | ಅ | 8963 | ø (inherent a) | 237387 | 246350 | **46.56%** |
| **ø** | | | ್ (virama) | 59932 | 59932 | **11.33%** |
| **i** | ಇ | 1879 | ಿ | 54773 | 56652 | **10.71%** |
| **u** | ಉ | 3644 | ು | 45920 | 49564 | **9.37%** |
| **A** | ಆ | 3551 | ಾ | 36978 | 40529 | **7.66%** |
| **e** | ಎ | 1830 | ೆ | 32298 | 34128 | **6.45%** |
| **o** | ಒ | 1819 | ೊ | 9426 | 11245 | **2.13%** |
| **O** | ಓ | 422 | ೋ | 8686 | 9108 | **1.72%** |
| **E** | ಏ | 675 | ೇ | 7549 | 8224 | **1.55%** |
| **I** | ಈ | 305 | ೀ | 7035 | 7340 | **1.39%** |
| **U** | ಊ | 379 | ೂ | 5706 | 6085 | **1.15%** |

Additional: ay (ಐ) = 3083 total; av (ಔ) = 1456 total; x (ಋ) = 2473 total.

---

## 13. TOP 100 OTTAKSARAS (CONSONANT CLUSTERS)

These 100 clusters account for ~91% of all ottakSaras in Kannada (94% in EK). OttakSaras form ~6% of total characters (12% of consonants). Doubled consonants (e.g., TT, tt, kk) are predominantly native Kannada origin.

| Num | Kannada | count | Eke | Eke(ek) | EK count | Origin |
|-----|---------|-------|-----|---------|----------|--------|
| 1 | ಟ್ಟ | 3756 | TT | TT | 3776 | kannaDa |
| 2 | ತ್ತ | 3450 | tt | tt | 3505 | kannaDa |
| 3 | ಕ್ಕ | 2708 | kk | kk | 2762 | kannaDa |
| 4 | ಪ್ರ | 2617 | pr | pr | 2618 | samskxta |
| 5 | ತ್ರ | 2507 | tr | tr | 2514 | samskxta |
| 6 | ಕ್ಷ | 2302 | kSh | **kS** | 2306 | samskxta |
| 7 | ಸ್ತ | 1493 | st | st | 2164 | samskxta |
| 8 | ಲ್ಲ | 1923 | ll | ll | 1923 | kannaDa |
| 9 | ಚ್ಚ | 1477 | cc | cc | 1850 | kannaDa |
| 10 | ನ್ನ | 1462 | nn | nn | 1462 | kannaDa |
| 11 | ದ್ದ | 724 | dd | dd | 1739 | kannaDa |
| 12 | ಳ್ಳ | 1414 | LL | LL | 1414 | kannaDa |
| 13 | ಪ್ಪ | 1375 | pp | pp | 1375 | kannaDa |
| 14 | ಷ್ಟ | 1015 | ShT | **ST** | 1412 | samskxta |
| 15 | ರ್ತ | 854 | rt | rt | 1423 | samskxta |
| 16 | ದ್ರ | 1211 | dr | dr | 1211 | samskxta |
| 17 | ಣ್ಣ | 1169 | NN | NN | 1169 | kannaDa |
| 18 | ಡ್ಡ | 1132 | DD | DD | 1132 | samskxta |
| 19 | ರ್ವ | 1063 | rv | rv | 1063 | samskxta |
| 20 | ಮ್ಮ | 1041 | mm | mm | 1041 | kannaDa |
| 21 | ಬ್ಬ | 953 | bb | bb | 953 | kannaDa |
| 22 | ಕ್ರ | 933 | kr | kr | 933 | samskxta |
| 23 | ದ್ಯ | 627 | dy | dy | 1024 | samskxta |
| 24 | ಕ್ತ | 867 | kt | kt | 867 | samskxta |
| 25 | ರ್ಮ | 799 | rm | rm | 799 | samskxta |
| 26 | ವ್ಯ | 796 | vy | vy | 796 | samskxta |
| 27 | ತ್ವ | 743 | tv | tv | 743 | samskxta |
| 28 | ಗ್ರ | 721 | gr | gr | 721 | samskxta |
| 29 | ಗ್ಗ | 711 | gg | gg | 711 | kannaDa |
| 30 | ರ್ದ | 472 | rd | rd | 798 | samskxta |
| 31 | ತ್ಯ | 674 | ty | ty | 674 | samskxta |
| 32 | ಜ್ಜ | 669 | jj | jj | 669 | kannaDa |
| 33 | ಜ್ಞ | 634 | jY | gy | 634 | samskxta |
| 34 | ದ್ವ | 427 | dv | dv | 641 | kannaDa |
| 35 | ರ್ಯ | 627 | ry | ry | 627 | samskxta |
| 36 | ರ್ಗ | 618 | rg | rg | 618 | samskxta |
| 37 | ರ್ಣ | 577 | rN | rN | 577 | samskxta/kannaDa |
| 38 | ಶ್ರ | 569 | Sr | **Sr** | 569 | samskxta |
| 39 | ಸ್ವ | 546 | sv | sv | 546 | samskxta |
| 40 | ನ್ಯ | 519 | ny | ny | 519 | samskxta |
| 41 | ಭ್ರ | 284 | bhr | **br** | 587 | samskxta |
| 42 | ರ್ಬ | 263 | rb | rb | 485 | samskxta |
| 43 | ರ್ಕ | 429 | rk | rk | 429 | samskxta |
| 44 | ರ್ಷ | 222 | rSh | **rS** | 555 | samskxta |
| 45 | ಪ್ತ | 397 | pt | pt | 397 | samskxta |
| 46 | ಶ್ವ | 385 | Sv | Sv | 385 | samskxta |
| 47 | ರ್ಪ | 378 | rp | rp | 378 | samskxta |
| 48 | ಷ್ಠ | 345 | ShTh | **ST** | 345 | samskxta |
| 49 | ತ್ಮ | 333 | tm | tm | 333 | samskxta |
| 50 | ರ್ಜ | 326 | rj | rj | 326 | samskxta |

---

## 14. TRANSLITERATION RULES SUMMARY

### Rule 1: Aspirates (ottulis) in Eke(ek)
Drop the `h` in aspirate digraphs when using EK mode:
- kh → k, gh → g, ch → c, jh → j
- Th → T, Dh → D, th → t, dh → d
- ph → p, bh → b, Sh → S

### Rule 2: Old Kannada letters in Eke(ek)
- ಱ (Ra) → ರ (ra): old r merges with modern r
- ೞ (Za) → ಳ (La): old zh merges with retroflex L

### Rule 3: Nasal assimilation
In EK, nasal consonants before plosives use anusvAra (ಂ) with the following plosive:
- ಂಕ = nka, ಂಗ = nga (velar nasal)
- ಂಚ = nca, ಂಜ = nja (palatal nasal)
- ಂಟ = nTa, ಂಡ = nDa (retroflex nasal)
- ಂತ = nta, ಂದ = nda (dental nasal)
- ಂಪ = mpa, ಂಬ = mba (labial nasal)

### Rule 3b: anusvAra before unordered consonants

Before **unordered consonants** (sonorants and sibilants that fall outside the five ordered plosive rows), the anusvAra (ಂ) is rendered as **m** or **n** by phonological approximation:

| Consonant after anusvAra | Kannada | Eke prefix | Eke(ek) prefix | Example |
|---|---|---|---|---|
| y (ಯ) | ಯ | m | m | ಂಯ = mya |
| r (ರ) | ರ | n | n | ಂರ = nra |
| l (ಲ) | ಲ | m | m | ಂಲ = mla |
| v (ವ) | ವ | n | n | ಂವ = nva |
| S (ಶ) | ಶ | m | m | ಂಶ = mSa |
| s (ಸ) | ಸ | m | m | ಂಸ = msa |
| h (ಹ) | ಹ | m | m | ಂಹ = mha |
| L (ಳ) | ಳ | m | m | ಂಳ = mLa |
| R (ಱ) | ಱ | n | n (→ r in EK) | ಂಱ = nRa |
| Z (ೞ) | ೞ | n | n (→ L in EK) | ಂೞ = nZa |

**Summary:** prefix sequence for `y r l v S s h L R Z` is `m n m n m m m m n n`:

| y | r | l | v | S | s | h | L | R | Z |
|---|---|---|---|---|---|---|---|---|---|
| m | n | m | n | m | m | m | m | n | n |

- **m** before labial-adjacent/sonorant consonants: y, l, S, s, h, L
- **n** before rhotic/glide consonants: r, v, R, Z
- This is a phonological approximation; in natural speech these clusters are rare and the nasal tends to assimilate to the most natural place of articulation.
- In Eke(ek), the same prefixes apply; legacy forms R and Z further reduce to r and L respectively.

### Rule 4: Case sensitivity
- Uppercase = retroflex or special: T, D, N, L (retroflex); S (palatal sibilant ಶ); R (old ಱ); Z (old ೞ); G (velar nasal ಙ); Y (palatal nasal ಞ); H (visarga ಃ); A, I, U, E, O (long vowels); X (vocalic R ಋ)
- Lowercase = dental/standard forms: t, d, n, l, s, r, g, y, h, a, i, u, e, o, x (vocalic R)

### Rule 5: The inherent vowel
Every consonant has an inherent `a` vowel unless followed by:
- Another vowel marker (ಾ, ಿ, ೀ, ು, ೂ, ೆ, ೇ, ೊ, ೋ, ೈ, ೌ)
- Virama ್ (halant) — suppresses the inherent vowel in ottakSaras

### Rule 6: Distinguishing Eke from Eke(ek)
When the aspirate `h` is optional (can be dropped in EK), it is shown in parentheses: `kaS(h)TagaLa`, `vid(h)i`.

---

## 15. TRANSLITERATION EXAMPLES

### gurinuDi (Kannada motto)

    ಸಿರಿಗನ್ನಡಂ ಗೆಲ್ಗೆ, ಸಿರಿಗನ್ನಡಂ ಬಾಳ್ಗೆ.
    sirigannaDam gelge, sirigannaDam bALge.

### A pangram (all EK letters)

**Kannada:**

    ಕಾವಲುಗಾರನು ಓರ್ವನು ಇಳಿವೇಳೆ ಆ ದಿನ
    ಒಂದು ಉರಿಯ ಬಾಣವನ್ನು ಈ ಶಿಲೆಗೆ ಹೊಡೆದು
    ಏರಿ ಅಂದೇ ಊರಿನ ಮೇಳದಲ್ಲಿ ಎಡವಿ
    ಚಟಪಟನೆ ಜನರಿಗೆ ತಪ್ಪು ಹಾಡು ಹಾಡಿದ.

**Eke(ek):**

    kAvalugAranu Orvanu iLivELe A dina
    ondu uriya bANavannu I Silege hoDedu
    Eri andE Urina mELadalli eDavi
    caTapaTane janarige tappu haDu haDida.

### mankutimmana kagga (D.V. Gundappa)

**Kannada:**

    ಹುಲ್ಲಾಗು ಬೆಟ್ಟದಡಿ, ಮನೆಗೆ ಮಲ್ಲಿಗೆಯಾಗು
    ಕಲ್ಲಾಗು ಕಷ್ಟಗಳ ಮಳೆಯ ವಿಧಿ ಸುರಿಯೆ
    ಬೆಲ್ಲ ಸಕ್ಕರೆಯಾಗು ದೀನ ದುರ್ಬಲರಿಂಗೆ
    ಎಲ್ಲರೊಳಗೊಂದಾಗು ಮಂಕುತಿಮ್ಮ

**Eke(ek):**

    hullAgu beTTadaDi, manege malligeyAgu
    kallAgu kaS(h)TagaLa maLeya vid(h)i suriye
    bella sakkareyAgu dIna durbalaringe
    ellaroLagondAgu mankutimma

### uLLavaru (Basavanna vachana)

**Kannada:**

    ಉಳ್ಳವರು ಶಿವಾಲಯ ಮಾಡಿಹರು | ನಾನೇನ ಮಾಡಲಿ ಬಡವನಯ್ಯಾ ||
    ಎನ್ನ ಕಾಲೇ ಕಂಬ ದೇಹವೇ ದೇಗುಲ | ಶಿರ ಹೊನ್ನ ಕಳಶವಯ್ಯಾ ||

**Eke(ek):**

    uLLavaru SivAlaya mADiharu | nAnEna mADali baDavanayyA ||
    enna kAlE kamba dEhavE dEgula | Sira honna kaLaSavayyA ||

### jana gaNa mana (national anthem — first line)

**Kannada script:**

    ಜನ ಗಣ ಮನ ಅಧಿನಾಯಕ ಜಯ ಹೇ
    ಭಾರತ ಭಾಗ್ಯ ವಿಧಾತಾ

**Eke:**

    jana gaNa mana ad(h)inAyaka jaya hE
    b(h)Arata b(h)Agya vid(h)AtA
