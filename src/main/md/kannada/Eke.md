# Eke (ಏಕೆ) - A proposal for transcribing Kannada

This proposal attempts to address the slight divergence in informal
writing for kannada (kannaDa) that is already in use in various channels
on the internet. It is a slight variation of the Harvard Kyoto
protocol(HK) adapted to kannaDa.

For lack of a better term, there's already an informal scheme in use to
transcribe kannaDa. Let's call it IK (informal kannaDa). Eke walks a
line between IK and HK.

The default sans serif fonts on wikitext may cause ambiguity between
**l** (small el) and **I**(capital Ay). There are quite a few other
fonts that avoid this ambiguity.

## akSaras (abugidAs) vs alphabets

Brahmic scripts dating back to the oldest archealogical sources are used
as aksharas (akSaras in EK terminology akSharas in formal kannaDa) or
abugidas as linguists often refer to them.

Kharoshti has been linked to Phoenician origin but the links between
Brahmi to Phoenician are disputed by certain scholars.

IAST and other alphabets have been used to represent brahmic scripts.
Other than HK, most other use diacritics quite heavily - mostly for

## ellara kannaDa

"Ellara Kannada" (ellara kannaDa / EK) is a proposal aimed at reducing
the gap between spoken and written Kannada language. This was proposed
by the eminent linguist and padmaSri award winner D.N.Shankara Bhat
(D.N.Sankara BhaT). Some features of EK include eschewing the use of
mahaprANas (ottuli or breathed consonants) and emphasize usage and
construction of native kannaDa words. It uses the orthography of ಹೊಸಬರಹ
instead of ಕನ್ನಡ.

## Use in computation

Diacritics makes it harder to type and use on regular english keyboards
although unicode has made it increasingly easier to render text. Word
processors, Spreadsheets are more usable wrt unicode than programming
focused environments. Non-english scripts are also less prevalent in
programming languages and scripting tools. Lack of full unicode support
in programming editors, command lines make them harder to use. See [^1]
for details.

## ಹೊಸಬರಹ

The gist of ಹೊಸಬರಹ is to address the disconnect in how common people
speak and (mostly can’t) read/write Kannada. Note that EK's a holistic
approach to using native kannaDa words, inventing new words using
kannaDa native constructs, using a native kannaDa grammar which does not
rely on external techniques like Sanskrit along with the orthography of
ಹೊಸಬರಹ. We use EK interchangably with ಹೊಸಬರಹ in the remaining portion of
the article.

For otthaksharas, 35x35 consonant symbols are reduced to 21x21 symbols.
These would be combined with the following 10 vowels and 3 modifiers
instead of 16 vowels and 5 modifiers.

Complexity reduction is from 35x35x21 ≈ 25725 to 21x21x13 ≈ 5733
symbols. Its about a 77% reduction in symbols, greatly simplifying
reading/writing without any loss of fidelity for pronunciation in
Kannada (but not classical or Vedic Sanskrit).

Aspiration (mahapraana) from phonology perspective is the same as ಹ
otthu.

So ಕ ಖ ಗ ಘ = ಕ ಕ್ಹ ಗ ಗ್ಹ

Since aspiration is not used in common speech in Kannada (unlike Hindi
and Sanskrit), ಕ ಗ would suffice.

Simplifications like those drop 25 “ordered”consonants into 13 ಕಗ ಚಜ ಟಡಣ
ತದನ ಪಬಮ This would eliminate the following ಖಘಙ ಛಝಞ ಠಢ ಥಧ ಫಭ

ಙ ಞ ಣ ನ ಮ with nasalization/non standalone are represented by anusvara
ಂ. The first 2 don’t occur in standalone form in Kannada. So ಮಂಗ, ಗಂಜಿ,
ಗಂಟೆ, ತಂದೆ, ಪಂಪ are the five variants.

“unordered” would simplify to ಯರಲವಶಸಹಳ Eliminating ಱೞಷ which are not
used.

Coming to vowels ಅಆಇಈಉಊಎಏಒಓ are retained.

ಋೠಌೡಐಔಅಃ are not. See
<https://www.bolochant.com/blog/sanskrit-pronunciation> for correct
pronunciation of these in Sanskrit. It’s not important/relevant in
Kannada.

ಐಔ (diphthongs) need special mention. In Sanskrit only ai, ou occurs
frequently, hence the special symbols. In Kannada ಆಯ್, ಎಯ್, ಏಯ್, ಓಯ್ etc are
common. It’s more uniform to use ಅಯ್ than ಐ, ಅವ್ than ಔ.

It's similar to why Sanskrit has क्षत्रज्ञ are special characters but
unnecessary as symbols in Kannada and formed by ಕ್ಷತ್ರಜ್ಞ. In hosabaraha,
ಕ್ಶ, ತ್ರ, ಗ್ನ್ಯ or ಜ್ನ್ಯ or ಗ್ಯ (depending on pronunciation).

Modifiers ್ಂ are retained. ಃ ೱ are not. ಼ is debatable. It’s useful for
indicating foreign languages like English, Hindi and Sanskrit- like fa,
za, bank, odd etc.

## Terminology

|         |                     |              |                    |                    |                          |                  |                                               |
|---------|---------------------|--------------|--------------------|--------------------|--------------------------|------------------|-----------------------------------------------|
| **Num** | **English**         | **samskxta** | **Formal Kannada** | \*\* Eke(Kan) \*\* | \*\* ellara kannaDa \*\* | \*\* Eke(ek)\*\* | Notes                                         |
| 0       | Letter              |              |                    | akShara            |                          | barige           | could mean writing, sometimes akSara is used. |
| 1       | Word                |              |                    | pada               |                          | pada             |                                               |
| 2       | Sentence            |              |                    | vAkya              |                          | sollu            | Like "saying"                                 |
| 3       | Science / Method    |              |                    | SAstra             |                          | arime            | ari means to know in kannaDa                  |
| 4       | Verb                |              |                    | kriyApada          |                          | esakapada        | action word - like throwing                   |
| 5       | Noun                |              |                    | nAmapada           |                          | hesarupada       |                                               |
| 6       | Adjective           |              |                    |                    |                          | paricepada       |                                               |
| 7       | syllable            |              |                    | prANa              |                          | uli              |                                               |
| 8       | consonant           |              |                    | vyanjana           |                          | taDeyuli         |                                               |
| 9       | vowel               |              |                    | svara              |                          | tereyuli         |                                               |
| 10      | Aspirated Consonant |              |                    | mahAprANa          |                          | ottuli           |                                               |
| 11      | Short Consonant     |              |                    | alpaprANa          |                          | kiriduli         |                                               |
| 12      | Consonant cluster   |              |                    | ottakShara         |                          | ottakSara        |                                               |
| 13      | Language            |              |                    | bhAShe             |                          | nuDi             |                                               |
| 14      | Grammar             |              |                    | vyAkaraNa          |                          | sollarime        |                                               |
| 15      | Structure           |              |                    | rachane            |                          | iTTaLa           |                                               |
| 16      | Case                |              |                    | vibhakti           |                          |                  |                                               |
| 17      | Technical term      |              |                    | pAriBhAShika pada  |                          | arimeya pada     |                                               |
| 18      | Negation            |              |                    | niShedhArthaka     |                          | allageLeta       |                                               |
| 19      | Event               |              |                    |                    |                          | Aguha            |                                               |
| 20      | Causer              |              |                    |                    |                          | Agisuga          |                                               |
| 21      | Patient, Theme      |              |                    |                    |                          | Aguga            |                                               |
| 22      | Quantity            |              |                    | praMaNa            |                          | aLavi            |                                               |
| 23      | First Person        |              |                    | uttama puruSha     |                          | ADuga            |                                               |
| 24      | Mood                |              |                    |                    |                          | ADugana niluvu   |                                               |
| 25      | Personal Pronoun    |              |                    |                    |                          | ADupada          |                                               |
| 26      | Velar               |              |                    |                    |                          |                  |                                               |
| 27      | palatal             |              |                    |                    |                          |                  |                                               |
| 28      | retroflex           |              |                    |                    |                          |                  |                                               |
| 29      | dental              |              |                    |                    |                          |                  |                                               |
| 30      | labial              |              |                    |                    |                          |                  |                                               |
| 31      | diphtongs           |              |                    |                    |                          |                  |                                               |
| 32      | ISO                 |              |                    |                    |                          |                  |                                               |
| 33      | IPA                 |              |                    |                    |                          |                  |                                               |
| 34      | Eke                 |              |                    |                    |                          |                  |                                               |
| 35      | ellara kannada      |              |                    |                    |                          |                  |                                               |
| 36      | Eke (ek)            |              |                    |                    |                          |                  |                                               |
| 37      | abugida             |              |                    |                    |                          |                  |                                               |
| 38      | syllabary           |              |                    |                    |                          |                  |                                               |
| 39      | alphasyllabary      |              |                    |                    |                          |                  |                                               |
| 40      | PIE                 |              |                    |                    |                          |                  |                                               |
| 41      | Dravidian           |              |                    |                    |                          |                  |                                               |
| 42      | Proto Dravidian     |              |                    |                    |                          |                  |                                               |
| 43      | Indo Aryan          |              |                    |                    |                          |                  |                                               |
| 44      | Brahmi              |              |                    |                    |                          |                  |                                               |
| 45      | Asokan Brahmi       |              |                    |                    |                          |                  |                                               |
| 46      | Tamil Brahmi        |              |                    |                    |                          |                  |                                               |
| 47      |                     |              |                    |                    |                          |                  | Case 1                                        |
| 48      |                     |              |                    |                    |                          |                  | Case 2                                        |
| 49      |                     |              |                    |                    |                          |                  | Case 3                                        |
| 50      |                     |              |                    |                    |                          |                  | Case 4                                        |
| 51      |                     |              |                    |                    |                          |                  | Case 5                                        |
| 52      |                     |              |                    |                    |                          |                  | Case 6                                        |
| 53      |                     |              |                    |                    |                          |                  | Case 7                                        |
| 54      |                     |              |                    |                    |                          |                  | Case 1a                                       |

## Background phonics, linguistics

## Differences between kannaDa and samskxta

## Cultural perspective

This is mostly cultural commentary that can be open ended. Languages are
a contentious topic in India - like elsewhere.

The diversity of languages, history of various invasions, colonization,
the partition of India, linguistic organization of states, urbanization
and recent trend towards assertion of the Indian way of thinking (and
along with supremacist tendencies of language and religion) has created
a potpourri of opinions.

The commonly held viewpoint on languages often differs completely from
the academic consensus. On the flip side, there are traditions in
linguistic understanding that are more a couple of thousand years old,
the most impactful being pAnini and the schools of study of pANinian
grammar.

Although there is value in these traditions, we should also be mindful
of the fact that grammars of kannaDa and other DraviDian languages were
written by people who held that all non-samskxta languages were
apabramhSAs (or corrupted speech). In the drive for standardization, non
PIE language families have been studied with the same scheme that
applied by pANini for samskxrta.

It's only with the advent of modern linguistics, etymology and phylogeny
that alternates have emerged. Although there's been many that are not
mentioned here, AK rAmAnujan's attempts to write a generative grammar
for kannaDa and the recent exhaustive work of Sankara BaT in writing a
grammar for kannaDa from first principles which have resulted in a
grammar which doesn't follow the same template of Samskxrta.

## A guide to writing in ellara kannaDa - EK

## Goals and Non goals

Eke prioritizes ellara kannaDa over formal kannaDa given its simplicity
and implicit appeal to ease of use. Eke doesn't have the same goals as
HK. HK aims to faithfully retain the original spelling in devanAgari
i.e. the original spelling in devaNagari can be reconstructed from text
in HK.

Eke also does not attempt to solve the spelling problems of English.
Although there are several attempts to do so like Arpabet, wiki
pronunciation for English there's no clear consensus. IPA is quite
complete but complex to learn and the extensive use of diacritics makes
it difficult to use on standard desktop and phone keyboards.

Attempting to unify Indic pronunciations and English is quite tricky. No
attempt will be made to synthesize them.

Although ellara kannaDa achieves a 77% complexity reduction from
35x35x21 ≈ 25725 to 21x21x13 ≈ 5733 symbols, its still a significant
number of symbols to learn. Eliminating ottakSaras could achieve a
further reduction to 21x13 ≈ 273 symbols.

This simplification is automatically obtained in usage of an alphabet
set (without diacritics). There is a reduction in precision in certain
cases. Eke, like HK goes down this line with only slight modifications.

Eke will use 31 symbols for all of ellara kannaDa, 41 symbols for formal
kannada including historical symbols and 44 to incorporate english f, w,
z.

When Eke is used with ellara kannaDa (ek) simplifications, the term
"Eke(ek)" will be used.

If it is a direct transliteration from any text, without any
alterations, the term "Eke" is used.

## Consonants

[sections/Eke_consonants.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_Consonants.md)

<div style="margin:0 auto;overflow:scroll;width:auto;max-width:100%">

| Eke                             | ka  | kha | ga  | gha | Ga         | ca  | cha | ja  | jha | Ya    | Ta  | Tha | Da  | Dha | Na  | ta  | tha | da  | dha | na  | na  | pa  | pha | ba  | bha | ma  | ya  |     | ra  | Ra  | la  | La  | Za  | va  | Sa  | Sha | sa  | ha  | kSa  |
|---------------------------------|-----|-----|-----|-----|------------|-----|-----|-----|-----|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Ashoka Brahmi                   | 𑀓   | 𑀔   | 𑀕   | 𑀖   | 𑀗          | 𑀘   | 𑀙   | 𑀚   | 𑀛   | 𑀜     | 𑀝   | 𑀞   | 𑀟   | 𑀠   | 𑀡   | 𑀢   | 𑀣   | 𑀤   | 𑀥   | 𑀦   |     | 𑀧   | 𑀨   | 𑀩   | 𑀪   | 𑀫   | 𑀬   |     | 𑀭   |     | 𑀮   | 𑀴   |     | 𑀯   | 𑀰   | 𑀱   | 𑀲   | 𑀳   |      |
| Devanagari                      | क   | ख   | ग   | घ   | ङ          | च   | छ   | ज   | झ   | ञ     | ट   | ठ   | ड   | ढ   | ण   | त   | थ   | द   | ध   | न   |     | प   | फ   | ब   | भ   | म   | य   | य़   | र   | ऱ   | ल   | ळ   | ऴ   | व   | श   | ष   | स   | ह   | क्ष   |
| Tamil                           | க   |     |     |     | ங          | ச   |     | ஜ   |     | ஞ     | ட   |     |     |     | ண   | த   |     |     |     | ந   | ன   | ப   |     |     |     | ம   | ய   |     | ர   | ற   | ல   | ள   | ழ   | வ   | ஶ   | ஷ   | ஸ   | ஹ   | க்ஷ   |
| Kannada                         | ಕ   | ಖ   | ಗ   | ಘ   | ಙ          | ಚ   | ಛ   | ಜ   | ಝ   | ಞ     | ಟ   | ಠ   | ಡ   | ಢ   | ಣ   | ತ   | ಥ   | ದ   | ಧ   | ನ   |     | ಪ   | ಫ   | ಬ   | ಭ   | ಮ   | ಯ   |     | ರ   | ಱ   | ಲ   | ಳ   | ೞ   | ವ   | ಶ   | ಷ   | ಸ   | ಹ   | ಕ್ಷ   |
| ellara kannaDa / ek             | ಕ   | ಕ   | ಗ   | ಗ   | ಂಕ ಂಗ      | ಚ   | ಚ   | ಜ   | ಜ   | ಂಚ ಂಜ | ಟ   | ಟ   | ಡ   | ಡ   | ಣ   | ತ   | ತ   | ದ   | ದ   | ನ   | ನ   | ಪ   |     | ಬ   |     | ಮ   | ಯ   |     | ರ   |     | ಲ   | ಳ   |     | ವ   | ಶ   |     | ಸ   | ಹ   |      |
| ellara kannada in Eke / EKe(ek) | ka  | ka  | ga  | ga  | nka or nga | ca  | ca  | ja  | ja  | nya   | Ta  | Ta  | Da  | Da  | Na  | ta  | ta  | da  | da  | na  | na  | pa  | pa  | ba  | ba  | ma  | ya  |     | ra  | ra  | la  | La  | La  | va  | Sa  | Sa  | sa  | ha  | kSa  |
| ISO                             | ka  | kha | ga  | gha | ṅa         | ca  | cha | ja  | jha | ña    | ṭa  | ṭha | ḍa  | ḍha | ṇa  | ta  | tha | da  | dha | na  | ṉa  | pa  | pha | ba  | bha | ma  | ya  | ẏa  | ra  | ṟa  | la  | ḷa  | ḻa  | va  | śa  | ṣa  | sa  | ha  | kṣa  |
| IK                              | ka  | kha | ga  | gha | nga        | cha | cha | ja  | jha | nya   | ta  | ta  | da  | da  | na  | tha | tha | dha | dha | na  | na  | pa  | pha | ba  | bha | ma  | ya  |     | ra  | ra  | la  | la  | la  | va  | sha | sha | sa  | ha  | ksha |
| HK                              | ka  | kha | ga  | gha | Ga         | ca  | cha | ja  | jha | Ya    | Ta  | Tha | Da  | Dha | Na  | ta  | tha | da  | dha | na  |     | pa  | pha | ba  | bha | ma  | ya  |     | ra  |     | la  | La  |     | va  | za  | sha | sa  | ha  | ksha |
| EKe                             | ka  | kha | ga  | gha | Ga         | ca  | cha | ja  | jha | Ya    | Ta  | Tha | Da  | Dha | Na  | ta  | tha | da  | dha | na  |     | pa  | pha | ba  | bha | ma  | ya  |     | ra  | Ra  | la  | La  | Za  | va  | Sa  | Sha | sa  | ha  | kSa  |

</div>

## Consonants of ellara kannaDa in Eke

[sections/Eke_Consonants_Table.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_Consonants_Table.md)

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

## Additional consonants in formal or legacy kannaDa in Eke

[sections/Eke_Consonants_Table_Extended.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_Consonants_Table_Extended.md)

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

## Vowels

## All vowels

[sections/Eke_Vowels.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_Vowels.md)

<div style="margin:0 auto;overflow:scroll;width:auto;max-width:100%">

| Eke           | a   | A   |     |     | i   | I   | u   | U   | e   | E   | ay  | o   | O   | av  | [ə](Schwa) | x\* | X\* | q\* | Q\* | m or n | H   |     |
|---------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------------|-----|-----|-----|-----|--------|-----|-----|
| a             | ka  | A   | kA  |     |     |     |     | i   | ki  | I   | kI  | u   | ku  | U   | kU         | e   | ke  | E   | kE  | ay     | kay | o   |
| Ashoka Brahmi | 𑀅   | 𑀓   | 𑀆   | 𑀓𑀸   |     |     |     |     | 𑀇   | 𑀓𑀺   | 𑀈   | 𑀓𑀻   | 𑀉   | 𑀓𑀼   | 𑀊          | 𑀓𑀽   |     |     | 𑀏   | 𑀓𑁂      | 𑀐   | 𑀓𑁃   |
| Devanagari    | अ   | क   | आ   | का  | ॲ   | कॅ   | ऑ   | कॉ  | इ   | कि  | ई   | की  | उ   | कु   | ऊ          | कू   | ऎ   | कॆ   | ए   | के      | ऐ   | कै   |
| Tamil         | அ   | க   | ஆ   | கா  |     |     |     |     | இ   | கி  | ஈ   | கீ   | உ   | கு  | ஊ          | கூ  | எ   | கெ  | ஏ   | கே     | ஐ   | கை  |
| Kannada       | ಅ   | ಕ   | ಆ   | ಕಾ  |     |     |     |     | ಇ   | ಕಿ   | ಈ   | ಕೀ  | ಉ   | ಕು  | ಊ          | ಕೂ  | ಎ   | ಕೆ   | ಏ   | ಕೇ     | ಐ   | ಕೈ  |
| EK            | ಅ   | ಕ   | ಆ   | ಕಾ  |     |     |     |     | ಇ   | ಕಿ   | ಈ   | ಕೀ  | ಉ   | ಕು  | ಊ          | ಕೂ  | ಎ   | ಕೆ   | ಏ   | ಕೇ     |     |     |
| ISO           | a   | ka  | ā   | kā  | ê   | kê  | ô   | kô  | i   | ki  | ī   | kī  | u   | ku  | ū          | kū  | e   | ke  | ē   | kē     | ai  | kai |
| IK            | a   | ka  | aa  | kaa |     |     |     |     | i   | ki  | ee  | kee | u   | ku  | oo         | koo | e   | ke  | ay  | kay    | ai  | kai |
| HK            | a   | ka  | A   | kA  |     |     |     |     | i   | ki  | I   | kI  | u   | ku  | U          | kU  |     |     | e   | ke     | ai  | kai |
| Eke           | a   | ka  | A   | kA  |     |     |     |     | i   | ki  | I   | kI  | u   | ku  | U          | kU  | e   | ke  | E   | kE     | ay  | kay |

