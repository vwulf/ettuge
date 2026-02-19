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
-- Using quarter notes as a basic approximation (no gamakas)
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
