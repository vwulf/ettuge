# From Euterpea to Rangapura Vihara

## Euterpea / HSOM
A while back I ran in to [^6] and thought this would be an interesting way to learn music.
The sections on using basic functional programming and a literate DSL to represent sheet notation
appealed to me. More advanced parts of the book connects the structure of music to some intricate
categorical concepts. However nothing advanced is needed to play with music.

## Twinkle Twinkle Little Star
I used it to write a simple song like "Twinkle Twinkle Little Star" [^1] [^5] from some sheet music that's
generally available.

```
twinkle1 =
  line (map pcToQN [C, C, G, G, A, A]) :+: g 4 hn :+:
  line (map pcToQN [F, F, E, E, D, D]) :+: c 4 hn :+:
  line (map pcToQN [G, G, F, F, E, E]) :+: d 4 hn :+:
  line (map pcToQN [G, G, F, F, E, E]) :+: d 4 hn :+:
  line (map pcToQN [C, C, G, G, A, A]) :+: g 4 hn :+:
  line (map pcToQN [F, F, E, E, D, D]) :+: c 4 hn 
```

## Rangapura Vihara by Agam
However I enjoy carnatic music as well as certain kinds of fusion with jazz, blues and
rock [^7]. In the time of playing around with Euterpea - the most complicated of which was to get an installation
working, I was introduced to a fusion version of "Rangapura Vihara" [^8] which held my attention for a while.

## Disambiguating

Although this version uses 2 different songs from 2 different sources.

"Rangapura Vihara" [^2] was written by Muthuswamy Dikshitar [^3].
He was known to compose exclusively in Sanskrit and have at least 1 self-reference to the underlying raga in his compositions.
The underlying raga being Brindāvana Sārangā is referenced in the song itself.

The puzzling beginning portion of the song (which is not in Sanskrit) sung by Agam is from a different composer [^12] [^13]
with a rich history as well.

## Attempt to synthesize

The idea of generating the basic song from notes seemed interesting. Carnatic notation is not as universal as sheet notation.
So I stuck to the original. There's extensive information on Carnatic and its mappings to Sheet music on Prof Shivkumar's website [^3]

Digging into [^4] without any musical training and trying to convert them to sheet notation wasn't easy.
In fact, it went nowhere and sounded nothing like the original. A project that I have left for later.

## Alternates to Euterpea
While attempting to summarize this earlier work, I also saw some interesting attempts to port HSOM/Euterpea to scala 3 [^10].
The original writer of HSOM - Paul Hudak is no more and the current maintainer has mentioned in some forums that the underlying
design is not being changed [^15] but just being maintained. It would be interesting to try the scala variant to see if the installation issues
along the line that I ran into [^9] are less prevalent.

## References

[^1]: https://github.com/vwulf/ettuge/blob/master/src/main/haskell/euterpea/twinkle.hs
[^2]: https://en.wikipedia.org/wiki/Rangapura_Vihara
[^3]: http://www.shivkumar.org/music/basics/ramesh/gentle-intro-ramesh-mahadevan-I.htm
[^4]: http://www.shivkumar.org/music/rangapura.pdf
[^5]: https://github.com/vwulf/ettuge/blob/master/src/main/haskell/euterpea/twinkle.m4a
[^6]: https://www.cs.yale.edu/homes/hudak/Papers/HSoM.pdf
[^7]: https://en.wikipedia.org/wiki/R._Prasanna
[^8]: https://youtu.be/c3O0PhhD6B4?si=LQbJRKrH7HZcbtIZ
[^9]: https://stackoverflow.com/questions/40869437/installation-of-haskell-package-euterpea-fails-on-nixos
[^10]: https://github.com/bartschuller/euterpea-scala3
[^11]: https://en.wikipedia.org/wiki/Muthuswami_Dikshitar
[^12]: https://en.wikipedia.org/wiki/Thondaradippodi_Alvar
[^13]: https://sujamusic.wordpress.com/2013/12/31/pacchai-ma-malai/
[^14]: https://sujamusic.wordpress.com/2012/02/08/rangapura-vihara/
[^15]: https://github.com/Euterpea/Euterpea2