</div>

## Eke from English/Latin alphabet combinations to kannaDa

|         |            |               |               |             |                                                                  |
|---------|------------|---------------|---------------|-------------|------------------------------------------------------------------|
| **Eke** | **akSara** | **ottakSara** | **EK**        | **kannaDa** | **Other**                                                        |
| **a**   | ಅ          | ❌            | ✅            | ✅          | ❌                                                               |
| **A**   | ಆ          | ❌            | ✅            | ✅          | ❌                                                               |
| **b**   | ಬ್          | ್ಬ             | ✅            | ✅          | ❌                                                               |
| **B**   | ❌         | ❌            | ❌            | ❌          | ❌                                                               |
| **c**   | ಚ್          | ್ಚ             | ✅            | ✅          | ❌                                                               |
| **d**   | ದ್          | ್ದ             | ✅            | ✅          | ❌                                                               |
| **D**   | ಡ್          | ್ಡ             | ✅            | ✅          | ❌                                                               |
| **e**   | ಎ          | ❌            | ✅            | ✅          | ❌                                                               |
| **E**   | ಏ          | ❌            | ✅            | ✅          | ❌                                                               |
| **f**   | ❌         | ❌            | ❌            | ❌          | English f                                                        |
| **F**   | ❌         | ❌            | ❌            | ❌          | ❌                                                               |
| **g**   | ಗ್          | ್ಗ             | ✅            | ✅          | ❌                                                               |
| **G**   | ಙ್          | ್ಙ             | ಂಕ್ ಂಗ್         | ✅          | anusvAra version used in EK                                      |
| **h**   | ಹ್          | ್ಹ             | ✅            | ✅          | ❌                                                               |
| **H**   | ಃ          | ❌            | ❌            | ✅          | ❌                                                               |
| **i**   | ಇ          | ❌            | ✅            | ✅          | ❌                                                               |
| **I**   | ಈ          | ❌            | ✅            | ✅          | ❌                                                               |
| **j**   | ಜ್          | ್ಜ             | ✅            | ✅          | ❌                                                               |
| **J**   | ❌         | ❌            | ❌            | ❌          | ❌                                                               |
| **k**   | ಕ್          | ್ಕ             | ✅            | ✅          | ❌                                                               |
| **K**   | ❌         | ❌            | ❌            | ❌          | ❌                                                               |
| **l**   | ಲ್          | ್ಲ             | ✅            | ✅          | ❌                                                               |
| **L**   | ಳ್          | ್ಳ             | ✅            | ✅          | ❌                                                               |
| **m**   | ಮ್          | ್ಮ             | ✅            | ✅          | anusvAra: ಂಪ/ಂಬ for mpa/mba                                      |
| **M**   | ❌         | ❌            | ❌            | ❌          | anuSvAra in HK                                                   |
| **n**   | ನ್          | ್ನ             | ✅            | ✅          | anusvAra: ಂಕ/ಙ್ಕ is nka, ಂಚ/ಞ್ಚ is nca, ಂಟ/ಣ್ಟ is nTa, ಂತ/ನ್ತ is nta |
| **N**   | ಣ್          | ್ಣ             | ✅            | ✅          | ❌                                                               |
| **o**   | ಒ          | ❌            | ✅            | ✅          | ❌                                                               |
| **O**   | ಓ          | ❌            | ✅            | ✅          | ❌                                                               |
| **p**   | ಪ್          | ್ಪ             | ✅            | ✅          | ❌                                                               |
| **P**   | ❌         | ❌            | ❌            | ❌          | ❌                                                               |
| **q**   | ಌ          | ❌            | li lu         | ✅          | ❌                                                               |
| **Q**   | ೡ          | ❌            | ❌            | ✅          | ❌                                                               |
| r       | ರ್          | ್ರ             | ✅            | ✅          | ❌                                                               |
| **R**   | ಱ್          | ್ಱ             | r ರ್           | ✅          | ಕೆಱೆ for lake in old Kannada                                       |
| **s**   | ಸ್          | ್ಸ             | ✅            | ✅          | ❌                                                               |
| **S**   | ಶ್          | ್ಶ             | ✅            | ✅          | z in HK                                                          |
| **t**   | ತ್          | ್ತ             | ✅            | ✅          | ❌                                                               |
| **T**   | ಟ್          | ್ಟ             | ✅            | ✅          | ❌                                                               |
| **u**   | ಉ          | ❌            | ✅            | ✅          | ❌                                                               |
| **U**   | ಊ          | ❌            | ✅            | ✅          | ❌                                                               |
| **v**   | ವ್          | ್ವ             | ✅            | ✅          | ❌                                                               |
| **V**   | ❌         | ❌            | ❌            | ❌          | ❌                                                               |
| **w**   | ❌         | ❌            | ❌            | ❌          | English w, ಔ in IK                                               |
| **W**   | ❌         | ❌            | ❌            | ❌          | ❌                                                               |
| **x**   | ಋ          | ❌            | ri ರಿ ru ರು    | ✅          | Analogous to 𑀋 in aSOkan brAhmi R in HK                          |
| **X**   | ೠ          | ❌            | ❌            | ✅          | ❌                                                               |
| **y**   | ಯ್          | ್ಯ             | ✅            | ✅          | ❌                                                               |
| **Y**   | ಞ್          | ್ಞ             | ಗ್ನ gna ನ್ಯ nya | ✅          | anusvAra version used in EK                                      |
| **z**   | ❌         | ❌            | ❌            | ❌          | English or Hindi z                                               |
| **Z**   | ೞ್          | ್ೞ             | ಳ್ L           | ✅          | tamiZ                                                            |

## Eke from English/Latin alphabet to kannaDa

[sections/Eke_EnglishAlphToKannadaAks.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_EnglishAlphToKannadaAks.md)

|         |            |               |        |             |             |
|---------|------------|---------------|--------|-------------|-------------|
| **Eke** | **akSara** | **ottakSara** | **EK** | **kannaDa** | **Other**   |
| **bh**  | ಭ್          | ್ಭ             | b ಬ್    | ✅          | ❌          |
| **ch**  | ಛ್          | ್ಛ             | c ಚ್    | ✅          | ❌          |
| **dh**  | ಧ್          | ್ಧ             | d ದ್    | ✅          | ❌          |
| **Dh**  | ಢ್          | ್ಢ             | D ಡ್    | ✅          | ❌          |
| **gh**  | ಘ್          | ್ಘ             | g ಗ್    | ✅          | ❌          |
| **jh**  | ಝ್          | ್ಝ             | j ಜ್    | ✅          | ❌          |
| **kh**  | ಖ್          | ್ಖ             | k ಕ್    | ✅          | ❌          |
| **ph**  | ಫ್          | ್ಫ             | p ಪ್    | ✅          | ❌          |
| **Sh**  | ಷ್          | ್ಷ             | S ಶ್    | ✅          | Retroflex ಶ್ |
| **th**  | ಥ್          | ್ಥ             | t ತ್    | ✅          | ❌          |
| **Th**  | ಠ್          | ್ಠ             | T ಟ್    | ✅          | ❌          |

## diphthongs

[sections/Eke_Diphthongs.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_Diphthongs.md)

|     |         |     |     |     |     |     |     |     |     |     |     |
|-----|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |         | ಅ   | ಆ   | ಇ   | ಈ   | ಉ   | ಊ   | ಎ   | ಏ   | ಒ   | ಓ   |
| ಯ್   | kannaDa | ಐ   | ಆಯ್  | ಇಯ್  | ಈಯ್  | ಉಯ್  | ಊಯ್  | ಎಯ್  | ಏಯ್  | ಒಯ್  | ಓಯ್  |
|     |         | ಕೈ  | ಕಾಯ್ | ಕಿಯ್  | ಕೀಯ್ | ಕುಯ್ | ಕೂಯ್ | ಕೆಯ್  | ಕೇಯ್ | ಕೊಯ್ | ಕೋಯ್ |
|     | EK      | ಅಯ್  | ಆಯ್  | ಇಯ್  | ಈಯ್  | ಉಯ್  | ಊಯ್  | ಎಯ್  | ಏಯ್  | ಒಯ್  | ಓಯ್  |
|     |         | ಕಯ್  | ಕಾಯ್ | ಕಿಯ್  | ಕೀಯ್ | ಕುಯ್ | ಕೂಯ್ | ಕೆಯ್  | ಕೇಯ್ | ಕೊಯ್ | ಕೋಯ್ |
|     | Eke     | ay  | Ay  | iy  | Iy  | uy  | Uy  | ey  | Ey  | oy  | Oy  |
|     |         | kay | kAy | kiy | kIy | kuy | kUy | key | kEy | koy | kOy |
| ವ್   | kannaDa | ಔ   | ಆವ್  | ಇವ್  | ಈವ್  | ಉವ್  | ಊವ್  | ಎವ್  | ಏವ್  | ಒವ್  | ಓವ್  |
|     |         | ಕೌ   | ಕಾವ್ | ಕಿವ್  | ಕೀವ್ | ಕುವ್ | ಕೂವ್ | ಕೆವ್  | ಕೇವ್ | ಕೊವ್ | ಕೋವ್ |
|     | EK      | ಅವ್  | ಆವ್  | ಇವ್  | ಈವ್  | ಉವ್  | ಊವ್  | ಎವ್  | ಏವ್  | ಒವ್  | ಓವ್  |
|     |         | ಕವ್  | ಕಾವ್ | ಕಿವ್  | ಕೀವ್ | ಕುವ್ | ಕೂವ್ | ಕೆವ್  | ಕೇವ್ | ಕೊವ್ | ಕೋವ್ |
|     | Eke     | av  | Av  | iv  | Iv  | uv  | Uv  | ev  | Ev  | ov  | Ov  |
|     |         | kav | kAv | kiv | kIv | kuv | kUv | kev | kEv | kov | kOv |

## ellara kannaDada akSaragaLu

[sections/Eke_akSaragaLu.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_aksaragaLu.md)

|         |               |       |       |       |       |       |       |       |       |       |       |       |
|---------|---------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| **Num** | **ottakSara** | **್**  | **ಅ** | **ಆ** | **ಇ** | **ಈ** | **ಉ** | **ಊ** | **ಎ** | **ಏ** | **ಒ** | **ಓ** |
| 0       | ❌            | ❌    | **a** | **A** | **i** | **I** | **u** | **U** | **e** | **E** | **o** | **O** |
| 1       | ್ಕ             | ಕ್     | ಕ     | ಕಾ    | ಕಿ     | ಕೀ    | ಕು    | ಕೂ    | ಕೆ     | ಕೇ    | ಕೊ    | ಕೋ    |
|         | k             | k     | ka    | kA    | ki    | kI    | ku    | kU    | ke    | kE    | ko    | kO    |
| 2       | ್ಗ             | ಗ್     | ಗ     | ಗಾ    | ಗಿ     | ಗೀ    | ಗು    | ಗೂ    | ಗೆ     | ಗೇ    | ಗೊ    | ಗೋ    |
|         | g             | g     | ga    | gA    | gi    | gI    | gu    | gU    | ge    | gE    | go    | gO    |
| 3       | ್ಚ             | ಚ್     | ಚ     | ಚಾ    | ಚಿ     | ಚೀ    | ಚು    | ಚೂ    | ಚೆ     | ಚೇ    | ಚೂ    | ಚೋ    |
|         | c             | c     | ca    | cA    | ci    | cI    | cu    | cU    | ce    | cE    | co    | cO    |
| 4       | ್ಜ             | ಜ್     | ಜ     | ಜಾ    | ಜಿ     | ಜೀ    | ಜು    | ಜೂ    | ಜೆ     | ಜೇ    | ಜೊ    | ಜೋ    |
|         | j             | j     | ja    | jA    | ji    | jI    | ju    | jU    | je    | jE    | jo    | jO    |
| 5       | ್ಟ             | ಟ್     | ಟ     | ಟಾ    | ಟಿ     | ಟೀ    | ಟು    | ಟೂ    | ಟೆ     | ಟೇ    | ಟೊ    | ಟೋ    |
|         | T             | T     | Ta    | TA    | Ti    | TI    | Tu    | TU    | Te    | TE    | To    | TO    |
| 6       | ್ಡ             | ಡ್     | ಡ     | ಡಾ    | ಡಿ     | ಡೀ    | ಡು    | ಡೂ    | ಡೆ     | ಡೇ    | ಡೊ    | ಡೋ    |
|         | D             | D     | Da    | DA    | Di    | DI    | Du    | DU    | De    | DE    | Do    | DO    |
| 7       | ್ಣ             | ಣ್     | ಣ     | ಣಾ    | ಣಿ     | ಣೀ    | ಣು    | ಣೂ    | ಣೆ     | ಣೇ    | ಣೊ    | ಣೋ    |
|         | N             | N     | Na    | NA    | Ni    | NI    | Nu    | NU    | Ne    | NE    | No    | NO    |
| 8       | ್ತ             | ತ್     | ತ     | ತಾ    | ತಿ     | ತೀ    | ತು    | ತೂ    | ತೆ     | ತೇ    | ತೊ    | ತೋ    |
|         | t             | t     | ta    | tA    | ti    | tI    | tu    | tU    | te    | tE    | to    | tO    |
| 9       | ್ದ             | ದ್     | ದ     | ದಾ    | ದಿ     | ದೀ    | ದು    | ದೂ    | ದೆ     | ದೇ    | ದೊ    | ದೋ    |
|         | d             | d     | da    | dA    | di    | dI    | du    | dU    | de    | dE    | do    | dO    |
| 10      | ್ನ             | ನ್     | ನ     | ನಾ    | ನಿ     | ನೀ    | ನು    | ನೂ    | ನೆ     | ನೇ    | ನೂ    | ನೋ    |
|         | n             | n     | na    | nA    | ni    | nI    | nu    | nU    | ne    | nE    | no    | nO    |
| 11      | ್ಪ             | ಪ್     | ಪ     | ಪಾ    | ಪಿ     | ಪೀ    | ಪು    | ಪೂ    | ಪೆ     | ಪೇ    | ಪೊ    | ಪೋ    |
|         | p             | p     | pa    | pA    | pi    | pI    | pu    | pU    | pe    | pE    | po    | pO    |
| 12      | ್ಬ             | ಬ್     | ಬ     | ಬಾ    | ಬಿ     | ಬೀ    | ಬು    | ಬೂ    | ಬೆ     | ಬೇ    | ಬೂ    | ಬೋ    |
|         | b             | b     | ba    | bA    | bi    | bI    | bu    | bU    | be    | bE    | bo    | bO    |
| 13      | ್ಮ             | ಮ್     | ಮ     | ಮಾ    | ಮಿ     | ಮೀ    | ಮು    | ಮೂ    | ಮೆ     | ಮೇ    | ಮೊ    | ಮೋ    |
|         | m             | m     | ma    | mA    | mi    | mI    | mu    | mU    | me    | mE    | mo    | mO    |
| 14      | ್ಯ             | ಯ್     | ಯ     | ಯಾ    | ಯಿ     | ಯೀ    | ಯು    | ಯೂ    | ಯೆ     | ಯೇ    | ಯೊ    | ಯೋ    |
|         | y             | y     | ya    | yA    | yi    | yI    | yu    | yU    | ye    | yE    | yo    | yO    |
| 15      | ್ರ             | ರ್     | ರ     | ರಾ    | ರಿ     | ರೀ    | ರು    | ರೂ    | ರೆ     | ರೇ    | ರೊ    | ರೋ    |
|         | r             | r     | ra    | rA    | ri    | rI    | ru    | rU    | re    | rE    | ro    | rO    |
| 16      | ್ಲ             | ಲ್     | ಲ     | ಲಾ    | ಲಿ     | ಲೀ    | ಲು    | ಲೂ    | ಲೆ     | ಲೇ    | ಲೊ    | ಲೋ    |
|         | l             | l     | la    | lA    | li    | lI    | lu    | lU    | le    | lE    | lo    | lO    |
| 17      | ್ವ             | ವ್     | ವ     | ವಾ    | ವಿ     | ವೀ    | ವು    | ವೂ    | ವೆ     | ವೇ    | ವೊ    | ವೋ    |
|         | v             | v     | va    | vA    | vi    | vI    | vu    | vU    | ve    | vE    | vo    | vO    |
| 18      | ್ಶ             | ಶ್     | ಶ     | ಶಾ    | ಶಿ     | ಶೀ    | ಶು    | ಶೂ    | ಶೆ     | ಶೇ    | ಶೊ    | ಶೋ    |
|         | S             | S     | Sa    | SA    | Si    | SI    | Su    | SU    | Se    | SE    | So    | SO    |
| 19      | ್ಸ             | ಸ್     | ಸ     | ಸಾ    | ಸಿ     | ಸೀ    | ಸು    | ಸೂ    | ಸೆ     | ಸೇ    | ಸೊ    | ಸೋ    |
|         | s             | s     | sa    | sA    | si    | sI    | su    | sU    | se    | sE    | so    | sO    |
| 20      | ್ಹ             | ಹ್     | ಹ     | ಹಾ    | ಹಿ     | ಹೀ    | ಹು    | ಹೂ    | ಹೆ     | ಹೇ    | ಹೂ    | ಹೋ    |
|         | h             | h     | ha    | hA    | hi    | hI    | hu    | hU    | he    | hE    | ho    | hO    |
| 21      | ್ಳ             | ಳ್     | ಳ     | ಳಾ    | ಳಿ     | ಳೀ    | ಳು    | ಳೂ    | ಳೆ     | ಳೇ    | ಳೊ    | ಳೋ    |
|         | L             | L     | La    | LA    | Li    | LI    | Lu    | LU    | Le    | LE    | Lo    | LO    |

## Remaining/Formal kannaDa akSaras / uLida akSaragaLu

[sections/Eke_formal_akSaragalu.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_formal_akSaragaLu.md)

