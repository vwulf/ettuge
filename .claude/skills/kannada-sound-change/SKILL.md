---
name: kannada-sound-change
description: >
  Answers questions about sound change in Kannada and in languages generally,
  drawing on D. N. Shankara Bhat's framework. Covers: what sound change is and
  why it happens, regularity and the Neogrammarian hypothesis, assimilation and
  dissimilation, comparative reconstruction, internal reconstruction, and how
  Bhat applied sound change theory specifically to Kannada (mahaprana argument
  in Book 08, vowel-raising in coastal dialects, arka-ottu and Kannada phonological
  history). Primary sources: Book 08 (applied), Book 26 (Kannada popularisation,
  2024), Book 22 (English textbook — not yet extracted). Trigger phrases:
  "sound change", "ಉಲಿ ಮಾರ್ಪಾಡು", "why do languages change pronunciation",
  "Neogrammarian", "assimilation dissimilation", "vowel raising Kannada",
  "comparative reconstruction Dravidian", "sound laws", "ಉಲಿ ಮಾರ್ಪಾಡಿನ ಗೆರೆಗಳು".
---

# Kannada Sound Change

You answer questions about sound change in Kannada and languages generally,
using D. N. Shankara Bhat's framework.

---

## Source Material — Readiness Status

| Book | Title | Status | Use for |
|------|-------|--------|---------|
| **Book 08** | *ಕನ್ನಡಕ್ಕೆ ಮಹಾಪ್ರಾಣ ಯಾಕೆ ಬೇಡ?* | ✅ Full text available | Applied phonology: why mahaprana is unnecessary |
| **Book 26** | *ಉಲಿ ಮಾರ್ಪಾಡಿನ ಗೆರೆಗಳು* (2024) | ⚠️ YouTube transcript only | Kannada-language popularisation of sound change theory |
| **Book 22** | *Sound Change* (English textbook) | ❌ Not yet extracted | Theoretical backbone — not yet available in repo |

Book 22 is the comprehensive English academic treatment (2001, Motilal Banarsidass,
167pp). It is the theoretical source Bhat draws on in Books 08 and 26. Until it is
extracted, answers on pure theory must use Books 08 and 26 only.

---

## Core Concepts (from Books 08, 26, and general linguistic knowledge)

### What Is Sound Change?

Sound change (ಉಲಿ ಮಾರ್ಪಾಡು) is the systematic, regular change in the phonological
(sound) system of a language over time. Key principles:

**Regularity (Neogrammarian hypothesis):** Sound changes apply to *all* words
containing the relevant sound in the relevant environment — without exception.
If a sound change has exceptions, there is a reason (analogy, borrowing, a more
specific conditioning environment).

**Conditioning environments:** Most changes are not random — they occur *in a
specific context*:
- Before/after a particular vowel or consonant
- At word boundaries or word-internally
- In stressed/unstressed syllables

### Types of Sound Change

| Type | What happens | Kannada example |
|------|-------------|----------------|
| **Assimilation** | A sound becomes more like a neighbouring sound | ಂ (anusvara) assimilates to following consonant: *kamba*, *kanka*, *tunDu* |
| **Dissimilation** | A sound becomes less like a neighbouring sound | — |
| **Vowel raising** | A mid vowel rises to high vowel | 8th-century Kannada: *e > i*, *o > u* (absent in coastal dialects) |
| **Lenition** | A consonant weakens intervocalically | Old Kannada *p > h* word-initially (ಪಾಲ್ > ಹಾಲು) |
| **Merger** | Two phonemes become one | Sanskrit ಭ and ಬ are not distinguished in native Kannada speech |
| **Deletion** | A sound disappears | Old Kannada word-final consonant clusters simplify |

### Comparative Reconstruction

When we compare cognate words across related languages (e.g., Kannada and Tamil),
regular sound correspondences reveal the *proto-language* form and the history of
changes in each language:

- Kannada *hālu* : Tamil *pāl* → Proto-Dravidian `*pāl` (Kannada underwent *p > h*)
- Kannada *hogi* : Tamil *poku* → Proto-Dravidian `*poku` (same change)

### Internal Reconstruction

Even without comparing related languages, we can sometimes infer earlier forms
from internal alternations within a single language. The Kannada OCR artefact
"arka-ottu reversal" is essentially a synchronic reflection of an older historical
ordering of the `/r/` + consonant cluster.

---

## Applied Sound Change: Mahaprana in Kannada (Book 08)

The mahaprana argument in Book 08 is essentially an application of sound change theory:

1. **The claim:** ಭ, ಧ, ಥ, ಖ, ಘ, ಛ, ಝ, ಠ, ಢ, ಫ are aspirated phonemes in Sanskrit.
   When Sanskrit words were borrowed into Kannada, the aspiration was not phonemically
   contrastive in Kannada — there was no minimal pair where aspiration distinguished
   meaning.

2. **The evidence:** Kannada speakers systematically *de-aspirate* Sanskrit loanwords
   in speech: ಭಾರತ is pronounced *bArata* not *bhArata*. This is a sound merger —
   the Sanskrit phonemic distinction collapsed in Kannada.

3. **The orthographic implication:** If the merger has already occurred phonologically,
   retaining the Sanskrit letters in writing is orthographic debt, not phonological
   necessity.

---

## Applied Sound Change: Vowel-Raising in Kannada

The 8th-century Kannada vowel-raising (*e > i*, *o > u* in certain environments)
is a textbook example of a conditioned sound change:

- **Scope:** Applied to non-coastal dialects; the coastal dialect cluster (Havyaka,
  Halakki, etc.) was geographically isolated before the change occurred
- **Evidence:** Coastal Kannada *beli* vs. standard Kannada *bili* (white);
  *kemi* vs. *kivi* (ear) — regular alternation across a large vocabulary set
- **Reconstruction:** The older forms (*beli*, *kemi*) are reconstructed as the
  Pre-8th-century Kannada forms (proto-non-coastal forms)

---

## The Arka-Ottu Historical Background

The arka-ottu (ರ್ consonant in Old Kannada) appears in a specific ordering in the
original script: as a raised half-form written *above* the following consonant.
In Nudi/legacy fonts this ordering was reversed during OCR. The OCR artefact
(consonant+್ರ instead of ರ್+consonant) is an encoding issue — but understanding
*why* Old Kannada wrote it this way requires knowing the historical phonology of
the pre-voiced retroflex rhotic in Dravidian.

---

## When to Fetch Source Content

For Book 08 applied phonology:
- Chapter 2 (orthographic depth, Sanskrit sounds in Kannada):
  `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/08-kannaDakke-mahAprANa-yAke-bEDa/book/kn/ch2`

For Book 26 (Kannada popularisation of sound change theory):
- YouTube transcript: the repo has a short transcript at
  `src/main/md/kannada/dnsbhat/26-uli-mArpADina-geregaLu/youtube/kn/full.md`
  (67 lines — limited content)

For Book 22 (English textbook): ❌ Not yet extracted. If the user needs the full
theoretical treatment, note that the book is *Sound Change* (2001, Motilal
Banarsidass, MLBD Series in Linguistics, Vol. 14, 167pp) and suggest they access
it directly.

---

## Answering Guidelines

1. **Acknowledge gaps:** Book 22 is not yet in the repo. For deep theoretical
   questions about sound change methodology, note this limitation.
2. **Applied > theoretical for now:** Use Book 08's applied phonology as the
   primary source; draw on general linguistics for theoretical frameworks.
3. **Connect to other skills:** The mahaprana argument leads to `kannada-script-reform`;
   the vowel-raising leads to `havyaka-kannada`; the arka-ottu leads to
   `kannada-ocr-cleaner`.
4. **Comparative Dravidian:** For Proto-Dravidian reconstruction questions,
   Bhat's comparative work is foundational — but note the primary references are
   not yet fully extracted in this repo.
