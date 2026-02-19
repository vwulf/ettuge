# Mapping Shivkumar's Music Terminology to Standard Western Sheet Music

## Context

This conversation discusses how Carnatic music terminology from Prof. Shivkumar's website maps to standard Western sheet music, and how to encode the Brindāvana Sārangā raga (used in Rangapura Vihara) into Euterpea notation.

References from `hsom.md`:
- Shivkumar's gentle intro: http://www.shivkumar.org/music/basics/ramesh/gentle-intro-ramesh-mahadevan-I.htm
- Rangapura Vihara notation: http://www.shivkumar.org/music/rangapura.pdf

---

## Carnatic (Shivkumar) → Western Sheet Music Mapping

### Notes (Swaras)

| Carnatic Swara | Abbreviation | Western Equivalent |
|---|---|---|
| Shadjam | **Sa** | C (tonic / root) |
| Rishabham | **Ri** (Ri1/Ri2/Ri3) | D♭ / D / D♯ |
| Gandharam | **Ga** (Ga1/Ga2/Ga3) | E♭ / E / (E♯) |
| Madhyamam | **Ma** (Ma1/Ma2) | F / F♯ |
| Panchamam | **Pa** | G (perfect fifth, fixed) |
| Dhaivatam | **Dha** (Dha1/Dha2/Dha3) | A♭ / A / A♯ |
| Nishadam | **Ni** (Ni1/Ni2/Ni3) | B♭ / B / (B♯) |

> **Sa** and **Pa** are fixed (like C and G). The other five swaras have variants (shrutis), giving rise to the full 12-semitone chromatic scale.

---

### Scale / Mode (Raga → Key/Mode)

| Carnatic | Western |
|---|---|
| **Raga** | Scale / Mode (e.g., Major, Minor, Dorian) |
| **Melakarta raga** | Parent scale (like a key signature) |
| **Janya raga** | Derived mode (subset of a parent scale) |
| **Aarohanam** (ascending scale) | Ascending scale pattern |
| **Avarohanam** (descending scale) | Descending scale pattern (may differ!) |

For example, the raga of **Rangapura Vihara** — **Brindāvana Sārangā** — is a janya raga whose notes map roughly to a pentatonic-ish mode in Western terms.

---

### Rhythm (Tala → Time Signature / Meter)

| Carnatic | Western |
|---|---|
| **Tala** | Time signature / meter |
| **Adi Tala** (8 beats) | 8/8 or 4/4 |
| **Rupaka Tala** (6 beats) | 6/8 |
| **Misra Chapu** (7 beats) | 7/8 |
| **Akshara** (beat unit) | Beat |
| **Gati / Nadai** (subdivisions) | Tuplets (triplets, quintuplets, etc.) |
| **Avartanam** | One full measure/bar |

---

### Ornamentation (Gamaka → Articulation/Ornaments)

| Carnatic | Western Equivalent |
|---|---|
| **Gamaka** (oscillation/glide) | Vibrato, trill, glissando |
| **Kampita** (shake) | Trill (~) |
| **Jaru** (slide) | Glissando / portamento |
| **Nokku** (stress) | Accent (>) |

> Gamakas are highly idiomatic to Carnatic music and are not fully representable in standard Western notation.

---

## Brindāvana Sārangā → Euterpea

### Raga Scale

**Brindāvana Sārangā** is a janya raga of the 23rd Melakarta (Gaurimanohari). Its swaras with **C as Sa**:

| Swara | Carnatic | Western (C as Sa) | Euterpea |
|---|---|---|---|
| Sa | S | C | `C` |
| Ri2 | R | D | `D` |
| Ga2 | G | E♭ | `Ef` |
| Ma1 | M | F | `F` |
| Pa | P | G | `G` |
| Dha2 | D | A | `A` |
| Ni2 | N | B♭ | `Bf` |

**Aarohanam (ascending):** S R M P N Ṡ → `C D F G Bf C(oct5)`
**Avarohanam (descending):** Ṡ N D P M G R S → `C(oct5) Bf A G F Ef D C`

> Ga (E♭) and Dha (A) appear **only in the descent** — this is what makes it a *vakra* (zigzag) janya raga.

---

### Euterpea Code

The following Haskell file (`src/main/haskell/euterpea/rangapura.hs`) encodes the raga scale and opening phrases:

```haskell
module Main where
import Euterpea

-- Map a pitch class to a quarter note at octave 4
pcToQN :: PitchClass -> Music Pitch
pcToQN pc = note qn (pc, 4)

-- Map a pitch class to an eighth note at octave 4
pcToEN :: PitchClass -> Music Pitch
pcToEN pc = note en (pc, 4)

-- Brindavana Saranga raga scale
-- Arohanam (ascending): S R M P N S'
-- Note: no Ga or Dha in ascent
arohanam :: Music Pitch
arohanam =
  line (map pcToQN [C, D, F, G, Bf]) :+: note qn (C, 5)

-- Avarohanam (descending): S' N D P M G R S
-- Ga (Ef) and Dha (A) appear only in descent
avarohanam :: Music Pitch
avarohanam =
  note qn (C, 5) :+:
  line (map pcToQN [Bf, A, G, F, Ef, D, C])

-- Full scale (up and down)
brindavanaSaranga :: Music Pitch
brindavanaSaranga = arohanam :+: avarohanam

-- Opening phrase of Rangapura Vihara (approximate)
-- "Ran-ga-pu-ra vi-ha-ra" : P P M G R S
rangapuraPhrase :: Music Pitch
rangapuraPhrase =
  line (map pcToQN [G, G, F, Ef, D, C])

-- Anupallavi fragment: "rAjIva nayana" : N D P M P G R
rangapuraAnupallavi :: Music Pitch
rangapuraAnupallavi =
  note qn (Bf, 4) :+:
  line (map pcToQN [A, G, F, G, Ef, D])

main :: IO ()
main = play $ brindavanaSaranga :+: rangapuraPhrase :+: rangapuraAnupallavi
```

---

### Caveats & What's Missing

| What's missing | Why it matters |
|---|---|
| **Kampita on Ga (E♭)** | The Ga in this raga is heavily oscillated — it is not a flat static note |
| **Jaru (slides)** into Pa and Ni | These define the raga's character |
| **Subtle Dha (A)** in descent | It is often approached with a glide from Pa |
| **Microtonal shrutis** | Euterpea uses equal temperament; Carnatic uses just intonation |

To go further, you would need either custom `Music` constructors in Euterpea for ornaments, or a different synthesis backend (like SuperCollider or CSound) that supports microtonal pitch bends.

---

## References

- [hsom.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/hsom.md)
- [rangapura.hs](https://github.com/vwulf/ettuge/blob/master/src/main/haskell/euterpea/rangapura.hs)
- [twinkle.hs](https://github.com/vwulf/ettuge/blob/master/src/main/haskell/euterpea/twinkle.hs)
- [Shivkumar's gentle intro](http://www.shivkumar.org/music/basics/ramesh/gentle-intro-ramesh-mahadevan-I.htm)
- [Rangapura Vihara notation PDF](http://www.shivkumar.org/music/rangapura.pdf)
- [Rangapura Vihara - Wikipedia](https://en.wikipedia.org/wiki/Rangapura_Vihara)
- [Muthuswami Dikshitar - Wikipedia](https://en.wikipedia.org/wiki/Muthuswami_Dikshitar)
- [Agam fusion version (YouTube)](https://youtu.be/c3O0PhhD6B4?si=LQbJRKrH7HZcbtIZ)