|         |               |       |       |       |       |       |       |       |       |       |       |       |
|---------|---------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| **Num** | **ottakSara** | **್**  | **ಅ** | **ಆ** | **ಇ** | **ಈ** | **ಉ** | **ಊ** | **ಎ** | **ಏ** | **ಒ** | **ಓ** |
| 0       | ❌            | ❌    | **a** | **A** | **i** | **I** | **u** | **U** | **e** | **E** | **o** | **O** |
| 1       | ್ಖ             | ಖ್     | ಖ     | ಖಾ    | ಖಿ     | ಖೀ    | ಖು    | ಖೂ    | ಖೆ     | ಖೇ    | ಖೊ    | ಖೋ    |
|         | ್ಕ್ಹ            | ಕ್ಹ್    | ಕ್ಹ    | ಕ್ಹಾ   | ಕ್ಹಿ    | ಕ್ಹೀ   | ಕ್ಹು   | ಕ್ಹೂ   | ಕ್ಹೆ    | ಕ್ಹೇ   | ಕ್ಹೊ   | ಕ್ಹೋ   |
|         | kh            | kh    | kha   | khA   | khi   | khI   | khu   | khU   | khe   | khE   | kho   | khO   |
| 2       | ್ಘ             | ಘ್     | ಘ     | ಘಾ    | ಘಿ     | ಘೀ    | ಘು    | ಘೂ    | ಘೆ     | ಘೇ    | ಘೊ    | ಘೋ    |
|         | ್ಗ್ಹ            | ಗ್ಹ್    | ಗ್ಹ    | ಗ್ಹಾ   | ಗ್ಹಿ    | ಗ್ಹೀ   | ಗ್ಹು   | ಗ್ಹೂ   | ಗ್ಹೆ    | ಗ್ಹೇ   | ಗ್ಹೊ   | ಗ್ಹೋ   |
|         | gh            | gh    | gha   | ghA   | ghi   | ghI   | ghu   | ghU   | ghe   | ghE   | gho   | ghO   |
| 3       | ್ಛ             | ಛ್     | ಛ     | ಛಾ    | ಛಿ     | ಛೀ    | ಛು    | ಛೂ    | ಛೆ     | ಛೇ    | ಛೊ    | ಛೋ    |
|         | ್ಚ್ಹ            | ಚ್ಹ್    | ಚ್ಹ    | ಚ್ಹಾ   | ಚ್ಹಿ    | ಚ್ಹೀ   | ಚ್ಹು   | ಚ್ಹೂ   | ಚ್ಹೆ    | ಚ್ಹೇ   | ಚ್ಹೊ   | ಚ್ಹೋ   |
|         | ch            | ch    | cha   | chA   | chi   | chI   | chu   | cU    | ce    | cE    | co    | cO    |
| 4       | ್ಝ             | ಝ್     | ಝ     | ಝಾ    | ಝಿ     | ಝೀ    | ಝು    | ಝೂ    | ಝೆ     | ಝೇ    | ಝೊ    | ಝೋ    |
|         | ್ಜ್ಹ            | ಜ್ಹ್    | ಜ್ಹ    | ಜ್ಹಾ   | ಜ್ಹಿ    | ಜ್ಹೀ   | ಜ್ಹು   | ಜ್ಹೂ   | ಜ್ಹೆ    | ಜ್ಹೇ   | ಜ್ಹೊ   | ಜ್ಹೋ   |
|         | jh            | jh    | jha   | jhA   | jhi   | jhI   | jhu   | jhU   | jhe   | jhE   | jho   | jhO   |
| 5       | ್ಠ             | ಠ್     | ಠ     | ಠಾ    | ಠಿ     | ಠೀ    | ಠು    | ಠೂ    | ಠೆ     | ಠೇ    | ಠೊ    | ಠೋ    |
|         | ್ಟ್ಹ            | ಟ್ಹ್    | ಟ್ಹ    | ಟ್ಹಾ   | ಟ್ಹಿ    | ಟ್ಹೀ   | ಟ್ಹು   | ಟ್ಹೂ   | ಟ್ಹೆ    | ಟ್ಹೇ   | ಟ್ಹೊ   | ಟ್ಹೋ   |
|         | Th            | Th    | Tha   | ThA   | Thi   | ThI   | Thu   | ThU   | The   | ThE   | Tho   | ThO   |
| 6       | ್ಢ             | ಢ್     | ಢ     | ಢಾ    | ಢಿ     | ಢೀ    | ಢು    | ಢೂ    | ಢೆ     | ಢೇ    | ಢೊ    | ಢೋ    |
|         | ್ಡ್ಹ            | ಡ್ಹ್    | ಡ್ಹ    | ಡ್ಹಾ   | ಡ್ಹಿ    | ಡ್ಹೀ   | ಡ್ಹು   | ಡ್ಹೂ   | ಡ್ಹೆ    | ಡ್ಹೇ   | ಡ್ಹೊ   | ಡ್ಹೋ   |
|         | Dh            | Dh    | Dha   | DhA   | Dhi   | DhI   | Dhu   | DhU   | Dhe   | DhE   | Dho   | DhO   |
| 7       | ್ಥ             | ಥ್     | ಥ     | ಥಾ    | ಥಿ     | ಥೀ    | ಥು    | ಥೂ    | ಥೆ     | ಥೇ    | ಥೊ    | ಥೋ    |
|         | ್ತ್ಹ            | ತ್ಹ್    | ತ್ಹ    | ತ್ಹಾ   | ತ್ಹಿ    | ತ್ಹೀ   | ತ್ಹು   | ತ್ಹೂ   | ತ್ಹೆ    | ತ್ಹೇ   | ತ್ಹೊ   | ತ್ಹೋ   |
|         | th            | th    | tha   | thA   | thi   | thI   | thu   | thU   | the   | thE   | tho   | thO   |
| 8       | ್ಧ             | ಧ್     | ಧ     | ಧಾ    | ಧಿ     | ಧೀ    | ಧು    | ಧೂ    | ಧೆ     | ಧೇ    | ಧೊ    | ಧೋ    |
|         | ್ದ್ಹ            | ದ್ಹ್    | ದ್ಹ    | ದ್ಹಾ   | ದ್ಹಿ    | ದ್ಹೀ   | ದ್ಹು   | ದ್ಹೂ   | ದ್ಹೆ    | ದ್ಹೇ   | ದ್ಹೊ   | ದ್ಹೋ   |
|         | dh            | dh    | dha   | dhA   | dhi   | dhI   | dhu   | dhU   | dhe   | dhE   | dho   | dhO   |
| 9       | ್ಫ             | ಫ್     | ಫ     | ಫಾ    | ಫಿ     | ಫೀ    | ಫು    | ಫೂ    | ಫೆ     | ಫೇ    | ಫೊ    | ಫೋ    |
|         | ್ಪ್ಹ            | ಪ್ಹ್    | ಪ್ಹ    | ಪ್ಹಾ   | ಪ್ಹಿ    | ಪ್ಹೀ   | ಪ್ಹು   | ಪ್ಹೂ   | ಪ್ಹೆ    | ಪ್ಹೇ   | ಪ್ಹೊ   | ಪ್ಹೋ   |
|         | ph            | ph    | pha   | phA   | phi   | phI   | phu   | phU   | phe   | phE   | pho   | phO   |
| 10      | ್ಭ             | ಭ್     | ಭ     | ಭಾ    | ಭಿ     | ಭೀ    | ಭು    | ಭೂ    | ಭೆ     | ಭೇ    | ಭೊ    | ಭೋ    |
|         | ್ಬ್ಹ            | ಬ್ಹ್    | ಬ್ಹ    | ಬ್ಹಾ   | ಬ್ಹಿ    | ಬ್ಹೀ   | ಬ್ಹು   | ಬ್ಹೂ   | ಬ್ಹೆ    | ಬ್ಹೇ   | ಬ್ಹೊ   | ಬ್ಹೋ   |
|         | bh            | bh    | bha   | bhA   | bhi   | bhI   | bhu   | bhU   | bhe   | bhE   | bho   | bhO   |
| 11      | ್ಱ             | ಱ್     | ಱ     | ಱಾ    | ಱಿ     | ಱೀ    | ಱು    | ಱೂ    | ಱೆ     | ಱೇ    | ಱೊ    | ಱೋ    |
|         | R             | R     | Ra    | RA    | Ri    | RI    | Ru    | RU    | Re    | RE    | Ro    | RO    |
| 12      | ್ಷ             | ಷ್     | ಷ     | ಷಾ    | ಷಿ     | ಷೀ    | ಷು    | ಷೂ    | ಷೆ     | ಷೇ    | ಷೊ    | ಷೋ    |
|         | Sh            | Sh    | Sha   | ShA   | Shi   | ShI   | Shu   | ShU   | She   | ShE   | Sho   | ShO   |
| 13      | ್ೞ             | ೞ್     | ೞ     | ೞಾ    | ೞಿ     | ೞೀ    | ೞು    | ೞೂ    | ೞೆ     | ೞೇ    | ೞೊ    | ೞೋ    |
|         | Z             | Z     | Za    | ZA    | Zi    | ZI    | Zu    | ZU    | Ze    | ZE    | Zo    | ZO    |

## Character distributions

Character distributions of words in Alar.

### Raw

Raw distributions of the kannaDa akSaras in the Alar dictionary can be
found here:
[Kannada_distributions.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Kannada_distributions.md)

It includes consonants, vowels (as full characters), modifiers(or half
charactoers, most of the vowels) and consonants as modifiers
(ottakSaras).

|         |           |
|---------|-----------|
| Total   | 989661    |
| **್**    | **59932** |
| **ಿ**    | **54773** |
| **ು**   | **45920** |
| **ರ**   | **45816** |
| **ಾ**   | **36978** |
| **ೆ**    | **32298** |
| **ಕ**   | **32121** |
| **ಗ**   | **31622** |
| **ತ**   | **31452** |
| **ವ**   | **26609** |
| **ಸ**   | **26340** |
| **ನ**   | **23180** |
| **ಂ**   | **22243** |
| **ಮ**   | **21340** |
| **ಲ**   | **20297** |
| **ದ**   | **19706** |
| **ಪ**   | **19475** |
| **ಡ**   | **17442** |
| **ಯ**   | **15766** |
| **ಳ**   | **15243** |
| **ಬ**   | **13899** |
| **ಹ**   | **12472** |
| **ಣ**   | **11156** |
| **ಟ**   | **10299** |
| **ಚ**   | **10129** |
| **ಜ**   | **9638**  |
| **್ರ**   | **9601**  |
| ೊ       | **9426**  |
| ಅ       | **8963**  |
| **ೋ**   | **8686**  |
| **ೇ**   | **7549**  |
| **್ತ**   | **7456**  |
| **ೀ**   | **7035**  |
| **ಶ**   | **6841**  |
| ಷ       | 6426      |
| **್ಯ**   | **5735**  |
| **ೂ**   | **5706**  |
| ಧ       | 5168      |
| **್ಟ**   | **4815**  |
| ಭ       | 4618      |
| ್ವ       | **4340**  |
| ್ಕ       | **4240**  |
| ಱ       | 4088      |
| **ಉ**   | **3644**  |
| **ಆ**   | **3551**  |
| **\|್ಮ** | **3470**  |
| ೈ       | 2862      |
| ್ಪ       | 2699      |
| ್ಷ       | 2534      |
| ್ಲ       | **2497**  |
| ಖ       | 2460      |
| ೃ       | 2301      |
| ್ನ       | **2232**  |
| ್ಗ       | **2090**  |
| ್ಚ       | **2025**  |
| ಥ       | 1976      |
| ್ಣ       | **1943**  |
| ಇ       | **1879**  |
| ಎ       | **1830**  |
| ಒ       | **1819**  |
| ್ದ       | **1573**  |
| ೞ       | 1461      |
| ್ಳ       | **1421**  |
| ್ಬ       | **1380**  |
| ೌ        | 1329      |
| ಘ       | 1177      |
| ್ಡ       | **1144**  |
| ್ಥ       | 1130      |
| ್ಧ       | 1090      |
| ್ಜ       | **1042**  |
| ಠ       | 993       |
| ಫ       | 879       |
| ್ಸ       | **768**   |
| ಛ       | 764       |
| ಏ       | **675**   |
| ಞ       | 641       |
| ್ಞ       | 638       |
| ಢ       | 424       |
| ಓ       | **422**   |
| ್ಛ       | 415       |
| ಊ       | **379**   |
| ್ಭ       | 370       |
| ್ಠ       | 365       |
| ಈ       | **305**   |
| ಃ       | 290       |
| ಝ       | 274       |
| ್ಶ       | **268**   |
| ಐ       | 221       |
| ಋ       | 172       |
| ್ಫ       | 158       |
| ್ಘ       | 130       |
| ಔ       | 127       |
| ್ಖ       | 119       |
| ್ಹ       | **108**   |
| ಙ       | 39        |
| ್ಝ       | 30        |
| ್ಙ       | 8         |
| ಼        | 4         |
| ್ಢ       | 3         |
| ೱ       | 0         |
| ೯       | 0         |
| ೮       | 0         |
| ೭       | 0         |
| ೬       | 0         |
| ೫       | 0         |
| ೪       | 0         |
| ೩       | 0         |
| ೨       | 0         |
| ೧       | 0         |
| ೦       | 0         |
| ್ೞ       | 0         |
| ್ಱ       | 0         |

### Eke consonants

Below table has the ottulis merged into kiridulis since ottulis are
represented by an additional h. ottakSaras also map to the underlying
consonant representation reflecting the real spread of consonants.

Frequency tables are listed for EK representations only. As expected
ottulis fall below every EK consonant in the frequency distribution of
characters in words found in the alar dictionary.

[sections/Eke_char_distributions_consonants.md
](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_char_distributions_consonants.md)

|            |            |            |               |           |                                                 |                          |                 |                    |                |
|------------|------------|------------|---------------|-----------|-------------------------------------------------|--------------------------|-----------------|--------------------|----------------|
| **Eke**    | **akSara** | **count**  | **ottakSara** | **count** | **EK alternate: ottuli/Legacy**                 | **count**                | **Total count** | **% of consonant** | **% of total** |
| **r**      | ರ್          | 45816      | ್ರ             | 9601      | ಱ್, ್ಱ, ಋ, ೃ , ೠ, ್ೠ                               | 4088, 0, 172, 2301, 0, 0 | 61978           | **11.35%**         | 5.76%          |
| **t**      | ತ್          | 31452      | ್ತ             | 7456      | ಥ, ್ಥ                                            | 1976 ,1130               | 42014           | **7.69%**          | 3.91%          |
| **k**      | ಕ್          | 34581      | ್ಕ             | 4240      | ಖ, ್ಖ                                            | 2460, 119                | 41400           | **7.58%**          | 3.85%          |
| **n**      | ನ್          | 23180      | ್ನ             | 2232      | Unvoiced ನ್, anusVAra with k,g, c, j, T, D, t, n | 0, 14723                 | 40135           | **7.35%**          | 3.73%          |
| **g**      | ಗ್          | 31622      | ್ಗ             | 2090      | ಘ, ್ಘ                                            | 1177, 130                | 35019           | **6.41%**          | 3.26%          |
| **m**      | ಮ್          | 21340      | ್ಮ             | 3470      | anusVAra with p, b, s, S, h                     | 7520                     | 32330           | **5.92%**          | 3.01%          |
| **v**      | ವ್          | 26609      | ್ವ             | 4340      |                                                 |                          | 30949           | **5.67%**          | 2.88%          |
| **d**      | ದ್          | 19706      | ್ದ             | 1573      | ಧ್, ್ಧ                                            | 5168, 1090               | 27537           | **5.04%**          | 2.56%          |
| **s**      | ಸ್          | 26340      | ್ಸ             | 768       |                                                 |                          | 27108           | **4.96%**          | 2.52%          |
| **p**      | ಪ್          | 19475      | ್ಪ             | 2699      | ಫ್, ್ಫ                                            | 879, 158                 | 23211           | **4.25%**          | 2.16%          |
| **l**      | ಲ್          | 20297      | ್ಲ             | 2497      |                                                 | 0                        | 22794           | **4.17%**          | 2.12%          |
| **y**      | ಯ್          | 15766      | ್ಯ             | 5735      | ಐ                                               | 221                      | 21722           | **3.98%**          | 2.02%          |
| **b**      | ಬ್          | 13899      | ್ಬ             | 1380      | ಭ್, ್ಭ                                            | 4618, 370                | 20267           | **3.71%**          | 1.88%          |
| **D**      | ಡ್          | 17442      | ್ಡ             | 1144      | ಢ್, ್ಢ                                            | 424, 3                   | 19013           | **3.48%**          | 1.77%          |
| **L**      | ಳ್          | 15243      | ್ಳ             | 1421      | ೞ್, ್ೞ                                            | 1461, 0                  | 18125           | **3.32%**          | 1.69%          |
| **T**      | ಟ್          | 10299      | ್ಟ             | 4815      | ಠ್, ್ಠ                                            | 993, 365                 | 16472           | **3.02%**          | 1.53%          |
| **S**      | ಶ್          | 6841       | ್ಶ             | 268       | ಷ್, ್ಷ                                            | 6426, 2534               | 16069           | **2.94%**          | 1.49%          |
| **c**      | ಚ್          | 10129      | ್ಚ             | 2025      | ಛ್, ್ಛ                                            | 764, 415                 | 13333           | **2.44%**          | 1.24%          |
| **N**      | ಣ್          | 11156      | ್ಣ             | 1943      |                                                 | 0                        | 13099           | **2.40%**          | 1.22%          |
| **h**      | ಹ್          | 12472      | ್ಹ             | 108       | ottulis - can be omitted                        | 24916                    | 12580           | **2.30%**          | 1.17%          |
| **j**      | ಜ್          | 9638       | ್ಜ             | 1042      | ಝ್, ್ಝ                                            | 274, 30                  | 10984           | **2.01%**          | 1.02%          |
| **Totals** |            | **423303** |               | **60847** |                                                 | **61989**                | **536430**      | 100%               | 50.2 %         |

22243 anusvAras distribute into m or n as per context.

Estimate : (p,b, s, S, h)/(p,b, s, S, h)+(k,g,c,j,T,D,t,d) \* 22243 ≈
(19475 + 879 + 13899 + 4618 + 26340 + 6841 + 6426 + 12472) / (Numerator
Sum + 34581 + 2460 + 31622 + 1177 + 10129 + 764 + 9638 + 274 + 10299 +
993 + 17422 + 424 + 31452 + 1976 +19706 + 5168) ≈ 90950/(90950+178085) ≈
0.34 \* 22243 ≈ 7520 m

22243-7520 ≈ 14723 n

### Eke vowels

[sections/Eke_char_distributions_vowels.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_char_distributions_vowels.md)

|            |           |           |                    |            |            |                 |                |
|------------|-----------|-----------|--------------------|------------|------------|-----------------|----------------|
| **Eke**    | **svara** | **count** | **modifier/kombu** | **count**  | **Total**  | **% of vowels** | **% of total** |
| **a**      | ಅ         | 8963      | ø                  | 237387     | 246350     | **46.56%**      | 23.42%         |
| **ø**      |           |           | ್                   | 59932      | 59932      | **11.33%**      | 5.70%          |
| **i**      | ಇ         | 1879      | ಿ                   | 54773      | 56652      | **10.71%**      | 5.39%          |
| **u**      | ಉ         | 3644      | ು                  | 45920      | 49564      | **9.37%**       | 4.71%          |
| **A**      | ಆ         | 3551      | ಾ                  | 36978      | 40529      | **7.66%**       | 3.85%          |
| **e**      | ಎ         | 1830      | ೆ                   | 32298      | 34128      | **6.45%**       | 3.24%          |
| **o**      | ಒ         | 1819      | ೊ                  | 9426       | 11245      | **2.13%**       | 1.07%          |
| **O**      | ಓ         | 422       | ೋ                  | 8686       | 9108       | **1.72%**       | 0.87%          |
| **E**      | ಏ         | 675       | ೇ                  | 7549       | 8224       | **1.55%**       | 0.78%          |
| **I**      | ಈ         | 305       | ೀ                  | 7035       | 7340       | **1.39%**       | 0.70%          |
| **U**      | ಊ         | 379       | ೂ                  | 5706       | 6085       | **1.15%**       | 0.58%          |
| **Totals** |           | **23467** |                    | **505690** | **529157** | 100%            | **49.8%**      |

ø or ್ reflects the number of ottakSaras as well as vowel-less endings.
Spoken kannada tends to have more schwa reductions than written kannada.

|        |     |     |     |      |      |
|--------|-----|-----|-----|------|------|
| **ay** | ಐ   | 221 | ೈ   | 2862 | 3083 |
| **av** | ಔ   | 127 | ೌ    | 1329 | 1456 |
| **x**  | ಋ   | 172 | ೃ   | 2301 | 2473 |

## ellara kannaDa ottakSaragaLu

About 365 of 1296 possible ottakSaras are actually used in a
comprehensive dictionary like Alar. Even there less than a 100 of them
have \>100 counts. About 4 symbols of formal kannaDa map to 1 symbol of
EK - which transliterates to a 2 letter combination in Eke.

Since each of the following combine with with all vowels and modifiers
(10 vowels + 1 anusvAra in EK, 16 vowels + 1 anusVara, 1 visarga + 2
other legacy combinators in kannaDa), its a large sample space indeed.
So only the ottaksharas are provided here. The ್ is omitted without loss
of generality for the kannaDa and EK akSaras.

About 12% of the consonants, and 6% of the total characters are
ottakSaras totalling to around 60k occurences. We speculate (without
concrete evidence) that about 26-27k out of 60k occurences in words
indicate native origin while the remaining indicate that they are
borrowed from samskxuta or elsewhere. Outside of these, words with
ottulis are almost always borrowed.

kannaDa tends to have the same consonant repeated in ottakSaras. Most
other combinations are from samskxta, persian or hindi.

