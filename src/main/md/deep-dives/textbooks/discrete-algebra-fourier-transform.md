<a id="ch1"></a>
# The Discrete Algebra of the Fourier Transform

> Gabriel Peyré · English translation of “L’algèbre discrète de la transformée de Fourier” · [the PDF in Drive](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

Exercise solutions and the Matlab/Maple listings at the end (PDF pp. 221–296) are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An algebraic treatment of Fourier analysis in the finite setting. Peyré starts from duality on finite groups (characters, the dual group, Fourier transform and Plancherel), applies it to Gauss sums, the Walsh transform and Poisson summation, and then develops the discrete Fourier transform for signal processing: the FFT, circular convolution, multidimensional transforms, filtering, solving differential equations and fast multiplication. Later chapters extend the idea to the Hartley, Z and fractional Fourier transforms, to transforms over finite fields and rings with error-correcting codes, and finally to linear representations of finite non-abelian groups, characters and their applications.

**Contents**

1. [Fourier transform on a finite group](ch1): Characters of finite groups and the Fourier transform they define.
2. [Applications of duality on a finite group](ch2): Number-theoretic and combinatorial applications of duality.
3. [Discrete Fourier transform](ch3): The DFT as used in signal processing, and its fast algorithm.
4. [Applications of the discrete Fourier transform](ch4): Using the DFT to approximate, filter, solve and multiply.
5. [Extension of the notion of Fourier transform](ch5): Other transforms in the same family.
6. [Fourier transform with values in a finite field](ch6): Fourier transforms over finite fields and rings, and error-correcting codes.
7. [Linear representations of finite groups](ch7): Representations of non-abelian finite groups as the general setting for Fourier analysis.
8. [Applications of linear representations](ch8): Applying representation theory.


---

## Fourier transform on a finite group

*PDF pp. 9–30*

Characters of finite groups and the Fourier transform they define.

**Dual of a finite group**  
The dual of a finite group.  
*Terms:* dual group, characters  
→ PDF pp. 9–12 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Dual of an abelian group**  
Characters of abelian groups and the structure of the dual.  
*Terms:* abelian groups  
→ PDF pp. 13–16 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Dual of a non-commutative group**  
The non-commutative case.  
*Terms:* non-abelian groups  
→ PDF pp. 17–18 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Fourier transform**  
Fourier transform, inversion and Plancherel.  
*Terms:* Fourier transform, Plancherel, inversion  
→ PDF pp. 19–23 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)


---

<a id="ch2"></a>
## Applications of duality on a finite group

*PDF pp. 31–64*

Number-theoretic and combinatorial applications of duality.

**Gaussian sums**  
Quadratic Gauss sums and quadratic reciprocity.  
*Terms:* Gauss sums, quadratic reciprocity  
→ PDF pp. 31–41 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Walsh transform**  
The Walsh–Hadamard transform on Boolean cubes.  
*Terms:* Walsh transform, Hadamard  
→ PDF pp. 42–44 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Poisson formula**  
The Poisson summation formula and its uses.  
*Terms:* Poisson summation  
→ PDF pp. 45–52 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)


---

<a id="ch3"></a>
## Discrete Fourier transform

*PDF pp. 65–92*

The DFT as used in signal processing, and its fast algorithm.

**The language of signal processing**  
Signals, sampling and spectra.  
*Terms:* signal processing, sampling  
→ PDF p. 65 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Fast Fourier transform**  
Cooley–Tukey FFT and its complexity.  
*Terms:* FFT, Cooley-Tukey  
→ PDF pp. 66–73 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Circular convolution**  
Circular convolution and the convolution theorem.  
*Terms:* circular convolution, convolution theorem  
→ PDF pp. 74–76 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**In higher dimension**  
Multidimensional DFTs.  
*Terms:* 2D DFT  
→ PDF pp. 77–79 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Symmetry and discrete transform**  
Symmetric signals and related transforms.  
*Terms:* symmetry  
→ PDF pp. 80–81 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)


---

