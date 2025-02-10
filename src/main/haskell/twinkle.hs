module Main where
import Lib
import Euterpea

pcToQN pc = note qn (pc, 4)

twinkle1 =
  line (map pcToQN [C, C, G, G, A, A]) :+: g 4 hn :+:
  line (map pcToQN [F, F, E, E, D, D]) :+: c 4 hn :+:
  line (map pcToQN [G, G, F, F, E, E]) :+: d 4 hn :+:
  line (map pcToQN [G, G, F, F, E, E]) :+: d 4 hn :+:
  line (map pcToQN [C, C, G, G, A, A]) :+: g 4 hn :+:
  line (map pcToQN [F, F, E, E, D, D]) :+: c 4 hn 

main :: IO ()
main = play $ twinkle1