When there are no aspirated vowels, they could still be borrowed (like
jana, dina) but presence of retroflex consonants (N, L, Z) or vowels (o
O, e E) that are distinguished in dravidian languages indicate native
origin. Presence of x (ಋ) is almost certain to be of samskxta origin.

There are cases where many words in samskxta are of draviDian origin,
typically agricultural and food crop related and/or words with retroflex
consonants. These are noted in references. Some of these words are
reborrowed into kannaDa from other languages. E.g. phala, khurci, gOdi,
pulAv, biriyAni, cash(from kAsu). Other borrowings from draviDian
languages are not commonly used in kannaDa e.g. chAval, brinjAl.

Also dictionaries are built out of scholarly discretion and may contain
more formal content than everyday speech. Character and word occurrence
in dictionaries are not indicative of actual usage.

## kannaDa ottakSaragaLu distributions

The following table contains a comprehensive distribution of all
ottakSara combinations that are found in the alar dictionary.

[ottakSaras_stats.md
](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/ottakSara_stats.md)

## ottakSaragaLu

Note: Read from Top to Bottom.

Also see the diagonal effect of ottakSaras repeating the primary akSara.
This is common in kannaDa and prAkxt. Having different letter
combinations is common in samskxta.

### vElAr

|     |        |          |        |         |        |         |     |     |     |     |
|-----|--------|----------|--------|---------|--------|---------|-----|-----|-----|-----|
|     | k      |          | kh     |         | g      |         | gh  |     | G   |     |
| k   | **ಕ್ಕ** | **2708** | ಖ್ಕ     | 0       | ಗ್ಕ     | 0       | ಘ್ಕ  | 0   | ಙ್ಕ  | 0   |
| kh  | ಕ್ಖ     | 21       | ಖ್ಖ     | 33      | ಗ್ಖ     | 0       | ಘ್ಖ  | 0   | ಙ್ಖ  | 0   |
| g   | ಕ್ಗ     | 0        | ಖ್ಗ     | 0       | **ಗ್ಗ** | **711** | ಘ್ಗ  | 0   | ಙ್ಗ  | 8   |
| gh  | ಕ್ಘ     | 0        | ಖ್ಘ     | 0       | ಗ್ಘ     | 12      | ಘ್ಘ  | 0   | ಙ್ಘ  | 0   |
| G   | ಕ್ಙ     | 0        | ಖ್ಙ     | 0       | ಗ್ಙ     | 0       | ಘ್ಙ  | 0   | ಙ್ಙ  | 0   |
| c   | ಕ್ಚ     | 12       | ಖ್ಚ     | 0       | ಗ್ಚ     | 0       | ಘ್ಚ  | 0   | ಙ್ಚ  | 0   |
| ch  | ಕ್ಛ     | 7        | ಖ್ಛ     | 0       | ಗ್ಛ     | 0       | ಘ್ಛ  | 0   | ಙ್ಛ  | 0   |
| j   | ಕ್ಜ     | 0        | ಖ್ಜ     | 0       | ಗ್ಜ     | 11      | ಘ್ಜ  | 0   | ಙ್ಜ  | 0   |
| jh  | ಕ್ಝ     | 0        | ಖ್ಝ     | 0       | ಗ್ಝ     | 0       | ಘ್ಝ  | 0   | ಙ್ಝ  | 0   |
| Y   | ಕ್ಞ     | 0        | ಖ್ಞ     | 0       | ಗ್ಞ     | 0       | ಘ್ಞ  | 0   | ಙ್ಞ  | 0   |
| T   | ಕ್ಟ     | 3        | ಖ್ಟ     | 0       | ಗ್ಟ     | 0       | ಘ್ಟ  | 0   | ಙ್ಟ  | 0   |
| Th  | ಕ್ಠ     | 0        | ಖ್ಠ     | 0       | ಗ್ಠ     | 0       | ಘ್ಠ  | 0   | ಙ್ಠ  | 0   |
| D   | ಕ್ಡ     | 0        | ಖ್ಡ     | 0       | ಗ್ಡ     | 2       | ಘ್ಡ  | 0   | ಙ್ಡ  | 0   |
| Dh  | ಕ್ಢ     | 0        | ಖ್ಢ     | 0       | ಗ್ಢ     | 0       | ಘ್ಢ  | 0   | ಙ್ಢ  | 0   |
| N   | ಕ್ಣ     | 0        | ಖ್ಣ     | 0       | ಗ್ಣ     | 6       | ಘ್ಣ  | 0   | ಙ್ಣ  | 0   |
| t   | **ಕ್ತ** | **867**  | ಖ್ತ     | 20      | ಗ್ತ     | 2       | ಘ್ತ  | 0   | ಙ್ತ  | 0   |
| th  | ಕ್ಥ     | 6        | ಖ್ಥ     | 0       | ಗ್ಥ     | 0       | ಘ್ಥ  | 0   | ಙ್ಥ  | 0   |
| d   | ಕ್ದ     | 6        | ಖ್ದ     | 0       | ಗ್ದ     | 18      | ಘ್ದ  | 0   | ಙ್ದ  | 0   |
| dh  | ಕ್ಧ     | 0        | ಖ್ಧ     | 0       | ಗ್ಧ     | 86      | ಘ್ಧ  | 0   | ಙ್ಧ  | 0   |
| n   | ಕ್ನ     | 2        | ಖ್ನ     | 0       | **ಗ್ನ** | **232** | ಘ್ನ  | 37  | ಙ್ನ  | 2   |
| p   | ಕ್ಪ     | 29       | ಖ್ಪ     | 0       | ಗ್ಪ     | 1       | ಘ್ಪ  | 0   | ಙ್ಪ  | 0   |
| ph  | ಕ್ಫ     | 0        | ಖ್ಫ     | 0       | ಗ್ಫ     | 0       | ಘ್ಫ  | 0   | ಙ್ಫ  | 0   |
| b   | ಕ್ಬ     | 1        | ಖ್ಬ     | 0       | ಗ್ಬ     | 10      | ಘ್ಬ  | 0   | ಙ್ಬ  | 0   |
| bh  | ಕ್ಭ     | 0        | ಖ್ಭ     | 0       | ಗ್ಭ     | 20      | ಘ್ಭ  | 0   | ಙ್ಭ  | 0   |
| m   | ಕ್ಮ     | 10       | ಖ್ಮ     | 0       | ಗ್ಮ     | 12      | ಘ್ಮ  | 0   | ಙ್ಮ  | 26  |
| y   | **ಕ್ಯ** | **124**  | **ಖ್ಯ** | **160** | **ಗ್ಯ** | **118** | ಘ್ಯ  | 19  | ಙ್ಯ  | 0   |
| r   | **ಕ್ರ** | **933**  | ಖ್ರ     | 1       | **ಗ್ರ** | **721** | ಘ್ರ  | 51  | ಙ್ರ  | 0   |
| Z   | ಕ್ಱ     | 0        | ಖ್ಱ     | 0       | ಗ್ಱ     | 0       | ಘ್ಱ  | 0   | ಙ್ಱ  | 0   |
| l   | **ಕ್ಲ** | **105**  | ಖ್ಲ     | 0       | ಗ್ಲ     | 24      | ಘ್ಲ  | 0   | ಙ್ಲ  | 0   |
| L   | ಕ್ಳ     | 1        | ಖ್ಳ     | 0       | ಗ್ಳ     | 0       | ಘ್ಳ  | 0   | ಙ್ಳ  | 0   |
| v   | ಕ್ವ     | 56       | ಖ್ವ     | 1       | ಗ್ವ     | 34      | ಘ್ವ  | 0   | ಙ್ವ  | 0   |
| S   | ಕ್ಶ     | 4        | ಖ್ಶ     | 0       | ಗ್ಶ     | 0       | ಘ್ಶ  | 0   | ಙ್ಶ  | 0   |
| Sh  | **ಕ್ಷ** | **2302** | ಖ್ಷ     | 0       | ಗ್ಷ     | 0       | ಘ್ಷ  | 0   | ಙ್ಷ  | 0   |
| s   | ಕ್ಸ     | 24       | ಖ್ಸ     | 0       | ಗ್ಸ     | 0       | ಘ್ಸ  | 0   | ಙ್ಸ  | 0   |
| h   | ಕ್ಹ     | 0        | ಖ್ಹ     | 0       | ಗ್ಹ     | 0       | ಘ್ಹ  | 0   | ಙ್ಹ  | 0   |
| R   | ಕ್ೞ     | 0        | ಖ್ೞ     | 0       | ಗ್ೞ     | 0       | ಘ್ೞ  | 0   | ಙ್ೞ  | 0   |

### palAhTal

|        |        |          |        |     |        |         |        |     |       |
|--------|--------|----------|--------|-----|--------|---------|--------|-----|-------|
|        | **c**  |          | **ch** |     | **j**  |         | **jh** |     | **Y** |
| **k**  | ಚ್ಕ     | 0        | ಛ್ಕ     | 0   | ಜ್ಕ     | 0       | ಝ್ಕ     | 0   | ಞ್ಕ    |
| **kh** | ಚ್ಖ     | 0        | ಛ್ಖ     | 0   | ಜ್ಖ     | 0       | ಝ್ಖ     | 0   | ಞ್ಖ    |
| **g**  | ಚ್ಗ     | 0        | ಛ್ಗ     | 0   | ಜ್ಗ     | 0       | ಝ್ಗ     | 0   | ಞ್ಗ    |
| **gh** | ಚ್ಘ     | 0        | ಛ್ಘ     | 0   | ಜ್ಘ     | 0       | ಝ್ಘ     | 0   | ಞ್ಘ    |
| **G**  | ಚ್ಙ     | 0        | ಛ್ಙ     | 0   | ಜ್ಙ     | 0       | ಝ್ಙ     | 0   | ಞ್ಙ    |
| **c**  | **ಚ್ಚ** | **1477** | ಛ್ಚ     | 0   | ಜ್ಚ     | 0       | ಝ್ಚ     | 0   | ಞ್ಚ    |
| **ch** | **ಚ್ಛ** | **373**  | ಛ್ಛ     | 1   | ಜ್ಛ     | 0       | ಝ್ಛ     | 0   | ಞ್ಛ    |
| **j**  | ಚ್ಜ     | 0        | ಛ್ಜ     | 0   | **ಜ್ಜ** | **669** | ಝ್ಜ     | 0   | ಞ್ಜ    |
| **jh** | ಚ್ಝ     | 0        | ಛ್ಝ     | 0   | ಜ್ಝ     | 18      | ಝ್ಝ     | 3   | ಞ್ಝ    |
| **Y**  | ಚ್ಞ     | 0        | ಛ್ಞ     | 0   | **ಜ್ಞ** | **634** | ಝ್ಞ     | 0   | ಞ್ಞ    |
| **T**  | ಚ್ಟ     | 0        | ಛ್ಟ     | 0   | ಜ್ಟ     | 0       | ಝ್ಟ     | 0   | ಞ್ಟ    |
| **Th** | ಚ್ಠ     | 0        | ಛ್ಠ     | 0   | ಜ್ಠ     | 0       | ಝ್ಠ     | 0   | ಞ್ಠ    |
| **D**  | ಚ್ಡ     | 0        | ಛ್ಡ     | 0   | ಜ್ಡ     | 0       | ಝ್ಡ     | 0   | ಞ್ಡ    |
| **Dh** | ಚ್ಢ     | 0        | ಛ್ಢ     | 0   | ಜ್ಢ     | 0       | ಝ್ಢ     | 0   | ಞ್ಢ    |
| **N**  | ಚ್ಣ     | 0        | ಛ್ಣ     | 0   | ಜ್ಣ     | 0       | ಝ್ಣ     | 0   | ಞ್ಣ    |
| **t**  | ಚ್ತ     | 0        | ಛ್ತ     | 0   | ಜ್ತ     | 0       | ಝ್ತ     | 0   | ಞ್ತ    |
| **th** | ಚ್ಥ     | 0        | ಛ್ಥ     | 0   | ಜ್ಥ     | 0       | ಝ್ಥ     | 0   | ಞ್ಥ    |
| **d**  | ಚ್ದ     | 0        | ಛ್ದ     | 0   | ಜ್ದ     | 1       | ಝ್ದ     | 0   | ಞ್ದ    |
| **dh** | ಚ್ಧ     | 0        | ಛ್ಧ     | 0   | ಜ್ಧ     | 0       | ಝ್ಧ     | 0   | ಞ್ಧ    |
| **n**  | ಚ್ನ     | 1        | ಛ್ನ     | 0   | ಜ್ನ     | 1       | ಝ್ನ     | 0   | ಞ್ನ    |
| **p**  | ಚ್ಪ     | 0        | ಛ್ಪ     | 0   | ಜ್ಪ     | 1       | ಝ್ಪ     | 0   | ಞ್ಪ    |
| **ph** | ಚ್ಫ     | 0        | ಛ್ಫ     | 0   | ಜ್ಫ     | 0       | ಝ್ಫ     | 0   | ಞ್ಫ    |
| **b**  | ಚ್ಬ     | 1        | ಛ್ಬ     | 0   | ಜ್ಬ     | 0       | ಝ್ಬ     | 0   | ಞ್ಬ    |
| **bh** | ಚ್ಭ     | 0        | ಛ್ಭ     | 0   | ಜ್ಭ     | 0       | ಝ್ಭ     | 0   | ಞ್ಭ    |
| **m**  | ಚ್ಮ     | 0        | ಛ್ಮ     | 0   | ಜ್ಮ     | 1       | ಝ್ಮ     | 0   | ಞ್ಮ    |
| **y**  | ಚ್ಯ     | 72       | ಛ್ಯ     | 2   | **ಜ್ಯ** | **214** | ಝ್ಯ     | 0   | ಞ್ಯ    |
| **r**  | ಚ್ರ     | 9        | ಛ್ರ     | 17  | ಜ್ರ     | 54      | ಝ್ರ     | 0   | ಞ್ರ    |
| **Z**  | ಚ್ಱ     | 0        | ಛ್ಱ     | 0   | ಜ್ಱ     | 0       | ಝ್ಱ     | 0   | ಞ್ಱ    |
| **l**  | ಚ್ಲ     | 0        | ಛ್ಲ     | 0   | ಜ್ಲ     | 0       | ಝ್ಲ     | 0   | ಞ್ಲ    |
| **L**  | ಚ್ಳ     | 0        | ಛ್ಳ     | 0   | ಜ್ಳ     | 0       | ಝ್ಳ     | 0   | ಞ್ಳ    |
| **v**  | ಚ್ವ     | 5        | ಛ್ವ     | 6   | **ಜ್ವ** | **151** | ಝ್ವ     | 0   | ಞ್ವ    |
| **S**  | ಚ್ಶ     | 0        | ಛ್ಶ     | 0   | ಜ್ಶ     | 0       | ಝ್ಶ     | 0   | ಞ್ಶ    |
| **Sh** | ಚ್ಷ     | 0        | ಛ್ಷ     | 0   | ಜ್ಷ     | 0       | ಝ್ಷ     | 0   | ಞ್ಷ    |
| **s**  | ಚ್ಸ     | 0        | ಛ್ಸ     | 0   | ಜ್ಸ     | 0       | ಝ್ಸ     | 0   | ಞ್ಸ    |
| **h**  | ಚ್ಹ     | 0        | ಛ್ಹ     | 0   | ಜ್ಹ     | 1       | ಝ್ಹ     | 0   | ಞ್ಹ    |

### reTrOfleks

|        |        |          |        |     |        |          |        |     |        |          |
|--------|--------|----------|--------|-----|--------|----------|--------|-----|--------|----------|
|        | **T**  |          | **Th** |     | **D**  |          | **Dh** |     | **N**  |          |
| **k**  | ಟ್ಕ     | 14       | ಠ್ಕ     | 0   | ಡ್ಕ     | 6        | ಢ್ಕ     | 0   | ಣ್ಕ     | 44       |
| **kh** | ಟ್ಖ     | 3        | ಠ್ಖ     | 0   | ಡ್ಖ     | 0        | ಢ್ಖ     | 0   | ಣ್ಖ     | 0        |
| **g**  | ಟ್ಗ     | 0        | ಠ್ಗ     | 0   | ಡ್ಗ     | 37       | ಢ್ಗ     | 0   | **ಣ್ಗ** | **104**  |
| **gh** | ಟ್ಘ     | 0        | ಠ್ಘ     | 0   | ಡ್ಘ     | 1        | ಢ್ಘ     | 0   | ಣ್ಘ     | 0        |
| **G**  | ಟ್ಙ     | 0        | ಠ್ಙ     | 0   | ಡ್ಙ     | 0        | ಢ್ಙ     | 0   | ಣ್ಙ     | 0        |
| **c**  | ಟ್ಚ     | 5        | ಠ್ಚ     | 0   | ಡ್ಚ     | 1        | ಢ್ಚ     | 0   | ಣ್ಚ     | 14       |
| **ch** | ಟ್ಛ     | 0        | ಠ್ಛ     | 0   | ಡ್ಛ     | 0        | ಢ್ಛ     | 0   | ಣ್ಛ     | 2        |
| **j**  | ಟ್ಜ     | 0        | ಠ್ಜ     | 0   | ಡ್ಜ     | 8        | ಢ್ಜ     | 0   | ಣ್ಜ     | 7        |
| **jh** | ಟ್ಝ     | 0        | ಠ್ಝ     | 0   | ಡ್ಝ     | 0        | ಢ್ಝ     | 0   | ಣ್ಝ     | 0        |
| **Y**  | ಟ್ಞ     | 0        | ಠ್ಞ     | 0   | ಡ್ಞ     | 0        | ಢ್ಞ     | 0   | ಣ್ಞ     | 0        |
| **T**  | **ಟ್ಟ** | **3756** | ಠ್ಟ     | 0   | ಡ್ಟ     | 0        | ಢ್ಟ     | 0   | ಣ್ಟ     | 0        |
| **Th** | ಟ್ಠ     | 15       | ಠ್ಠ     | 5   | ಡ್ಠ     | 0        | ಢ್ಠ     | 0   | ಣ್ಠ     | 0        |
| **D**  | ಟ್ಡ     | 0        | ಠ್ಡ     | 0   | **ಡ್ಡ** | **1132** | ಢ್ಡ     | 0   | ಣ್ಡ     | 0        |
| **Dh** | ಟ್ಢ     | 0        | ಠ್ಢ     | 0   | ಡ್ಢ     | 3        | ಢ್ಢ     | 0   | ಣ್ಢ     | 0        |
| **N**  | ಟ್ಣ     | 3        | ಠ್ಣ     | 0   | ಡ್ಣ     | 0        | ಢ್ಣ     | 0   | ಣ್ಣ     | **1169** |
| **t**  | ಟ್ತ     | 2        | ಠ್ತ     | 0   | ಡ್ತ     | 7        | ಢ್ತ     | 0   | ಣ್ತ     | 22       |
| **th** | ಟ್ಥ     | 0        | ಠ್ಥ     | 0   | ಡ್ಥ     | 0        | ಢ್ಥ     | 0   | ಣ್ಥ     | 0        |
| **d**  | ಟ್ದ     | 0        | ಠ್ದ     | 0   | ಡ್ದ     | 1        | ಢ್ದ     | 0   | ಣ್ದ     | 39       |
| **dh** | ಟ್ಧ     | 0        | ಠ್ಧ     | 0   | ಡ್ಧ     | 0        | ಢ್ಧ     | 0   | ಣ್ಧ     | 0        |
| **n**  | ಟ್ನ     | 3        | ಠ್ನ     | 0   | ಡ್ನ     | 3        | ಢ್ನ     | 0   | ಣ್ನ     | 4        |
| **p**  | ಟ್ಪ     | 14       | ಠ್ಪ     | 0   | ಡ್ಪ     | 1        | ಢ್ಪ     | 0   | ಣ್ಪ     | 66       |
| **ph** | ಟ್ಫ     | 0        | ಠ್ಫ     | 0   | ಡ್ಫ     | 0        | ಢ್ಫ     | 0   | ಣ್ಫ     | 0        |
| **b**  | ಟ್ಬ     | 0        | ಠ್ಬ     | 0   | ಡ್ಬ     | 2        | ಢ್ಬ     | 0   | ಣ್ಬ     | 55       |
| **bh** | ಟ್ಭ     | 0        | ಠ್ಭ     | 0   | ಡ್ಭ     | 4        | ಢ್ಭ     | 0   | ಣ್ಭ     | 1        |
| **m**  | ಟ್ಮ     | 0        | ಠ್ಮ     | 0   | ಡ್ಮ     | 6        | ಢ್ಮ     | 0   | ಣ್ಮ     | 98       |
| **y**  | ಟ್ಯ     | 52       | ಠ್ಯ     | 23  | ಡ್ಯ     | 31       | ಢ್ಯ     | 20  | **ಣ್ಯ** | **135**  |
| **r**  | ಟ್ರ     | 84       | ಠ್ರ     | 0   | ಡ್ರ     | 26       | ಢ್ರ     | 5   | ಣ್ರ     | 3        |
| **Z**  | ಟ್ಱ     | 0        | ಠ್ಱ     | 0   | ಡ್ಱ     | 0        | ಢ್ಱ     | 0   | ಣ್ಱ     | 0        |
| **l**  | ಟ್ಲ     | 32       | ಠ್ಲ     | 0   | ಡ್ಲ     | 22       | ಢ್ಲ     | 0   | ಣ್ಲ     | 0        |
| **L**  | ಟ್ಳ     | 2        | ಠ್ಳ     | 0   | ಡ್ಳ     | 1        | ಢ್ಳ     | 0   | ಣ್ಳ     | 0        |
| **v**  | ಟ್ವ     | 8        | ಠ್ವ     | 0   | ಡ್ವ     | 15       | ಢ್ವ     | 0   | ಣ್ವ     | 11       |
| **S**  | ಟ್ಶ     | 0        | ಠ್ಶ     | 0   | ಡ್ಶ     | 0        | ಢ್ಶ     | 0   | ಣ್ಶ     | 0        |
| **Sh** | ಟ್ಷ     | 0        | ಠ್ಷ     | 0   | ಡ್ಷ     | 0        | ಢ್ಷ     | 0   | ಣ್ಷ     | 0        |
| **s**  | ಟ್ಸ     | 2        | ಠ್ಸ     | 0   | ಡ್ಸ     | 3        | ಢ್ಸ     | 0   | ಣ್ಸ     | 12       |
| **h**  | ಟ್ಹ     | 1        | ಠ್ಹ     | 0   | ಡ್ಹ     | 0        | ಢ್ಹ     | 0   | ಣ್ಹ     | 0        |
| **R**  | ಟ್ೞ     | 0        | ಠ್ೞ     | 0   | ಡ್ೞ     | 0        | ಢ್ೞ     | 0   | ಣ್ೞ     | 0        |