<a id="ch4"></a>
## Applications of the discrete Fourier transform

*PDF pp. 93–124*

Using the DFT to approximate, filter, solve and multiply.

**Link with the Fourier transform on R**  
Approximating the continuous Fourier transform.  
*Terms:* Fourier transform on R, aliasing  
→ PDF pp. 93–96 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Filtering**  
Linear filters.  
*Terms:* filtering  
→ PDF pp. 97–100 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Geometric aspects of filtering**  
Filtering seen geometrically.  
*Terms:* geometric filtering  
→ PDF pp. 101–105 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Numerical solution of derivative equations by tials**  
Solving differential equations such as Poisson and heat equations spectrally.  
*Terms:* spectral methods, Poisson equation, heat equation  
→ PDF pp. 106–111 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Product calculations**  
Fast polynomial and big-integer multiplication.  
*Terms:* fast multiplication, big integers  
→ PDF pp. 112–114 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)


---

<a id="ch5"></a>
## Extension of the notion of Fourier transform

*PDF pp. 125–148*

Other transforms in the same family.

**Hartley transform**  
The real-valued Hartley transform.  
*Terms:* Hartley transform  
→ PDF pp. 125–128 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Z transform and applications**  
The Z transform for recurrences and filters.  
*Terms:* Z transform, recurrences  
→ PDF pp. 129–135 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Vectorial Z Transform**  
A vector version of the Z transform.  
*Terms:* vectorial Z transform  
→ PDF pp. 136–138 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Fractional Fourier transform**  
The fractional Fourier transform.  
*Terms:* fractional Fourier transform  
→ PDF pp. 139–141 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)


---

<a id="ch6"></a>
## Fourier transform with values in a finite field

*PDF pp. 149–178*

Fourier transforms over finite fields and rings, and error-correcting codes.

**Finite field calculations**  
Arithmetic in finite fields and roots of unity.  
*Terms:* finite fields, roots of unity  
→ PDF pp. 149–152 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Calculations on a ring**  
Transforms over rings (number-theoretic transforms).  
*Terms:* number theoretic transform  
→ PDF pp. 153–155 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Application to correction codes**  
Cyclic and BCH codes via the transform.  
*Terms:* error-correcting codes, BCH codes, cyclic codes  
→ PDF pp. 156–166 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Correction codes and duality on a finite abelian group**  
MacWilliams-style duality for codes.  
*Terms:* MacWilliams identity, duality  
→ PDF pp. 167–171 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)


---

<a id="ch7"></a>
## Linear representations of finite groups

*PDF pp. 179–206*

Representations of non-abelian finite groups as the general setting for Fourier analysis.

**First definitions**  
Representations and their basic constructions.  
*Terms:* group representation  
→ PDF pp. 179–186 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Invariance and representations**  
Invariant subspaces and irreducibility (Maschke, Schur).  
*Terms:* irreducible representation, Maschke, Schur lemma  
→ PDF pp. 187–188 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Characters**  
Characters and orthogonality.  
*Terms:* characters, orthogonality relations  
→ PDF pp. 189–191 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Representations and enumeration**  
Counting with representations.  
*Terms:* enumeration  
→ PDF pp. 192–193 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Fourier Theory**  
Fourier theory for non-abelian groups.  
*Terms:* non-abelian Fourier transform  
→ PDF pp. 194–198 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)


---

<a id="ch8"></a>
## Applications of linear representations

*PDF pp. 207–220*

Applying representation theory.

**Representation of classic groups**  
Representations of symmetric and dihedral groups.  
*Terms:* symmetric group, dihedral group  
→ PDF pp. 207–210 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**The question of simplicity**  
Using characters to test simplicity of groups.  
*Terms:* simple groups  
→ PDF pp. 211–212 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

**Spectral analysis**  
Spectral analysis of data on groups.  
*Terms:* spectral analysis  
→ PDF pp. 213–216 in [the PDF](https://drive.google.com/file/d/1Jqw9puCT2NbLmpaNk4HOQZCkRtXgPh8W/view)

