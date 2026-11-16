<a id="ch1"></a>
# Pragmatic Type-Level Design

> Alexander Granin · self-published (Leanpub), v1.1.0 · [the PDF in Drive](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

The per-chapter “Summary” subsections, the Typed Forms diagram reference (Appendix A) and the two project appendices (D, E) are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A practical guide to using type-level programming for application design rather than for its own sake, with Haskell as the main language and Rust and Scala 3 counterparts. Granin introduces his “Typed Forms” diagram notation, then works through use cases: extensibility via type classes and existential or “valuefied” storage, genericity with empty ADTs, kinds and type-level lists, and correctness via static integrity checks and type-level validators. He moves on to application architecture and component design (static vs. dynamic domain models, free monads vs. type-class interfaces, his Granular Type Selector and Dynamic Payload patterns), then advanced cases: type-level object models and the expression problem. “Rosetta Stone” chapters map every technique to Rust and Scala 3.

**Contents**

1. [Chapter 1: Emergent type-level design](ch1): What type-level design is and the vocabulary used.
2. [Chapter 2: Use case: simple extensibility](ch2): Extensibility through type classes and heterogeneous storage.
3. [Chapter 3: Use case: genericity and customization](ch3): Genericity and customization at the type level.
4. [Chapter 4: Use case: enforcing correctness](ch4): Using types to enforce correctness.
5. [Chapter 5: Application architecture](ch5): Architecture for type-level applications.
6. [Chapter 6: Components design](ch6): Designing components with static and dynamic models.
7. [Chapter 7: Use case: type-level object-oriented programming](ch7): Type-level object-oriented programming.
8. [Chapter 8: Use case: advanced extensibility](ch8): Advanced extensibility with type-level interfaces.
9. [Rosetta Stone 1: Rust](ch9): The same techniques in Rust.
10. [Rosetta Stone 2: Scala 3](ch10): The same techniques in Scala 3.
11. [Appendix B: Existential Fight Club](ch11): One problem solved with existentials vs.
12. [Appendix C: The Mythologized Correctness](ch12): A critical look at claims about type safety and correctness.


---

## Chapter 1: Emergent type-level design

*PDF pp. 13–46*

What type-level design is and the vocabulary used.

**1.1 Approaching the type-level design**  
Types vs. values, pragmatism and the Typed Forms diagrams.  
*Terms:* type-level design, types and values, Typed Forms diagrams  
→ PDF pp. 15–28 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**1.2 The foreshadowing of type-level design**  
Generics, type classes, design principles and type-level literals.  
*Terms:* generics, type classes, type-level literals, design principles  
→ PDF pp. 29–46 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch2"></a>
## Chapter 2: Use case: simple extensibility

*PDF pp. 47–76*

Extensibility through type classes and heterogeneous storage.

**2.1 Extensibility**  
Extensibility mechanisms and extension points.  
*Terms:* extensibility, extension points  
→ PDF pp. 48–57 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**2.2 Basically extensible application**  
A type-class-based extensible app; storing heterogeneous values by valuefication or existentials.  
*Terms:* type class interface, heterogeneous collections, existential types, valuefication  
→ PDF pp. 58–76 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch3"></a>
## Chapter 3: Use case: genericity and customization

*PDF pp. 77–111*

Genericity and customization at the type level.

**3.1 Type-level genericity**  
Empty ADTs, type applications, kinds, custom kinds, type-level lists.  
*Terms:* empty data types, TypeApplications, kinds, DataKinds, type-level lists  
→ PDF pp. 79–97 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**3.2 Type-level customization**  
Case-driven design and a customizable type-level eDSL.  
*Terms:* case-driven design, eDSL  
→ PDF pp. 98–111 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch4"></a>
## Chapter 4: Use case: enforcing correctness

*PDF pp. 112–138*

Using types to enforce correctness.

**4.1 Correctness is about meaning**  
Type safety vs. correctness.  
*Terms:* correctness, type safety  
→ PDF pp. 113–117 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**4.2 Static integrity**  
Static integrity: stronger domain models, static vs. volatile notions, type-level validators.  
*Terms:* static integrity, type-level validation, domain modeling  
→ PDF pp. 118–138 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch5"></a>
## Chapter 5: Application architecture

*PDF pp. 140–163*

Architecture for type-level applications.

**5.1 Approaching software architecture**  
Architecture levels and assessment practices.  
*Terms:* software architecture, Double Usage Assessment  
→ PDF pp. 141–148 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**5.2 Application structure**  
Layered architecture, project structure, where type-level code lives.  
*Terms:* layered architecture, project structure  
→ PDF pp. 149–163 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch6"></a>
## Chapter 6: Components design

*PDF pp. 164–191*

Designing components with static and dynamic models.

**6.1 Static and dynamic domain models**  
Separate type- and value-level models, Granular Type Selector, static materialization, DTOs.  
*Terms:* static model, dynamic model, Granular Type Selector, materialization, DTO  
→ PDF pp. 165–178 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**6.2 Two functional interfaces**  
Free monad vs. type-class interfaces; Dynamic Payload pattern.  
*Terms:* free monad, type class interface, Dynamic Payload  
→ PDF pp. 179–191 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch7"></a>
## Chapter 7: Use case: type-level object-oriented programming

*PDF pp. 193–218*

Type-level object-oriented programming.

**7.1 Multiparadigm approach**  
Multiparadigm motivation.  
*Terms:* multiparadigm  
→ PDF p. 195 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**7.2 Glimpse of typed object-oriented programming**  
Typed OOP glimpse and the expression problem.  
*Terms:* typed OOP, expression problem  
→ PDF pp. 195–201 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**7.3 Type-oriented object model**  
A type-oriented object model with scripting and the Typed-Untyped pattern.  
*Terms:* object model, Typed-Untyped pattern  
→ PDF pp. 202–218 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch8"></a>
## Chapter 8: Use case: advanced extensibility

*PDF pp. 219–244*

Advanced extensibility with type-level interfaces.

**8.1 Advanced type-level design and extensibility**  
Empty parameterized ADTs, type-level interfaces, universal evaluation, type-level lambdas and the expression problem.  
*Terms:* type-level interfaces, evaluation mechanism, expression problem, type-level lambdas  
→ PDF pp. 221–244 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch9"></a>
## Rosetta Stone 1: Rust

*PDF pp. 249–289*

The same techniques in Rust.

**RSC.1.1 Value-level and mixed-level features**  
Newtypes, ADTs, traits, phantom types, generics.  
*Terms:* Rust, newtype, traits, phantom types  
→ PDF pp. 251–259 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**RSC.1.2 Type-level features**  
Const generics, type-level lists and associated types.  
*Terms:* type-level literals, associated types  
→ PDF pp. 260–271 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**RSC.1.3 Type-level interfaces, extensibility, and domain modeling**  
Existential wrappers and evaluation.  
*Terms:* trait objects, existential wrappers  
→ PDF pp. 272–280 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**RSC.1.4 Integrity validation**  
Type equality and static asserts.  
*Terms:* type equality, static assert  
→ PDF pp. 281–289 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch10"></a>
## Rosetta Stone 2: Scala 3

*PDF pp. 290–322*

The same techniques in Scala 3.

**RSC.2.1 Value-level and mixed-level features**  
Opaque types, ADTs, traits and type classes.  
*Terms:* Scala 3, opaque types, given, type classes  
→ PDF pp. 292–299 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**RSC.2.2 Type-level features**  
Singleton literal types, type-level lists, match types.  
*Terms:* literal types, match types  
→ PDF pp. 300–308 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**RSC.2.3 Type-level interfaces, extensibility, and domain modeling**  
Type-level interfaces and existential wrappers.  
*Terms:* existential types  
→ PDF pp. 309–316 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**RSC.2.4 Integrity validation**  
Validators and type comparison.  
*Terms:* type comparison, validators  
→ PDF pp. 317–322 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch11"></a>
## Appendix B: Existential Fight Club

*PDF pp. 339–353*

One problem solved with existentials vs. values across languages.

**B.1 Haskell, existentification**  
Haskell existentials.  
*Terms:* Haskell existential  
→ PDF pp. 340–341 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**B.2 Haskell, valuefication**  
Haskell valuefication.  
*Terms:* valuefication  
→ PDF p. 342 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**B.3 Rust, existentification**  
Rust existentials.  
*Terms:* Rust dyn trait  
→ PDF pp. 343–344 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**B.4 Rust, valuefication**  
Rust valuefication.  
*Terms:* Rust  
→ PDF p. 345 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**B.5 C++, object-oriented variant**  
C++ OOP.  
*Terms:* C++ virtual  
→ PDF pp. 346–348 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**B.6 C++, valuefication**  
C++ valuefication.  
*Terms:* C++  
→ PDF pp. 349–350 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**B.7 Scala 2, existentification with implicits**  
Scala 2 implicits.  
*Terms:* Scala implicits  
→ PDF pp. 351–353 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)


---

<a id="ch12"></a>
## Appendix C: The Mythologized Correctness

*PDF pp. 354–372*

A critical look at claims about type safety and correctness.

**C.1 Type safety**  
What type safety does and doesn’t guarantee.  
*Terms:* type safety myths  
→ PDF pp. 355–359 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

**C.2 Technical correctness**  
Technical correctness and its limits.  
*Terms:* correctness  
→ PDF pp. 360–371 in [the PDF](https://drive.google.com/file/d/1NM0rrnQD-TtN9vawt-_R13Rtril-8L3A/view)