### denTal

|        |        |          |        |     |        |          |        |         |        |          |
|--------|--------|----------|--------|-----|--------|----------|--------|---------|--------|----------|
|        | **t**  |          | **th** |     | **d**  |          | **dh** |         | **n**  |          |
| **k**  | **ತ್ಕ** | **232**  | ಥ್ಕ     | 0   | ದ್ಕ     | 0        | ಧ್ಕ     | 0       | ನ್ಕ     | 3        |
| **kh** | ತ್ಖ     | 5        | ಥ್ಖ     | 0   | ದ್ಖ     | 0        | ಧ್ಖ     | 0       | ನ್ಖ     | 0        |
| **g**  | ತ್ಗ     | 0        | ಥ್ಗ     | 0   | **ದ್ಗ** | **112**  | ಧ್ಗ     | 0       | ನ್ಗ     | 3        |
| **gh** | ತ್ಘ     | 0        | ಥ್ಘ     | 0   | ದ್ಘ     | 32       | ಧ್ಘ     | 0       | ನ್ಘ     | 0        |
| **G**  | ತ್ಙ     | 0        | ಥ್ಙ     | 0   | ದ್ಙ     | 0        | ಧ್ಙ     | 0       | ನ್ಙ     | 0        |
| **c**  | ತ್ಚ     | 0        | ಥ್ಚ     | 0   | ದ್ಚ     | 0        | ಧ್ಚ     | 0       | ನ್ಚ     | 0        |
| **ch** | ತ್ಛ     | 0        | ಥ್ಛ     | 0   | ದ್ಛ     | 0        | ಧ್ಛ     | 0       | ನ್ಛ     | 0        |
| **j**  | ತ್ಜ     | 0        | ಥ್ಜ     | 0   | ದ್ಜ     | 0        | ಧ್ಜ     | 0       | ನ್ಜ     | 0        |
| **jh** | ತ್ಝ     | 0        | ಥ್ಝ     | 0   | ದ್ಝ     | 0        | ಧ್ಝ     | 0       | ನ್ಝ     | 0        |
| **Y**  | ತ್ಞ     | 0        | ಥ್ಞ     | 0   | ದ್ಞ     | 0        | ಧ್ಞ     | 0       | ನ್ಞ     | 0        |
| **T**  | ತ್ಟ     | 0        | ಥ್ಟ     | 0   | ದ್ಟ     | 0        | ಧ್ಟ     | 0       | ನ್ಟ     | 0        |
| **Th** | ತ್ಠ     | 0        | ಥ್ಠ     | 0   | ದ್ಠ     | 0        | ಧ್ಠ     | 0       | ನ್ಠ     | 0        |
| **D**  | ತ್ಡ     | 0        | ಥ್ಡ     | 0   | ದ್ಡ     | 0        | ಧ್ಡ     | 0       | ನ್ಡ     | 0        |
| **Dh** | ತ್ಢ     | 0        | ಥ್ಢ     | 0   | ದ್ಢ     | 0        | ಧ್ಢ     | 0       | ನ್ಢ     | 0        |
| **N**  | ತ್ಣ     | 0        | ಥ್ಣ     | 0   | ದ್ಣ     | 0        | ಧ್ಣ     | 0       | ನ್ಣ     | 0        |
| **t**  | **ತ್ತ** | **3450** | ಥ್ತ     | 0   | ದ್ತ     | 0        | ಧ್ತ     | 0       | ನ್ತ     | 1        |
| **th** | ತ್ಥ     | 55       | ಥ್ಥ     | 0   | ದ್ಥ     | 0        | ಧ್ಥ     | 0       | ನ್ಥ     | 0        |
| **d**  | ತ್ದ     | 0        | ಥ್ದ     | 0   | **ದ್ದ** | **724**  | ಧ್ದ     | 0       | ನ್ದ     | 6        |
| **dh** | ತ್ಧ     | 0        | ಥ್ಧ     | 0   | **ದ್ಧ** | **708**  | ಧ್ಧ     | 0       | ನ್ಧ     | 0        |
| **n**  | **ತ್ನ** | **113**  | ಥ್ನ     | 0   | ದ್ನ     | 6        | ಧ್ನ     | 4       | **ನ್ನ** | **1462** |
| **p**  | **ತ್ಪ** | **186**  | ಥ್ಪ     | 0   | ದ್ಪ     | 0        | ಧ್ಪ     | 0       | ನ್ಪ     | 3        |
| **ph** | ತ್ಫ     | 7        | ಥ್ಫ     | 0   | ದ್ಫ     | 0        | ಧ್ಫ     | 0       | ನ್ಫ     | 0        |
| **b**  | ತ್ಬ     | 1        | ಥ್ಬ     | 0   | ದ್ಬ     | 25       | ಧ್ಬ     | 0       | ನ್ಬ     | 3        |
| **bh** | ತ್ಭ     | 0        | ಥ್ಭ     | 0   | ದ್ಭ     | 83       | ಧ್ಭ     | 0       | ನ್ಭ     | 0        |
| **m**  | **ತ್ಮ** | **333**  | ಥ್ಮ     | 0   | ದ್ಮ     | 94       | ಧ್ಮ     | 5       | **ನ್ಮ** | **239**  |
| **y**  | **ತ್ಯ** | **674**  | ಥ್ಯ     | 31  | **ದ್ಯ** | **627**  | **ಧ್ಯ** | **273** | **ನ್ಯ** | **519**  |
| **r**  | **ತ್ರ** | **2507** | ಥ್ರ     | 7   | **ದ್ರ** | **1211** | ಧ್ರ     | 85      | ನ್ರ     | 0        |
| **Z**  | ತ್ಱ     | 0        | ಥ್ಱ     | 0   | ದ್ಱ     | 0        | ಧ್ಱ     | 0       | ನ್ಱ     | 0        |
| **l**  | ತ್ಲ     | 1        | ಥ್ಲ     | 0   | ದ್ಲ     | 7        | ಧ್ಲ     | 0       | ನ್ಲ     | 0        |
| **L**  | ತ್ಳ     | 0        | ಥ್ಳ     | 0   | ದ್ಳ     | 0        | ಧ್ಳ     | 0       | ನ್ಳ     | 0        |
| **v**  | **ತ್ವ** | **743**  | ಥ್ವ     | 12  | ದ್ವ     | **427**  | **ಧ್ವ** | **205** | ನ್ವ     | 71       |
| **S**  | ತ್ಶ     | 0        | ಥ್ಶ     | 0   | ದ್ಶ     | 0        | ಧ್ಶ     | 0       | ನ್ಶ     | 2        |
| **Sh** | ತ್ಷ     | 0        | ಥ್ಷ     | 0   | ದ್ಷ     | 0        | ಧ್ಷ     | 0       | ನ್ಷ     | 4        |
| **s**  | **ತ್ಸ** | **303**  | ಥ್ಸ     | 0   | ದ್ಸ     | 0        | ಧ್ಸ     | 0       | ನ್ಸ     | 18       |
| **h**  | ತ್ಹ     | 0        | ಥ್ಹ     | 0   | ದ್ಹ     | 0        | ಧ್ಹ     | 0       | ನ್ಹ     | 3        |
| **R**  | ತ್ೞ     | 0        | ಥ್ೞ     | 0   | ದ್ೞ     | 0        | ಧ್ೞ     | 0       | ನ್ೞ     | 0        |

### labial

|        |        |          |        |     |        |         |        |         |        |          |
|--------|--------|----------|--------|-----|--------|---------|--------|---------|--------|----------|
|        | **p**  |          | **ph** |     | **b**  |         | **bh** |         | **m**  |          |
| **k**  | ಪ್ಕ     | 0        | ಫ್ಕ     | 0   | ಬ್ಕ     | 1       | ಭ್ಕ     | 0       | ಮ್ಕ     | 4        |
| **kh** | ಪ್ಖ     | 0        | ಫ್ಖ     | 0   | ಬ್ಖ     | 0       | ಭ್ಖ     | 0       | ಮ್ಖ     | 0        |
| **g**  | ಪ್ಗ     | 0        | ಫ್ಗ     | 0   | ಬ್ಗ     | 0       | ಭ್ಗ     | 0       | ಮ್ಗ     | 1        |
| **gh** | ಪ್ಘ     | 0        | ಫ್ಘ     | 0   | ಬ್ಘ     | 0       | ಭ್ಘ     | 0       | ಮ್ಘ     | 0        |
| **G**  | ಪ್ಙ     | 0        | ಫ್ಙ     | 0   | ಬ್ಙ     | 0       | ಭ್ಙ     | 0       | ಮ್ಙ     | 0        |
| **c**  | ಪ್ಚ     | 0        | ಫ್ಚ     | 0   | ಬ್ಚ     | 0       | ಭ್ಚ     | 0       | ಮ್ಚ     | 0        |
| **ch** | ಪ್ಛ     | 0        | ಫ್ಛ     | 0   | ಬ್ಛ     | 1       | ಭ್ಛ     | 0       | ಮ್ಛ     | 0        |
| **j**  | ಪ್ಜ     | 0        | ಫ್ಜ     | 0   | ಬ್ಜ     | 8       | ಭ್ಜ     | 0       | ಮ್ಜ     | 0        |
| **jh** | ಪ್ಝ     | 0        | ಫ್ಝ     | 0   | ಬ್ಝ     | 0       | ಭ್ಝ     | 0       | ಮ್ಝ     | 0        |
| **Y**  | ಪ್ಞ     | 0        | ಫ್ಞ     | 0   | ಬ್ಞ     | 0       | ಭ್ಞ     | 0       | ಮ್ಞ     | 0        |
| **T**  | ಪ್ಟ     | 0        | ಫ್ಟ     | 0   | ಬ್ಟ     | 0       | ಭ್ಟ     | 0       | ಮ್ಟ     | 0        |
| **Th** | ಪ್ಠ     | 0        | ಫ್ಠ     | 0   | ಬ್ಠ     | 0       | ಭ್ಠ     | 0       | ಮ್ಠ     | 0        |
| **D**  | ಪ್ಡ     | 0        | ಫ್ಡ     | 0   | ಬ್ಡ     | 0       | ಭ್ಡ     | 0       | ಮ್ಡ     | 0        |
| **Dh** | ಪ್ಢ     | 0        | ಫ್ಢ     | 0   | ಬ್ಢ     | 0       | ಭ್ಢ     | 0       | ಮ್ಢ     | 0        |
| **N**  | ಪ್ಣ     | 0        | ಫ್ಣ     | 0   | ಬ್ಣ     | 0       | ಭ್ಣ     | 0       | ಮ್ಣ     | 0        |
| **t**  | **ಪ್ತ** | **397**  | ಫ್ತ     | 20  | ಬ್ತ     | 1       | ಭ್ತ     | 0       | ಮ್ತ     | 2        |
| **th** | ಪ್ಥ     | 0        | ಫ್ಥ     | 0   | ಬ್ಥ     | 0       | ಭ್ಥ     | 0       | ಮ್ಥ     | 0        |
| **d**  | ಪ್ದ     | 0        | ಫ್ದ     | 0   | ಬ್ದ     | 76      | ಭ್ದ     | 0       | ಮ್ದ     | 0        |
| **dh** | ಪ್ಧ     | 0        | ಫ್ಧ     | 0   | ಬ್ಧ     | 60      | ಭ್ಧ     | 0       | ಮ್ಧ     | 0        |
| **n**  | ಪ್ನ     | 15       | ಫ್ನ     | 0   | ಬ್ನ     | 0       | ಭ್ನ     | 0       | ಮ್ನ     | 19       |
| **p**  | **ಪ್ಪ** | **1375** | ಫ್ಪ     | 0   | ಬ್ಪ     | 0       | ಭ್ಪ     | 0       | ಮ್ಪ     | 0        |
| **ph** | ಪ್ಫ     | 2        | ಫ್ಫ     | 0   | ಬ್ಫ     | 0       | ಭ್ಫ     | 0       | ಮ್ಫ     | 0        |
| **b**  | ಪ್ಬ     | 0        | ಫ್ಬ     | 0   | **ಬ್ಬ** | **953** | ಭ್ಬ     | 0       | ಮ್ಬ     | 0        |
| **bh** | ಪ್ಭ     | 0        | ಫ್ಭ     | 0   | ಬ್ಭ     | 3       | ಭ್ಭ     | 0       | ಮ್ಭ     | 0        |
| **m**  | ಪ್ಮ     | 0        | ಫ್ಮ     | 0   | ಬ್ಮ     | 0       | ಭ್ಮ     | 0       | **ಮ್ಮ** | **1041** |
| **y**  | ಪ್ಯ     | 52       | ಫ್ಯ     | 1   | ಬ್ಯ     | 34      | ಭ್ಯ     | 60      | **ಮ್ಯ** | **128**  |
| **r**  | **ಪ್ರ** | **2617** | ಫ್ರ     | 1   | **ಬ್ರ** | **232** | **ಭ್ರ** | **284** | ಮ್ರ     | 81       |
| **Z**  | ಪ್ಱ     | 0        | ಫ್ಱ     | 0   | ಬ್ಱ     | 0       | ಭ್ಱ     | 0       | ಮ್ಱ     | 0        |
| **l**  | ಪ್ಲ     | 62       | ಫ್ಲ     | 1   | ಬ್ಲ     | 7       | ಭ್ಲ     | 0       | ಮ್ಲ     | 64       |
| **L**  | ಪ್ಳ     | 0        | ಫ್ಳ     | 0   | ಬ್ಳ     | 2       | ಭ್ಳ     | 0       | ಮ್ಳ     | 0        |
| **v**  | ಪ್ವ     | 0        | ಫ್ವ     | 0   | ಬ್ವ     | 0       | ಭ್ವ     | 1       | ಮ್ವ     | 0        |
| **S**  | ಪ್ಶ     | 0        | ಫ್ಶ     | 0   | ಬ್ಶ     | 0       | ಭ್ಶ     | 0       | ಮ್ಶ     | 0        |
| **Sh** | ಪ್ಷ     | 0        | ಫ್ಷ     | 0   | ಬ್ಷ     | 0       | ಭ್ಷ     | 0       | ಮ್ಷ     | 0        |
| **s**  | ಪ್ಸ     | 24       | ಫ್ಸ     | 0   | ಬ್ಸ     | 0       | ಭ್ಸ     | 0       | ಮ್ಸ     | 0        |
| **h**  | ಪ್ಹ     | 0        | ಫ್ಹ     | 0   | ಬ್ಹ     | 1       | ಭ್ಹ     | 0       | ಮ್ಹ     | 0        |
| **R**  | ಪ್ೞ     | 0        | ಫ್ೞ     | 0   | ಬ್ೞ     | 0       | ಭ್ೞ     | 0       | ಮ್ೞ     | 0        |

### unordered

|        |        |         |        |          |       |     |        |         |
|--------|--------|---------|--------|----------|-------|-----|--------|---------|
|        | **y**  |         | **r**  |          | **R** |     | **v**  |         |
| **k**  | ಯ್ಕ     | 69      | **ರ್ಕ** | **429**  | ಱ್ಕ    | 0   | ವ್ಕ     | 0       |
| **kh** | ಯ್ಖ     | 0       | ರ್ಖ     | 22       | ಱ್ಖ    | 0   | ವ್ಖ     | 0       |
| **g**  | ಯ್ಗ     | 87      | **ರ್ಗ** | **618**  | ಱ್ಗ    | 0   | ವ್ಗ     | 0       |
| **gh** | ಯ್ಘ     | 0       | ರ್ಘ     | 85       | ಱ್ಘ    | 0   | ವ್ಘ     | 0       |
| **G**  | ಯ್ಙ     | 0       | ರ್ಙ     | 8        | ಱ್ಙ    | 0   | ವ್ಙ     | 0       |
| **c**  | ಯ್ಚ     | 7       | **ರ್ಚ** | **288**  | ಱ್ಚ    | 0   | ವ್ಚ     | 0       |
| **ch** | ಯ್ಛ     | 0       | ರ್ಛ     | 24       | ಱ್ಛ    | 0   | ವ್ಛ     | 0       |
| **j**  | ಯ್ಜ     | 3       | **ರ್ಜ** | **326**  | ಱ್ಜ    | 0   | ವ್ಜ     | 0       |
| **jh** | ಯ್ಝ     | 0       | ರ್ಝ     | 9        | ಱ್ಝ    | 0   | ವ್ಝ     | 0       |
| **Y**  | ಯ್ಞ     | 0       | ರ್ಞ     | 1        | ಱ್ಞ    | 0   | ವ್ಞ     | 0       |
| **T**  | ಯ್ಟ     | 0       | ರ್ಟ     | 12       | ಱ್ಟ    | 0   | ವ್ಟ     | 0       |
| **Th** | ಯ್ಠ     | 0       | ರ್ಠ     | 0        | ಱ್ಠ    | 0   | ವ್ಠ     | 0       |
| **D**  | ಯ್ಡ     | 0       | ರ್ಡ     | 8        | ಱ್ಡ    | 0   | ವ್ಡ     | 0       |
| **Dh** | ಯ್ಢ     | 0       | ರ್ಢ     | 0        | ಱ್ಢ    | 0   | ವ್ಢ     | 0       |
| **N**  | ಯ್ಣ     | 0       | **ರ್ಣ** | **577**  | ಱ್ಣ    | 0   | ವ್ಣ     | 0       |
| **t**  | ಯ್ತ     | 84      | **ರ್ತ** | **854**  | ಱ್ತ    | 1   | ವ್ತ     | 2       |
| **th** | ಯ್ಥ     | 0       | **ರ್ಥ** | **397**  | ಱ್ಥ    | 0   | ವ್ಥ     | 0       |
| **d**  | ಯ್ದ     | 79      | **ರ್ದ** | **472**  | ಱ್ದ    | 0   | ವ್ದ     | 0       |
| **dh** | ಯ್ಧ     | 1       | **ರ್ಧ** | **236**  | ಱ್ಧ    | 0   | ವ್ಧ     | 0       |
| **n**  | ಯ್ನ     | 15      | **ರ್ನ** | **111**  | ಱ್ನ    | 0   | ವ್ನ     | 0       |
| **p**  | ಯ್ಪ     | 18      | **ರ್ಪ** | **378**  | ಱ್ಪ    | 1   | ವ್ಪ     | 0       |
| **ph** | ಯ್ಫ     | 0       | ರ್ಫ     | 15       | ಱ್ಫ    | 0   | ವ್ಫ     | 0       |
| **b**  | ಯ್ಬ     | 20      | **ರ್ಬ** | **263**  | ಱ್ಬ    | 0   | ವ್ಬ     | 0       |
| **bh** | ಯ್ಭ     | 0       | **ರ್ಭ** | **252**  | ಱ್ಭ    | 0   | ವ್ಭ     | 0       |
| **m**  | ಯ್ಮ     | 52      | **ರ್ಮ** | **799**  | ಱ್ಮ    | 0   | ವ್ಮ     | 1       |
| **y**  | **ಯ್ಯ** | **283** | **ರ್ಯ** | **627**  | ಱ್ಯ    | 0   | **ವ್ಯ** | **796** |
| **r**  | ಯ್ರ     | 6       | ರ್ರ     | 52       | ಱ್ರ    | 0   | **ವ್ರ** | **180** |
| **Z**  | ಯ್ಱ     | 0       | ರ್ಱ     | 0        | ಱ್ಱ    | 0   | ವ್ಱ     | 0       |
| **l**  | ಯ್ಲ     | 72      | ರ್ಲ     | 81       | ಱ್ಲ    | 0   | ವ್ಲ     | 0       |
| **L**  | ಯ್ಳ     | 0       | ರ್ಳ     | 0        | ಱ್ಳ    | 0   | ವ್ಳ     | 0       |
| **v**  | ಯ್ವ     | 53      | **ರ್ವ** | **1063** | ಱ್ವ    | 0   | **ವ್ವ** | **168** |
| **S**  | ಯ್ಶ     | 1       | **ರ್ಶ** | **201**  | ಱ್ಶ    | 0   | ವ್ಶ     | 0       |
| **Sh** | ಯ್ಷ     | 0       | **ರ್ಷ** | **222**  | ಱ್ಷ    | 0   | ವ್ಷ     | 0       |
| **s**  | **ಯ್ಸ** | **138** | ರ್ಸ     | 24       | ಱ್ಸ    | 0   | ವ್ಸ     | 0       |
| **h**  | ಯ್ಹ     | 3       | ರ್ಹ     | 93       | ಱ್ಹ    | 0   | ವ್ಹ     | 0       |
| **R**  | ಯ್ೞ     | 0       | ರ್ೞ     | 0        | ಱ್ೞ    | 0   | ವ್ೞ     | 0       |

|        |        |          |        |          |        |         |
|--------|--------|----------|--------|----------|--------|---------|
|        | **l**  |          | **L**  |          | **Z**  |         |
| **k**  | **ಲ್ಕ** | **120**  | **ಳ್ಕ** | **145**  | ೞ್ಕ     | 91      |
| **kh** | ಲ್ಖ     | 0        | ಳ್ಖ     | 0        | ೞ್ಖ     | 0       |
| **g**  | **ಲ್ಗ** | **173**  | **ಳ್ಗ** | **173**  | ೞ್ಗ     | 66      |
| **gh** | ಲ್ಘ     | 0        | ಳ್ಘ     | 0        | ೞ್ಘ     | 0       |
| **G**  | ಲ್ಙ     | 0        | ಳ್ಙ     | 0        | ೞ್ಙ     | 0       |
| **c**  | ಲ್ಚ     | 22       | ಳ್ಚ     | 36       | ೞ್ಚ     | 25      |
| **ch** | ಲ್ಛ     | 2        | ಳ್ಛ     | 0        | ೞ್ಛ     | 1       |
| **j**  | ಲ್ಜ     | 3        | ಳ್ಜ     | 4        | ೞ್ಜ     | 3       |
| **jh** | ಲ್ಝ     | 0        | ಳ್ಝ     | 0        | ೞ್ಝ     | 0       |
| **Y**  | ಲ್ಞ     | 0        | ಳ್ಞ     | 0        | ೞ್ಞ     | 0       |
| **T**  | ಲ್ಟ     | 13       | ಳ್ಟ     | 2        | ೞ್ಟ     | 0       |
| **Th** | ಲ್ಠ     | 0        | ಳ್ಠ     | 0        | ೞ್ಠ     | 0       |
| **D**  | ಲ್ಡ     | 2        | ಳ್ಡ     | 0        | ೞ್ಡ     | 0       |
| **Dh** | ಲ್ಢ     | 0        | ಳ್ಢ     | 0        | ೞ್ಢ     | 0       |
| **N**  | ಲ್ಣ     | 0        | ಳ್ಣ     | 0        | ೞ್ಣ     | 0       |
| **t**  | ಲ್ತ     | 42       | **ಳ್ತ** | **117**  | **ೞ್ತ** | **108** |
| **th** | ಲ್ಥ     | 0        | ಳ್ಥ     | 0        | ೞ್ಥ     | 1       |
| **d**  | ಲ್ದ     | 64       | ಳ್ದ     | 54       | ೞ್ದ     | 32      |
| **dh** | ಲ್ಧ     | 0        | ಳ್ಧ     | 0        | ೞ್ಧ     | 0       |
| **n**  | ಲ್ನ     | 19       | ಳ್ನ     | 24       | ೞ್ನ     | 4       |
| **p**  | **ಲ್ಪ** | **254**  | ಳ್ಪ     | 84       | ೞ್ಪ     | 22      |
| **ph** | ಲ್ಫ     | 6        | ಳ್ಫ     | 0        | ೞ್ಫ     | 0       |
| **b**  | ಲ್ಬ     | 26       | ಳ್ಬ     | 12       | ೞ್ಬ     | 8       |
| **bh** | ಲ್ಭ     | 7        | ಳ್ಭ     | 0        | ೞ್ಭ     | 0       |
| **m**  | **ಲ್ಮ** | **133**  | ಳ್ಮ     | 82       | ೞ್ಮ     | 17      |
| **y**  | **ಲ್ಯ** | **185**  | ಳ್ಯ     | 22       | ೞ್ಯ     | 0       |
| **r**  | ಲ್ರ     | 2        | ಳ್ರ     | 0        | ೞ್ರ     | 0       |
| **Z**  | ಲ್ಱ     | 0        | ಳ್ಱ     | 0        | ೞ್ಱ     | 0       |
| **l**  | **ಲ್ಲ** | **1923** | ಳ್ಲ     | 1        | ೞ್ಲ     | 0       |
| **L**  | ಲ್ಳ     | 0        | **ಳ್ಳ** | **1414** | ೞ್ಳ     | 0       |
| **v**  | **ಲ್ವ** | **189**  | **ಳ್ವ** | **131**  | ೞ್ವ     | 17      |
| **S**  | ಲ್ಶ     | 0        | ಳ್ಶ     | 0        | ೞ್ಶ     | 0       |
| **Sh** | ಲ್ಷ     | 0        | ಳ್ಷ     | 0        | ೞ್ಷ     | 0       |
| **s**  | ಲ್ಸ     | 11       | ಳ್ಸ     | 1        | ೞ್ಸ     | 1       |
| **h**  | ಲ್ಹ     | 6        | ಳ್ಹ     | 0        | ೞ್ಹ     | 0       |
| **R**  | ಲ್ೞ     | 0        | ಳ್ೞ     | 0        | ೞ್ೞ     | 0       |

|        |       |         |        |          |       |          |       |         |
|--------|-------|---------|--------|----------|-------|----------|-------|---------|
|        | **S** |         | **Sh** |          | **s** |          | **h** |         |
| **k**  | ಶ್ಕ    | 0       | ಷ್ಕ     | **214**  | ಸ್ಕ    | **172**  | ಹ್ಕ    | 0       |
| **kh** | ಶ್ಖ    | 0       | ಷ್ಖ     | 2        | ಸ್ಖ    | 33       | ಹ್ಖ    | 0       |
| **g**  | ಶ್ಗ    | 0       | ಷ್ಗ     | 0        | ಸ್ಗ    | 0        | ಹ್ಗ    | 0       |
| **gh** | ಶ್ಘ    | 0       | ಷ್ಘ     | 0        | ಸ್ಘ    | 0        | ಹ್ಘ    | 0       |
| **G**  | ಶ್ಙ    | 0       | ಷ್ಙ     | 0        | ಸ್ಙ    | 0        | ಹ್ಙ    | 0       |
| **c**  | ಶ್ಚ    | **139** | ಷ್ಚ     | 0        | ಸ್ಚ    | 0        | ಹ್ಚ    | 0       |
| **ch** | ಶ್ಛ    | 4       | ಷ್ಛ     | 0        | ಸ್ಛ    | 0        | ಹ್ಛ    | 0       |
| **j**  | ಶ್ಜ    | 0       | ಷ್ಜ     | 0        | ಸ್ಜ    | 0        | ಹ್ಜ    | 0       |
| **jh** | ಶ್ಝ    | 0       | ಷ್ಝ     | 0        | ಸ್ಝ    | 0        | ಹ್ಝ    | 0       |
| **Y**  | ಶ್ಞ    | 0       | ಷ್ಞ     | 0        | ಸ್ಞ    | 0        | ಹ್ಞ    | 1       |
| **T**  | ಶ್ಟ    | 0       | ಷ್ಟ     | **1015** | ಸ್ಟ    | 16       | ಹ್ಟ    | 0       |
| **Th** | ಶ್ಠ    | 0       | ಷ್ಠ     | **345**  | ಸ್ಠ    | 0        | ಹ್ಠ    | 0       |
| **D**  | ಶ್ಡ    | 0       | ಷ್ಡ     | 0        | ಸ್ಡ    | 0        | ಹ್ಡ    | 0       |
| **Dh** | ಶ್ಢ    | 0       | ಷ್ಢ     | 0        | ಸ್ಢ    | 0        | ಹ್ಢ    | 0       |
| **N**  | ಶ್ಣ    | 0       | ಷ್ಣ     | **187**  | ಸ್ಣ    | 0        | ಹ್ಣ    | 3       |
| **t**  | ಶ್ತ    | 1       | ಷ್ತ     | 0        | ಸ್ತ    | **1493** | ಹ್ತ    | 0       |
| **th** | ಶ್ಥ    | 0       | ಷ್ಥ     | 0        | ಸ್ಥ    | **671**  | ಹ್ಥ    | 0       |
| **d**  | ಶ್ದ    | 0       | ಷ್ದ     | 0        | ಸ್ದ    | 0        | ಹ್ದ    | 0       |
| **dh** | ಶ್ಧ    | 1       | ಷ್ಧ     | 0        | ಸ್ಧ    | 0        | ಹ್ಧ    | 0       |
| **n**  | ಶ್ನ    | 27      | ಷ್ನ     | 0        | ಸ್ನ    | 78       | ಹ್ನ    | 54      |
| **p**  | ಶ್ಪ    | 0       | ಷ್ಪ     | **140**  | ಸ್ಪ    | **128**  | ಹ್ಪ    | 0       |
| **ph** | ಶ್ಫ    | 0       | ಷ್ಫ     | 7        | ಸ್ಫ    | **121**  | ಹ್ಫ    | 0       |
| **b**  | ಶ್ಬ    | 0       | ಷ್ಬ     | 0        | ಸ್ಬ    | 0        | ಹ್ಬ    | 0       |
| **bh** | ಶ್ಭ    | 0       | ಷ್ಭ     | 0        | ಸ್ಭ    | 0        | ಹ್ಭ    | 0       |
| **m**  | ಶ್ಮ    | 49      | ಷ್ಮ     | **141**  | ಸ್ಮ    | **158**  | ಹ್ಮ    | **184** |
| **y**  | ಶ್ಯ    | **139** | ಷ್ಯ     | **138**  | ಸ್ಯ    | **184**  | ಹ್ಯ    | **109** |
| **r**  | ಶ್ರ    | **569** | ಷ್ರ     | 7        | ಸ್ರ    | **132**  | ಹ್ರ    | 36      |
| **Z**  | ಶ್ಱ    | 0       | ಷ್ಱ     | 0        | ಸ್ಱ    | 0        | ಹ್ಱ    | 0       |
| **l**  | ಶ್ಲ    | 78      | ಷ್ಲ     | 0        | ಸ್ಲ    | 11       | ಹ್ಲ    | 10      |
| **L**  | ಶ್ಳ    | 0       | ಷ್ಳ     | 0        | ಸ್ಳ    | 0        | ಹ್ಳ    | 0       |
| **v**  | ಶ್ವ    | **385** | ಷ್ವ     | 25       | ಸ್ವ    | **546**  | ಹ್ವ    | 68      |
| **S**  | ಶ್ಶ    | 60      | ಷ್ಶ     | 0        | ಸ್ಶ    | 0        | ಹ್ಶ    | 0       |
| **Sh** | ಶ್ಷ    | 0       | ಷ್ಷ     | 10       | ಸ್ಷ    | 0        | ಹ್ಷ    | 0       |
| **s**  | ಶ್ಸ    | 0       | ಷ್ಸ     | 0        | ಸ್ಸ    | **207**  | ಹ್ಸ    | 0       |
| **h**  | ಶ್ಹ    | 0       | ಷ್ಹ     | 0        | ಸ್ಹ    | 0        | ಹ್ಹ    | 0       |
| **R**  | ಶ್ೞ    | 0       | ಷ್ೞ     | 0        | ಸ್ೞ    | 0        | ಹ್ೞ    | 0       |

## Top 100 ottakSaras

The below table has character counts for ottakSaras that occur 100 or
more times in alar. The table also shows mapping from formal to ek
ottaksaras and its counts as well.

[sections/Eke_ottakSaras_100_or_more.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_ottakSaras_100_or_more.md)

The below table summarizes the spread of ottakSaras in kannaDa and EK.
The top 100/1296 account for an overwhelming 91% of all ottakSaras in
kannaDa. The top 100/441 account for 94% of all ottakSaras.

Given that ottakSaras form 6% of the total characters (12% of the
consonants), we can see why obscure combinations and sparseness of the
permutations between characters can cause a large number of symbols
which are only rarely encountered. Using Eke automatically obviates the
need to recognize an entire parallel scheme of characters. As long as
ottakSaras are used, the following spread of frequencies will make it
hard to simplify them.

Doubled characters form about 38% of ottakSaras. Using kannaDa native
words or the process of tadBavization of foreign words can also simplify
these permutations but not eliminate the need for learning 2 symbol sets
for consonants.

|         |        |        |        |        |        |
|---------|--------|--------|--------|--------|--------|
| Top x   | 100    | 50     | 25     | 10     | 5      |
| kannaDa | 90.84% | 76.89% | 57.11% | 34.64% | 21.99% |
| EK      | 94.07% | 82.06% | 61.50% | 35.84% | 21.99% |

|     |                   |       |      |          |       |                       |                           |
|-----|-------------------|-------|------|----------|-------|-----------------------|---------------------------|
| Num | kannaDa ottakSara | count | Eke  | Eke(ek)  | count | "ellara kannada" / ek | Likely kannaDa / samskxta |
| 1   | ಟ್ಟ                | 3756  | TT   | TT       | 3776  | ಟ್ಟ                    | kannaDa                   |
| 2   | ತ್ತ                | 3450  | tt   | tt       | 3505  | ತ್ತ                    | kannaDa                   |
| 3   | ಕ್ಕ                | 2708  | kk   | kk       | 2762  | ಕ್ಕ                    | kannaDa                   |
| 4   | ಪ್ರ                | 2617  | pr   | pr       | 2618  | ಪ್ರ                    | samskxta                  |
| 5   | ತ್ರ                | 2507  | tr   | tr       | 2514  | ತ್ರ                    | samskxta                  |
| 6   | ಕ್ಷ                | 2302  | kSh  | **kS**   | 2306  | **ಕ್ಶ**                | samskxtA                  |
| 7   | ಸ್ತ                | 1493  | st   | st       | 2164  | ಸ್ತ                    | samskxta                  |
| 8   | ಲ್ಲ                | 1923  | ll   | ll       | 1923  | ಲ್ಲ                    | kannaDa                   |
| 9   | ಚ್ಚ                | 1477  | cc   | cc       | 1850  | ಚ್ಚ                    | kannaDa                   |
| 10  | ನ್ನ                | 1462  | nn   | nn       | 1462  | ನ್ನ                    | kannaDa                   |
| 11  | ದ್ದ                | 724   | dd   | dd       | 1739  | ದ್ದ                    | kannaDa                   |
| 12  | ಳ್ಳ                | 1414  | LL   | LL       | 1414  | ಳ್ಳ                    | kannaDa                   |
| 13  | ಪ್ಪ                | 1375  | pp   | pp       | 1375  | ಪ್ಪ                    | kannaDa                   |
| 14  | ಷ್ಟ                | 1015  | ShT  | **ST**   | 1412  | **ಶ್ಟ**                | samskxta                  |
| 15  | ರ್ತ                | 854   | rt   | rt       | 1423  | **ರ್‌ತ**                | samskxta                  |
| 16  | ದ್ರ                | 1211  | dr   | dr       | 1211  | ದ್ರ                    | samskxta                  |
| 17  | ಣ್ಣ                | 1169  | NN   | NN       | 1169  | ಣ್ಣ                    | kannaDa                   |
| 18  | ಡ್ಡ                | 1132  | DD   | DD       | 1132  | ಡ್ಡ                    | samskxta                  |
| 19  | ರ್ವ                | 1063  | rv   | rv       | 1063  | **ರ್‌ವ**                | samskxta                  |
| 20  | ಮ್ಮ                | 1041  | mm   | mm       | 1041  | ಮ್ಮ                    | kannaDa                   |
| 21  | ಬ್ಬ                | 953   | bb   | bb       | 953   | ಬ್ಬ                    | kannaDa                   |
| 22  | ಕ್ರ                | 933   | kr   | kr       | 933   | ಕ್ರ                    | samskxta                  |
| 23  | ದ್ಯ                | 627   | dy   | dy       | 1024  | ದ್ಯ                    | samskxta                  |
| 24  | ಕ್ತ                | 867   | kt   | kt       | 867   | ಕ್ತ                    | samskxta                  |
| 25  | ರ್ಮ                | 799   | rm   | rm       | 799   | **ರ್‌ಮ**                | samskxta                  |
| 26  | ವ್ಯ                | 796   | vy   | vy       | 796   | ವ್ಯ                    | samskxta                  |
| 27  | ತ್ವ                | 743   | tv   | tv       | 743   | ತ್ವ                    | samskxta                  |
| 28  | ಗ್ರ                | 721   | gr   | gr       | 721   | ಗ್ರ                    | samskxta                  |
| 29  | ಗ್ಗ                | 711   | gg   | gg       | 711   | ಗ್ಗ                    | kannaDa                   |
| 30  | ರ್ದ                | 472   | rd   | rd       | 798   | **ರ್‌ದ**                | samskxta                  |
| 31  | ತ್ಯ                | 674   | ty   | ty       | 674   | ತ್ಯ                    | samskxta                  |
| 32  | ಜ್ಜ                | 669   | jj   | jj       | 669   | ಜ್ಜ                    | kannaDa                   |
| 33  | ಜ್ಞ                | 634   | jY   | gy       | 634   | ಗ್ಯ                    | samskxta                  |
| 34  | ದ್ವ                | 427   | dv   | dv       | 641   | ದ್ವ                    | kannaDa                   |
| 35  | ರ್ಯ                | 627   | ry   | ry       | 627   | **ರ್‌ಯ**                | samskxta                  |
| 36  | ರ್ಗ                | 618   | rg   | rg       | 618   | **ರ್‌ಗ**                | samskxta                  |
| 37  | ರ್ಣ                | 577   | rN   | rN       | 577   | **ರ್‌ಣ**                | samskxta/kannaDa          |
| 38  | ಶ್ರ                | 569   | Sr   | **Sr**   | 569   | **ಶ್ರ**                | samskxta                  |
| 39  | ಸ್ವ                | 546   | sv   | sv       | 546   | ಸ್ವ                    | samskxta                  |
| 40  | ನ್ಯ                | 519   | ny   | ny       | 519   | ನ್ಯ                    | samskxta                  |
| 41  | ಭ್ರ                | 284   | bhr  | **br**   | 587   | **ಬ್ರ**                | samskxta                  |
| 42  | ರ್ಬ                | 263   | rb   | rb       | 485   | **ರ್‌ಬ**                | samskxta                  |
| 43  | ರ್ಕ                | 429   | rk   | rk       | 429   | **ರ್‌ಕ**                | samskxta                  |
| 44  | ರ್ಷ                | 222   | rSh  | **rS**   | 555   | **ರ್‌ಶ**                | samskxta                  |
| 45  | ಪ್ತ                | 397   | pt   | pt       | 397   | ಪ್ತ                    | samskxta                  |
| 46  | ಶ್ವ                | 385   | Sv   | Sv       | 385   | **ಶ್ವ**                | samskxta                  |
| 47  | ರ್ಪ                | 378   | rp   | rp       | 378   | **ರ್‌ಪ**                | samskxta                  |
| 48  | ಷ್ಠ                | 345   | ShTh | **ST**   | 345   | **ಶ್ಟ**                | samskxta                  |
| 49  | ತ್ಮ                | 333   | tm   | tm       | 333   | ತ್ಮ                    | samskxta                  |
| 50  | ರ್ಜ                | 326   | rj   | rj       | 326   | **ರ್‌ಜ**                | samskxta                  |
| 51  | ತ್ಸ                | 303   | ts   | ts       | 303   | ತ್ಸ                    | samskxta                  |
| 52  | ರ್ಚ                | 288   | rc   | rc       | 288   | **ರ್‌ಚ**                | samskxta                  |
| 53  | ಖ್ಯ                | 160   | khy  | ky       | 340   | ಕ್ಯ                    | samskxta                  |
| 54  | ಯ್ಯ                | 283   | yy   | yy       | 283   | ಯ್ಯ                    | kannaDa                   |
| 55  | ಲ್ಪ                | 254   | lp   | lp       | 254   | ಲ್ಪ                    | samskxta/kannaDa          |
| 56  | ಸ್ಪ                | 128   | sp   | sp       | 360   | ಸ್ಪ                    | samskxta/kannaDa          |
| 57  | ನ್ಮ                | 239   | nm   | nm       | 239   | ನ್ಮ                    | samskxta                  |
| 58  | ಗ್ನ                | 232   | gn   | gn       | 232   | ಗ್ನ                    | samskxta                  |
| 59  | ತ್ಕ                | 232   | tk   | tk       | 232   | ತ್ಕ                    | samskxta                  |
| 60  | ಜ್ಯ                | 214   | jy   | jy       | 214   | ಜ್ಯ                    | samskxta                  |
| 61  | ಷ್ಕ                | 214   | Shk  | **Sk**   | 214   | **ಶ್ಕ**                | samskxta                  |
| 62  | ಸ್ಸ                | 207   | ss   | ss       | 207   | ಸ್ಸ                    | kannaDa                   |
| 63  | ಲ್ವ                | 189   | lv   | lv       | 189   | ಲ್ವ                    | samskxta/kannaDa          |
| 64  | ಷ್ಣ                | 187   | ShN  | **SN**   | 187   | **ಶ್ಣ**                | samskxta                  |
| 65  | ತ್ಪ                | 186   | tp   | tp       | 186   | ತ್ಪ                    | samskxta                  |
| 66  | ಲ್ಯ                | 185   | ly   | ly       | 185   | ಲ್ಯ                    | samskxta                  |
| 67  | ಸ್ಯ                | 184   | sy   | sy       | 184   | ಸ್ಯ                    | samskxta                  |
| 68  | ಹ್ಮ                | 184   | hm   | hm       | 184   | ಹ್ಮ                    | samskxta                  |
| 69  | ವ್ರ                | 180   | vr   | vr       | 180   | ವ್ರ                    | samskxta                  |
| 70  | ಲ್ಗ                | 173   | lg   | lg       | 173   | ಲ್ಗ                    | kannaDa                   |
| 71  | ಳ್ಗ                | 173   | Lg   | Lg       | 173   | ಳ್ಗ                    | kannaDa                   |
| 72  | ಸ್ಕ                | 172   | sk   | sk       | 172   | ಸ್ಕ                    | samskxta                  |
| 73  | ವ್ವ                | 168   | vv   | vv       | 168   | ವ್ವ                    | kannaDa                   |
| 74  | ಸ್ಮ                | 158   | sm   | sm       | 158   | ಸ್ಮ                    | samskxta                  |
| 75  | ಜ್ವ                | 151   | jv   | jv       | 151   | ಜ್ವ                    | samskxta                  |
| 76  | ಳ್ಕ                | 145   | Lk   | Lk       | 145   | ಳ್ಕ                    | kannaDa                   |
| 77  | ಷ್ಮ                | 141   | Shm  | Sm       | 141   | **ಶ್ಮ**                | samskxta                  |
| 78  | ಷ್ಪ                | 140   | Shp  | **Sp**   | 140   | **ಶ್ಪ**                | samskxta                  |
| 79  | ಶ್ಚ                | 139   | Sc   | Sc       | 139   | ಶ್ಚ                    | samskxta                  |
| 80  | ಶ್ಯ                | 139   | Sy   | Sy       | 139   | ಶ್ಯ                    | samskxta                  |
| 81  | ಯ್ಸ                | 138   | ys   | ys       | 138   | ಯ್ಸ                    | samskxta                  |
| 82  | ಷ್ಯ                | 138   | Shy  | **Sy**   | 138   | ಶ್ಯ                    | samskxta                  |
| 83  | ಣ್ಯ                | 135   | Ny   | Ny       | 135   | ಣ್ಯ                    | kannaDa                   |
| 84  | ಲ್ಮ                | 133   | lm   | lm       | 133   | ಲ್ಮ                    | samskxta                  |
| 85  | ಸ್ರ                | 132   | sr   | sr       | 132   | ಸ್ರ                    | samskxta                  |
| 86  | ಳ್ವ                | 131   | Lv   | Lv       | 131   | ಳ್ವ                    | kannaDa                   |
| 87  | ಮ್ಯ                | 128   | my   | my       | 128   | ಮ್ಯ                    | samskxta                  |
| 88  | ಲ್ಕ                | 120   | lk   | lk       | 120   | ಲ್ಕ                    | samskxta                  |
| 89  | ಗ್ಯ                | 118   | gy   | gy       | 118   | ಗ್ಯ                    | samskxta                  |
| 90  | ಳ್ತ                | 117   | Lt   | Lt       | 117   | ಳ್ತ                    | kannaDa                   |
| 91  | ತ್ನ                | 113   | tn   | tn       | 113   | ತ್ನ                    | samskxta                  |
| 92  | ದ್ಗ                | 112   | dg   | dg       | 112   | ದ್ಗ                    | samskxta                  |
| 93  | ರ್ನ                | 111   | rn   | rn       | 111   | **ರ್‌ನ**                | samskxta                  |
| 94  | ಹ್ಯ                | 109   | hy   | hy       | 109   | ಹ್ಯ                    | samskxta                  |
| 95  | ೞ್ತ                | 108   | Zt   | ‘’’Lt’’’ | 108   | **ಳ್ತ**                | kannaDa                   |
| 96  | ಕ್ಲ                | 105   | kl   | kl       | 105   | ಕ್ಲ                    | samskxta                  |
| 97  | ಣ್ಗ                | 104   | Ng   | Ng       | 104   | ಣ್ಗ                    | kannaDa                   |

## Examples

### From some commmon Indian sources

[Eke_Examples.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_examples.md)

Note that brAhmi, like devaNAgari doesn't distinguish o and O, e and E.

Samskxta, Hindi and other PIE languages do differentiate ottulis.

Dropping the ottuli has no effect on the way its pronounced commonly
among South Indian (draviDian) language speakers.

The optional h is listed in parentheses in the examples below.

In contrast, l L, n N, d D, e E, o O distinctions are considerably
important in South Indian languages both in pronunciation and
orthography.

tamiZ does not distinguish between k g, t T d D, c j, p b in orthography
but the differences show up in pronunciation. tamiz additionally values
r R, l L Z pronunciation and orhtography differences. These distinctions
were important in older flavors of kannaDa but are not relevant any
more.

### gurinuDi

    ಸಿರಿಗನ್ನಡಂ ಗೆಲ್ಗೆ, ಸಿರಿಗನ್ನಡಂ ಬಾಳ್ಗೆ.

    𑀲𑀺𑀭𑀺𑀕𑀦𑁆𑀦𑀟𑀁 𑀕𑁂𑀮𑁆𑀕𑁂, 𑀲𑀺𑀭𑀺𑀕𑀦𑁆𑀦𑀟𑀁 𑀧𑀸𑀴𑁆𑀕𑁂.

    sirigannaDam gelge, sirigannaDam bALge.

### A pangram using the letters of EK

#### kannaDa

    ಕಾವಲುಗಾರನು ಓರ್ವನು ಇಳಿವೇಳೆ ಆ ದಿನ

    ಒಂದು ಉರಿಯ ಬಾಣವನ್ನು ಈ ಶಿಲೆಗೆ ಹೊಡೆದು

    ಏರಿ ಅಂದೇ ಊರಿನ ಮೇಳದಲ್ಲಿ ಎಡವಿ

    ಚಟಪಟನೆ ಜನರಿಗೆ ತಪ್ಪು ಹಾಡು ಹಾಡಿದ.

#### brAhmi

    𑀓𑀸𑀯𑀮𑀼𑀕𑀸𑀭𑀦𑀼 𑀑𑀭𑁆𑀯𑀦𑀼 𑀇𑀴𑀺𑀯𑁂𑀴𑁂 𑀆 𑀤𑀺𑀦

    𑀑𑀁𑀤𑀼 𑀉𑀭𑀺𑀬 𑀩𑀸𑀡𑀯𑀦𑁆𑀦𑀼 𑀈 𑀰𑀺𑀮𑁂𑀕𑁂 𑀳𑁄𑀟𑁂𑀤𑀼

    𑀓𑁂𑀭𑀺 𑀅𑀁𑀤𑁂 𑀊𑀭𑀺𑀦 𑀫𑁂𑀴𑀤𑀮𑁆𑀮𑀺 𑀓𑁂𑀟𑀯𑀺

    𑀘𑀝𑀧𑀝𑀦𑁂 𑀚𑀦𑀭𑀺𑀕𑁂 𑀢𑀧𑁆𑀧𑀼 𑀳𑀸𑀟𑀼 𑀳𑀸𑀟𑀺𑀤.

#### Eke(EK)

    kAvalugAranu Orvanu iLivELe A diNa

    ondu uriya bANavannu I Silege hoDedu

    Eri andE Urina mELadalli eDavi

    caTapaTane janarige tappu haDu haDida.

#### Meaning

    A guard, one evening,

    struck one burning arrow against this rock,

    arose and then during the village fair,

    stumbled and sang the wrong song energetically to the crowd.

### mankutimmana kagga

#### kannaDa

    ಹುಲ್ಲಾಗು ಬೆಟ್ಟದಡಿ, ಮನೆಗೆ ಮಲ್ಲಿಗೆಯಾಗು

    ಕಲ್ಲಾಗು ಕಷ್ಟಗಳ ಮಳೆಯ ವಿಧಿ ಸುರಿಯೆ

    ಬೆಲ್ಲ ಸಕ್ಕರೆಯಾಗು ದೀನ ದುರ್ಬಲರಿಂಗೆ

    ಎಲ್ಲರೊಳಗೊಂದಾಗು ಮಂಕುತಿಮ್ಮ

#### Eke

    hullAgu beTTadaDi, manege malligeyAgu

    kallAgu kaS(h)TagaLa maLeya vid(h)i suriye

    bella sakkareyAgu dIna durbalaringe

    ellaroLagondAgu mankutimma

### ಉಳ್ಳವರು

#### kannaDa

    ಉಳ್ಳವರು ಶಿವಾಲಯ ಮಾಡಿಹರು\| ನಾನೇನ ಮಾಡಲಿ ಬಡವನಯ್ಯಾ\|\|

    ಎನ್ನ ಕಾಲೇ ಕಂಬ ದೇಹವೇ ದೇಗುಲ\| ಶಿರ ಹೊನ್ನ ಕಳಶವಯ್ಯಾ\|\|

    ಕೂಡಲಸಂಗಮದೇವಾ, ಕೇಳಯ್ಯಾ\| ಸ್ಥಾವರಕಳಿವುಂಟು ಜಂಗಮಕ್ಕಳಿವಿಲ್ಲ\|\|

    —ಬಸವಣ್ಣ

#### Eke

    uLLavaru SivAlaya mADiharu \| nAnEna mADali baDavanayyA \|\|

    enna kAlE kamba dEhavE dEgula \| Sira honna kaLaSavayyA \|\|

    kUDalsangamadEvA, kELayyA \| st(h)AvarakkaLivunTu jangamakkaLivilla \|\|

    -basavaNNa

### ಜನ ಗಣ ಮನ

#### kannaDa

    ಜನ ಗಣ ಮನ ಅಧಿನಾಯಕ ಜಯಹೇ,

    ಭಾರತ ಭಾಗ್ಯ ವಿಧಾತಾ!

    ಪಂಜಾಬ, ಸಿಂಧು, ಗುಜರಾತ, ಮರಾಠಾ,

    ದ್ರಾವಿಡ, ಉತ್ಕಲ, ವಂಗ!

    ವಿಂಧ್ಯ, ಹಿಮಾಚಲ, ಯಮುನಾ, ಗಂಗ,

    ಉಚ್ಚಲ ಜಲಧಿತರಂಗ!

    ತವ ಶುಭನಾಮೇ ಜಾಗೇ!

    ತವ ಶುಭ ಆಶಿಷ ಮಾಗೇ!

    ಗಾಹೇ ತವ ಜಯ ಗಾಥಾ!

    ಜನಗಣ ಮಂಗಳದಾಯಕ ಜಯಹೇ ಭಾರತ ಭಾಗ್ಯವಿಧಾತಾ!

    ಜಯಹೇ! ಜಯಹೇ! ಜಯಹೇ! ಜಯ ಜಯ ಜಯ ಜಯಹೇ!

#### Eke

    jana gaNa mana ad(h)inAyaka jayahE,

    b(h)Arata b(h)Agya vid(h)Ata!

    panjAba, sind(h)u, gujarAta, marAT(h)a,

    drAviDa, utkala, vanga!

    vind(h)ya, himAcala, yamunA, ganga,

    uccala jalad(h)itaranga!

    tava Sub(h)anAmE jAgE!

    tava Sub(h)a ASiS(h)a mAgE!

    gAhE tava jaya gAt(h)A!

    janagaNa mangaLadAyaka jayahE b(h)Arata b(h)Agyavid(h)AtA!

    jayahE! jayahE! jayahE! jaya jaya jaya jayahE!

### bhaja gOvindam

#### samskxta in devanAgari

    भज गोविन्दं भज गोविन्दं

    गोविन्दं भज मूढमते ।

    सम्प्राप्ते सन्निहिते काले

    नहि नहि रक्षति डुकृञ्करणे ॥

#### samskxta in kannaDa script

    ಭಜ ಗೋವಿಂದಮ್ ಭಜ ಗೋವಿಂದಂ

    ಗೋವಿಂದಮ್ ಭಜ ಮೂಢಮತೆ ।

    ಸಂಪ್ರಾಪ್ತೆ ಸನ್ನಿಹಿತೆ ಕಾಲೆ

    ನಹಿ ನಹಿ ರಕ್ಷತಿ ಡುಕೃಂಕರಣೆ ॥

#### samskxta in Eke

    b(h)aja gOvindam b(h)aja gOvindam

    gOvindam b(h)aja mUD(h)amate \|

    samprApte sannihite kAle

    nahi nahi rakS(h)ati Dukru(x)n(G)karaNe \|\|

### Enidu ellara kannaDa

<https://honalu.net/%e0%b2%8e%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%b0%e0%b2%95%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b2%a1/>

#### In Eke

    ellarakannaDa

    enidu ‘ellarakannaDa’?

    kannaDavannu hosadondu ritiyalli bareyuva aleyondu eddide. idu
    heccu-kaDime kannaDadalli bareyuvavarellara gamanakkU bandide. I
    caLuvaLiyannu ‘ellarakannaDa’da caLuvaLiyennabahudu. ellarakannaDadalli
    bareyuvAga AdaSTuu heccu (nUrakke nUralla!) accagannaDa pada gaLannu
    baLasi bareyuva mogasu barahagAranadagiruttide
    (barahagAr‍tiyadagiruttide). jotege, heccina kannaDigaru uliyada
    barigegaLada mahaprANa gaLu, x, Sha ivugaLa badalAgi OraNavAgi
    alpapraaNa gaLu, ru, Sa ivugaLannu baLasalaguttide. haageye
    barigemaNeyalli yAva viSeSavada kelasavannU mADada arkAvottina badalAgi
    rakArakke ottannu baLasalaguttade. ettugege: sukha \> suka, kxShi \>
    kruSi, kaShTa \> kaSTa, karnATaka \> karnATaka. EkI ‘ellarakannaDa’?

### halmiDi inscription

The transcription from kadamba script into kannada from the Wiki on
halmiDi is transcribed into Eke here. Original is in kadamba kannaDa
script which is very different. In some ways it can be seen as between
modern kannaDa and asokan/tamiZ brAhmi and note that all script names
are quite incidental. Most scripts were not referred to as such at that
point in time.

#### Modern kannaDa script

    ಜಯತಿ ಶ್ರೀ ಪರಿಷ್ವರ್ಙ್ಗ ಶ್ಯಾರ್ಙ್ಗ \[ವ್ಯಾ\]ನತಿರ್ ಅಚ್ಯುತಃ ದಾನಕ್ಷೆರ್ ಯುಗಾನ್ತಾಗ್ನಿಃ \[ಶಿ\]ಷ್ಟಾನಾನ್ತು
    ಸುದರ್ಶನಃ ನಮಃ ಶ್ರೀಮತ್ ಕದಂಬಪನ್ ತ್ಯಾಗ ಸಂಪನ್ನನ್‍ಕಲಭೋರ\[ನಾ\] ಅರಿ ಕ ಕುಸ್ಥಭಟ್ಟೋರನ್ ಆಳೆ
    ನರಿದಾವಿ\[ಳೆ\] ನಾಡುಳ್ ಮೃಗೇಶನಾ ಗೇನ್ದ್ರಾಭೀಳರ್ ಭ್ಭಟಹರಪ್ಪೋರ್ ಶ್ರೀ ಮೃಗೇಶ ನಾಗಾಹ್ವಯ ರ್ ಇರ್ವ್ವರಾ
    ಬಟರಿ ಕುಲಾಮಲ ವ್ಯೋಮತಾರಾಧಿನಾಥನ್ ಅಳಪ ಗಣ ಪಶುಪತಿಯಾ ದಕ್ಷಿಣಾಪಥ ಬಹುಶತಹವನಾಹವದು\[ಳ್\]
    ಪಶುಪ್ರದಾನ ಶೌರ್ಯ್ಯೋದ್ಯಮ ಭರಿತೋ\[ನ್ದಾನ\]ಪಶುಪತಿಯೆನ್ದು ಪೊಗೞೆಪ್ಪೊಟ್ಟಣ ಪಶುಪತಿ ನಾಮಧೇಯನ್
    ಆಸರಕ್ಕೆಲ್ಲಭಟರಿಯಾ ಪ್ರೇಮಾಲಯಸುತನ್ಗೆ zಸೇನ್ದ್ರಕ ಬಣೋಭಯ ದೇಶದಾ ವೀರಪುರುಷಸಮಕ್ಷದೆ ಕೇಕಯ ಪಲ್ಲವರಂ
    ಕಾದೆಱದು ಪೆತ್ತಜಯನಾ ವಿಜ ಅರಸಂಗೆ ಬಾಳ್ಗೞ್ಚು ಪಲ್ಮಡಿಉಂ ಮೂಱುವಳ್ಳಿಉಂ ಕೊಟ್ಟಾರ್ ಬಟಾರಿ ಕುಲದೊನಳ
    ಕದಂಬನ್ ಕೞ್ದೋನ್ ಮಹಾಪಾತಕನ್ ಸ್ವಸ್ತಿ ಭಟ್ಟರ್ಗ್ಗೀಗೞ್ದೆ ಒಡ್ಡಲಿ ಆ ಪತ್ತೊನ್ದಿ ವಿಟ್ಟಾರಕರ

#### Eke

    jayati SrI pariSvarGga SyArGga \[vyA\]natir achyutaH dAnakSer
    yugAntAgniH \[Si\]STAnAntu sudarSanH namaH SrImat kadambapan tyAga
    sampannan‍kalab(h)Ora\[nA\] ari ka kusT(h)ab(h)aTTOran ALe nariDAvi\[Le\]
    nADuL mRgeSanA gEndrAb(h)ILar b(h)b(h)aT(h)arapappOr SrI mRgeSa
    nAgA(h)vaya r irvvaraa baTari kulAmala vyOmatArAd(h)inAT(h)an aLapa gaNa
    paSupatiyaa dakSiNApat(h)a ba(h)uSata(h)avanA(h)avadu\[L\] paSupradAna
    SOuryyOdyama b(h)ariTO\[ndAna\]paSupatiyendu pogaLeppOTTaNa paSupati
    nAmad(h)eyan Asarakkellb(h)aTariyaa prEmAlayasutan'ge zsEndraka
    baNOb(h)aya DES(h)adA vIra puruSasamakSadhe kEkaya pallavaram kAdeRedu
    pettajayanA vija arasan'ge bALgaLc(h)u palmaDi um mURuvalLi um kOTTAr
    baTArI kuladonaLa kadamban kaLdOn ma(h)ApAtakan svasti
    b(h)aTTar'gIghaLdhe oDDali A pattondi viTTArakar

### From English

[Eke_Examples_English.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_examples_English.md)

### lotr

English and Eke equivalents

    Gandalf : \[to Saruman\] There is only one Lord of the Ring, only one
    who can bend it to his will, and he does not share power.

    gyAnDAhlf : \[Tu sArumAn\] dEr is onli on lAhrD Ahf da ring, onli on hu
    kAhn benD iT Tu his will, AhnD hi daz nAhT SEr pAhwar.

    Saruman : So you have chosen... death.

    sArumAn : so yU hahv cOsan... Det.

### da sTAr spAhngalD bahnar

#### English

    The Star-Spangled Banner

    Say, can you see

    By the dawn's early light

    What so proudly we hailed

    At the twilight's last gleaming?

    Whose broad stripes and bright stars

    Through the perilous fight

    O'er the ramparts we watched

    Were so gallantly, yeah, streaming?

    And the rockets' red glare

    The bombs bursting in air

    Gave proof through the night

    That our flag was still there

    O say, does that star-spangled banner yet wave

    O'er the land of the free and the home of the brave

#### Eke


    **da sTAr spAhngalD bahnar**

    sE, kahn yu sI

    bAy da DAhn's arli layT

    wAT so pravDli wi haylD

    AhT da TwilayT's lAsT glIming?

    hUz brAhd sTrayps anD brAyT sTArs

    trU da perilas fAyT

    Ovar da rAhmpArts wi wAcD

    war so gAhlenTli, ya, sTrIming?

    AhnD da rAhkeTs' reD glEr

    da bAhmbs barsting in Er

    gEv prUf thrU da nAyT

    daT Awr flAhg wAs sTil dEr

    o sE, Das daT sTAr-spAhngalD bAhnar yeT wEv

    Owar da lAhnD Ahf da frE anD da lAhnD Ahf da brEv

### ArTikal on

#### English

    All human beings are born free and equal in dignity and rights. They are
    endowed with reason and conscience and should act towards one another in
    a spirit of brotherhood.

#### Eke

    All hyUman bEings Ar bAhrn frI AhnD Ikwal in Digniti AhnD rAiTs. De Ar
    enDOD wit rIzan AhnD shuD Ahct tuwarDs on anater in ah spiriT Ahf
    bradarhuD.

### Using Notebook LLM

[Eke_Examples_notebook.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/Eke_examples_notebook.md)

## halmiDi inscription using Notebook LLM using this wiki as a reference

The transcription from kadamba script into kannada from the Wiki on
halmiDi and this wiki link was provided as sources to get the following
response.

### Response

    Comprehensive Brahmi Transcription Attempt of the Full Kannada Text
    Building on the previous discussion, the provided sources can aid in
    transcribing the full Kannada text into Brahmi using Eke as a bridge.
    However, the same limitations apply: incomplete Eke tables, ambiguous
    "virama" mapping, and a lack of specification regarding the historical
    Brahmi variant to be used. Therefore, the following transcription
    represents a best-effort attempt based on the available sources and
    necessitates independent verification. External resources on Brahmi
    script, comparative script analysis, and Kannada-Brahmi mapping are
    highly recommended for confirmation and refinement.

#### kannaDa

    ಜಯತಿ ಶ್ರೀ ಪರಿಷ್ವರ್ಙ್ಗ ಶ್ಯಾರ್ಙ್ಗ \[ವ್ಯಾ\]ನತಿರ್ ಅಚ್ಯುತಃ ದಾನಕ್ಷೆರ್ ಯುಗಾನ್ತಾಗ್ನಿಃ \[ಶಿ\]ಷ್ಟಾನಾನ್ತು
    ಸುದರ್ಶನಃ ನಮಃ ಶ್ರೀಮತ್ ಕದಂಬಪನ್ ತ್ಯಾಗ ಸಂಪನ್ನನ್‍ಕಲಭೋರ\[ನಾ\] ಅರಿ ಕ ಕುಸ್ಥಭಟ್ಟೋರನ್ ಆಳೆ
    ನರಿದಾವಿ\[ಳೆ\] ನಾಡುಳ್ ಮೃಗೇಶನಾ ಗೇನ್ದ್ರಾಭೀಳರ್ ಭ್ಭಟಹರಪ್ಪೋರ್ ಶ್ರೀ ಮೃಗೇಶ ನಾಗಾಹ್ವಯ ರ್ ಇರ್ವ್ವರಾ
    ಬಟರಿ ಕುಲಾಮಲ ವ್ಯೋಮತಾರಾಧಿನಾಥನ್ ಅಳಪ ಗಣ ಪಶುಪತಿಯಾ ದಕ್ಷಿಣಾಪಥ ಬಹುಶತಹವನಾಹವದು\[ಳ್\]
    ಪಶುಪ್ರದಾನ ಶೌರ್ಯ್ಯೋದ್ಯಮ ಭರಿತೋ\[ನ್ದಾನ\]ಪಶುಪತಿಯೆನ್ದು ಪೊಗೞೆಪ್ಪೊಟ್ಟಣ ಪಶುಪತಿ ನಾಮಧೇಯನ್
    ಆಸರಕ್ಕೆಲ್ಲಭಟರಿಯಾ ಪ್ರೇಮಾಲಯಸುತನ್ಗೆ zಸೇನ್ದ್ರಕ ಬಣೋಭಯ ದೇಶದಾ ವೀರಪುರುಷಸಮಕ್ಷದೆ ಕೇಕಯ ಪಲ್ಲವರಂ
    ಕಾದೆಱದು ಪೆತ್ತಜಯನಾ ವಿಜ ಅರಸಂಗೆ ಬಾಳ್ಗೞ್ಚು ಪಲ್ಮಡಿಉಂ ಮೂಱುವಳ್ಳಿಉಂ ಕೊಟ್ಟಾರ್ ಬಟಾರಿ ಕುಲದೊನಳ
    ಕದಂಬನ್ ಕೞ್ದೋನ್ ಮಹಾಪಾತಕನ್ ಸ್ವಸ್ತಿ ಭಟ್ಟರ್ಗ್ಗೀಗೞ್ದೆ ಒಡ್ಡಲಿ ಆ ಪತ್ತೊನ್ದಿ ವಿಟ್ಟಾರಕರ

#### Potential Eke Transcription:

    jayati SrI pariSvarGga SyArGga \[vyA\]natir achyutaH dAnakSer
    yugAntAgniH \[Si\]STAnAntu sudarSanH namaH SrImat kadambapan tyAga
    sampannan‍kalab(h)Ora\[nA\] ari ka kusT(h)ab(h)aTTOran ALe nariDAvi\[Le\]
    nADuL mRgeSanA gEndrAb(h)ILar b(h)b(h)aT(h)arapappOr SrI mRgeSa
    nAgA(h)vaya r irvvaraa baTari kulAmala vyOmatArAd(h)inAT(h)an aLapa gaNa
    paSupatiyaa dakSiNApat(h)a ba(h)uSata(h)avanA(h)avadu\[L\] paSupradAna
    SOuryyOdyama b(h)ariTO\[ndAna\]paSupatiyendu pogaLeppOTTaNa paSupati
    nAmad(h)eyan Asarakkellb(h)aTariyaa prEmAlayasutan'ge zsEndraka
    baNOb(h)aya DES(h)adA vIra puruSasamakSadhe kEkaya pallavaram kAdeRedu
    pettajayanA vija arasan'ge bALgaLc(h)u palmaDi um mURuvalLi um kOTTAr
    baTArI kuladonaLa kadamban kaLdOn ma(h)ApAtakan svasti
    b(h)aTTar'gIghaLdhe oDDali A pattondi viTTArakar

#### Brahmi Transcription (Subject to Verification):

    𑀚𑀬𑀫𑀝𑀅 𑀰𑀅𑀭𑀅 𑀧𑀭𑀅𑀱𑀯𑀭𑀘𑀁𑀕𑀁 𑀰𑀬𑀆𑀱𑀁𑀕𑀁 \[𑀯𑀬𑀆\]𑀦𑀝𑀅𑀱𑀅 𑀅𑀙𑀬𑀝𑀆𑀳 𑀤𑀆𑀦𑀓𑀾𑀹𑀱𑀅 𑀬𑀴𑀕𑀆𑀦𑀝𑀆𑀕𑀦𑀅𑀳
    \[𑀰𑀅\]𑀲𑀝𑀆𑀦𑀆𑀦𑀝𑀴 𑀘𑀴𑀤𑀭𑀱𑀡𑀁𑀳 𑀦𑀫𑀳 𑀰𑀅𑀭𑀫𑀝𑀅 𑀓𑀤𑀁𑀩𑀁𑀧𑀁 𑀢𑀬𑀆𑀕 𑀘𑀁𑀧𑀦𑀦𑀁𑀦𑀁𑀓𑀟𑀪𑀸𑀭𑀆 \[𑀦𑀆\] 𑀅𑀭𑀅 𑀓
    𑀓𑀴𑀲𑀞𑀪𑀝𑀝𑀸𑀱𑀁𑀦𑀁 𑀆𑀟𑀹 𑀦𑀭𑀅𑀤𑀆𑀯𑀅 \[𑀴𑀹\] 𑀦𑀆𑀤𑀴𑀟𑀅 𑀫𑀼𑀕𑀹𑀬𑀦𑀆𑀦𑀆 𑀕𑀹𑀦𑀤𑀫𑀆𑀪𑀅𑀟𑀅 𑀪𑀪𑀝𑀳𑀯𑀭𑀧𑀧𑀸𑀧𑀧𑀸𑀱𑀁𑀱𑀸𑀭 𑀰𑀅𑀭𑀅
    𑀫𑀼𑀕𑀹𑀬𑀘 𑀦𑀆𑀕𑀆𑀯𑀯𑀬𑀬 𑀱𑀅𑀭𑀯𑀯𑀭𑀆 𑀩𑀀𑀝𑀭𑀅 𑀓𑀴𑀟𑀆𑀫𑀟 𑀯𑀬𑀸𑀫𑀝𑀆𑀭𑀆𑀟𑀆𑀳𑀁𑀁𑀝𑀁 𑀅𑀟𑀧 𑀕𑀡 𑀧𑀴𑀫𑀴𑀧𑀝𑀅𑀬𑀆
    𑀤𑀓𑀷𑀜𑀆𑀧𑀆𑀭𑀀 𑀤𑀓𑀾𑀜𑀆𑀧𑀆𑀑 𑀩𑀳𑀴𑀬𑀝𑀆𑀳𑀯𑀡𑀆𑀳𑀯𑀤𑀴𑀤𑀴 \[𑀴\] 𑀧𑀴𑀫𑀴𑀧𑀫𑀤𑀆𑀦 𑀘𑀸𑀼𑀬𑀬𑀸𑀤𑀬𑀫 𑀪𑀭𑀅𑀝𑀸
    \[𑀦𑀤𑀆𑀦\]𑀧𑀴𑀫𑀴𑀧𑀝𑀅𑀁𑀦𑀴 𑀧𑀸𑀕𑀴𑀧𑀧𑀸𑀝𑀝𑀡 𑀧𑀴𑀫𑀴𑀧𑀝𑀅 𑀦𑀆𑀫𑀤𑀵𑀬𑀁 𑀆𑀘𑀭𑀓𑀓𑀴𑀟𑀪𑀝𑀭𑀅𑀬𑀆 𑀧𑀫𑀹𑀫𑀟𑀆𑀟𑀴𑀘𑀴𑀝𑀦𑀁𑀕𑀹
    𑀚𑀁𑀦𑀼𑀦𑀓 𑀩𑀡𑀸𑀪𑀬𑀬 𑀤𑀹𑀬𑀤𑀆 𑀯𑀅𑀭𑀧𑀴𑀭𑀴𑀬𑀘𑀫𑀷𑀤𑀹 𑀓𑀹𑀓𑀬𑀬 𑀧𑀟𑀟𑀯𑀭𑀁 𑀓𑀆𑀤𑀹𑀭𑀤𑀴 𑀧𑀹𑀝𑀝𑀯𑀭𑀆𑀦𑀆 𑀯𑀅𑀚 𑀅𑀭𑀘𑀁𑀕𑀹 𑀩𑀆𑀟𑀁𑀕𑀴𑀟𑀁
    𑀓𑀸𑀝𑀁𑀩𑀁 𑀓𑀴𑀝𑀝𑀆𑀭 𑀩𑀝𑀆𑀭𑀅 𑀓𑀴𑀟𑀤𑀸𑀦𑀟 𑀓𑀤𑀁𑀩𑀁𑀦𑀁 𑀓𑀟𑀳𑀆𑀧𑀆𑀝𑀁 𑀓𑀟𑀳𑀦𑀇𑀝𑀁 𑀓𑀸𑀝𑀝𑀆𑀭 𑀩𑀝𑀆𑀭𑀅 𑀓𑀴𑀟𑀤𑀸𑀦𑀅 𑀓𑀴𑀟𑀤𑀸𑀤𑀸𑀦𑀟
    𑀓𑀤𑀁𑀩𑀁𑀦𑀁 𑀓𑀟𑀳𑀤𑀸𑀦𑀁 𑀫𑀳𑀳𑀆𑀧𑀆𑀝𑀁 𑀘𑀯𑀘𑀝𑀅 𑀆 𑀧𑀝𑀝𑀸𑀦𑀁 𑀯𑀅𑀝𑀝𑀆𑀭𑀓𑀭

#### Notes as-is from Notebook LLM:

    The transcription heavily relies on Eke mapping, assuming a basic Brahmi
    variant.

    Complex consonant clusters and vowel modifications may be inaccurate due
    to limitations in the sources.

    The character "z" in the text is unclear and is represented with a
    placeholder in the Brahmi transcription.

    Square brackets indicate portions of the text with potential uncertainty
    in their representation.

    "Virama" in Brahmi is a complex aspect and is not clearly defined in the
    sources. Its representation here is a simplification and needs to be
    verified.

    Confirmation Needed: Independent verification of the entire
    transcription using specialized resources on Brahmi script and its
    relationship to Kannada is absolutely necessary. This transcription
    serves as a preliminary attempt based on the provided information.

## References

[^2][^3][^4][^5][^6][^7][^8][^9][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31]

## Consonant Clusters

The following tables can be used to transliterate from Kannada to Brahmi
to Devanagiri to Eke to grantha as appropriate.

Further the Eke(ek) and "ellara kannaDa" section allows for the
simplifications suggested by "ellara kannada" itself. It can be applied
to most dravidian languages without loss of precision.

### Consonant cluster combinations

TBD

### Consontant Vowel combinations

TBD

## English

TBD

[^1]: <https://tinyurl.com/indicprogramming>

[^2]: <http://dnshankarabhat.net/dr-d-n-shankara-bhat/>

[^3]: <https://honalu.net/%e0%b2%8e%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%b0%e0%b2%95%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b2%a1/>

[^4]: <https://en.wikipedia.org/wiki/ARPABET>

[^5]: <https://en.wikipedia.org/wiki/Pronunciation_respelling_for_English>

[^6]: <https://anglish.org/wiki/Anglish>

[^7]: <https://kn.wiktionary.org/wiki/%E0%B2%AE%E0%B3%81%E0%B2%96%E0%B3%8D%E0%B2%AF_%E0%B2%AA%E0%B3%81%E0%B2%9F>

[^8]: <https://alar.ink/>

[^9]: <https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration>

[^10]: <https://en.wikipedia.org/wiki/Harvard-Kyoto>

[^11]: <https://en.wikipedia.org/wiki/International_Phonetic_Alphabet>

[^12]: <https://en.wikipedia.org/wiki/Help:Pronunciation_respelling_key>

[^13]: <https://en.wikipedia.org/wiki/Brahmic_scripts>

[^14]: <https://en.wikipedia.org/wiki/ISO_15919>

[^15]: <https://en.wikipedia.org/wiki/Kannada_script>

[^16]: <https://wordalla.online/>

[^17]: <https://www.bolochant.com/blog/sanskrit-pronunciation?srsltid=AfmBOoo4xJI5AgtG15ArUM_XFhj0cQFh1Pa27NCNLguGITuLwpzl-rjs>

[^18]: <https://theleaflet.in/leaflet-specials/plain-languages-in-a-complex-country>

[^19]: <https://timesofindia.indiatimes.com/city/bengaluru/drive-to-sanitise-kannadalanguage-kicks-up-a-row/articleshow/88798079.cms>

[^20]: <https://en.wikipedia.org/wiki/Dravidian_languages>

[^21]: <https://en.wikipedia.org/wiki/Proto-Dravidian_language>

[^22]: <https://en.wiktionary.org/wiki/Appendix:Proto-Dravidian_reconstructions>

[^23]: <https://en.wikipedia.org/wiki/Kadamba_script>

[^24]: <https://mythicsociety.github.io/AksharaBhandara/#/learn/Varnamale>

[^25]: <https://en.wikipedia.org/wiki/Abugida>

[^26]: <https://en.wikipedia.org/wiki/Mankuthimmana_Kagga>

[^27]: <https://kn.wikisource.org/wiki/%E0%B2%89%E0%B2%B3%E0%B3%8D%E0%B2%B3%E0%B2%B5%E0%B2%B0%E0%B3%81_%E0%B2%B6%E0%B2%BF%E0%B2%B5%E0%B2%BE%E0%B2%B2%E0%B2%AF_%E0%B2%AE%E0%B2%BE%E0%B2%A1%E0%B2%BF%E0%B2%B9%E0%B2%B0%E0%B3%81>

[^28]: <https://en.wikipedia.org/wiki/Romanization_of_Japanese>

[^29]: <https://honalu.net/2013/05/29/%E0%B2%B6%E0%B2%AC%E0%B3%8D%E0%B2%A6%E0%B2%AE%E0%B2%A3%E0%B2%BF%E0%B2%A6%E0%B2%B0%E2%80%8D%E0%B3%8D%E0%B2%AA%E0%B2%A3%E0%B2%A6%E0%B2%B2%E0%B3%8D%E0%B2%B2%E0%B2%BF-%E0%B2%A4%E0%B2%B3%E0%B2%AE-3/>

[^30]: <https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/Dravidian/Kannada%2C%20A%20Generative%20Grammar%20of%20%28Ramanujan%29.pdf>

[^31]: <https://tinyurl.com/indicprogramming>
