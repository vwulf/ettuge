<a id="ch1"></a>
# The Little Book of Semaphores

> Allen B. Downey · Green Tea Press, 2nd edition · [the PDF in Drive](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

Most problems are presented as puzzle, hint and solution over several pages; the leaves here cover all three. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A puzzle book for learning concurrent programming with one primitive, the semaphore. After defining semaphores and the execution model, Downey builds the standard patterns (signaling, rendezvous, mutex, multiplex, barriers, queues) and then works through dozens of synchronization problems: the classics (producer–consumer, readers–writers, dining philosophers, cigarette smokers), lesser-known ones (barbershops, Santa Claus, H₂O, river crossing, roller coaster) and his own inventions (sushi bar, senate bus, Faneuil Hall). Each problem is posed, hinted and solved in Python-like pseudocode, with attention to deadlock, starvation and fairness. The last chapters translate the ideas into real Python and C with POSIX threads.

**Contents**

1. [Introduction](ch1): Why synchronization is needed when execution order is non-deterministic.
2. [Semaphores](ch2): What a semaphore is and how it is written.
3. [Basic synchronization patterns](ch3): Reusable building blocks for synchronization.
4. [Classical synchronization problems](ch4): The textbook problems and their solutions.
5. [Less classical synchronization problems](ch5): Less familiar problems that combine the basic patterns.
6. [Not-so-classical problems](ch6): Problems that need more careful categorical exclusion.
7. [Not remotely classical problems](ch7): The author’s original problems.
8. [Synchronization in Python](ch8): Running the patterns with Python threads.
9. [Synchronization in C](ch9): The same ideas in C with POSIX threads.
10. [Cleaning up Python threads](ch10): Utility code for Python examples.
11. [Cleaning up POSIX threads](ch11): Utility code for C examples.


---

## Introduction

*PDF pp. 13–18*

Why synchronization is needed when execution order is non-deterministic.

**Synchronization**  
Serialization and mutual exclusion as the two goals.  
*Terms:* synchronization, serialization, mutual exclusion  
→ PDF p. 13 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Execution model**  
The model: threads, interleavings, and what can be assumed.  
*Terms:* execution model, interleaving  
→ PDF pp. 13–14 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Serialization with messages**  
Coordinating with messages.  
*Terms:* message passing  
→ PDF p. 15 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Non-determinism**  
Why concurrent programs are hard to test.  
*Terms:* non-determinism  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Shared variables**  
Shared variables and race conditions.  
*Terms:* shared variables, race condition  
→ PDF pp. 16–18 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch2"></a>
## Semaphores

*PDF pp. 19–22*

What a semaphore is and how it is written.

**Definition**  
A counter with wait and signal operations that block when negative.  
*Terms:* semaphore, wait, signal, P, V  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Syntax**  
The notation used in the book.  
*Terms:* notation  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Why semaphores?**  
Why semaphores make constraints explicit and correct.  
*Terms:* rationale  
→ PDF pp. 21–22 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch3"></a>
## Basic synchronization patterns

*PDF pp. 23–66*

Reusable building blocks for synchronization.

**Signaling**  
One thread signals another that an event happened.  
*Terms:* signaling  
→ PDF p. 23 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Sync.py**  
A simulator for running the solutions.  
*Terms:* Sync.py, simulation  
→ PDF p. 24 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Rendezvous**  
Two threads wait for each other.  
*Terms:* rendezvous  
→ PDF pp. 24–27 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Mutex**  
A mutex as a semaphore initialized to one.  
*Terms:* mutex  
→ PDF pp. 28–30 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Multiplex**  
Allowing up to n threads in a critical section.  
*Terms:* multiplex  
→ PDF pp. 31–32 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Barrier**  
Making all threads wait until everyone arrives.  
*Terms:* barrier, turnstile  
→ PDF pp. 33–42 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Reusable barrier**  
A barrier that can be used repeatedly (two-phase turnstile).  
*Terms:* reusable barrier, two-phase barrier  
→ PDF pp. 43–56 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Queue**  
Pairing threads from two queues.  
*Terms:* queue, pairing  
→ PDF pp. 57–66 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch4"></a>
## Classical synchronization problems

*PDF pp. 67–126*

The textbook problems and their solutions.

**Producer-consumer problem**  
Bounded buffers between producers and consumers.  
*Terms:* producer-consumer, bounded buffer  
→ PDF pp. 67–76 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Readers-writers problem**  
Many readers or one writer, with lightswitch and starvation-free variants.  
*Terms:* readers-writers, lightswitch, writer starvation  
→ PDF pp. 77–92 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**No-starve mutex**  
A mutex that never starves a waiting thread (Morris).  
*Terms:* no-starve mutex, Morris algorithm  
→ PDF pp. 93–98 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Dining philosophers**  
Philosophers sharing forks without deadlock or starvation.  
*Terms:* dining philosophers, deadlock  
→ PDF pp. 99–112 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Cigarette smokers problem**  
Matching agents and smokers who need different ingredients.  
*Terms:* cigarette smokers problem  
→ PDF pp. 113–126 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch5"></a>
## Less classical synchronization problems

*PDF pp. 127–176*

Less familiar problems that combine the basic patterns.

**The dining savages problem**  
Savages eating from a pot that a cook refills.  
*Terms:* dining savages  
→ PDF pp. 127–132 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The barbershop problem**  
A barber, waiting chairs and customers who leave when full.  
*Terms:* barbershop problem  
→ PDF pp. 133–138 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The FIFO barbershop**  
Serving customers in arrival order.  
*Terms:* FIFO  
→ PDF pp. 139–144 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Hilzer's Barbershop problem**  
A larger barbershop with sofa and multiple barbers.  
*Terms:* Hilzer barbershop  
→ PDF pp. 145–148 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The Santa Claus problem**  
Santa waking for reindeer or groups of elves.  
*Terms:* Santa Claus problem  
→ PDF pp. 149–154 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Building H2O**  
Combining two hydrogen threads with one oxygen.  
*Terms:* H2O, building molecules  
→ PDF pp. 155–159 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**River crossing problem**  
Forming boatloads under group constraints.  
*Terms:* river crossing  
→ PDF pp. 160–164 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The roller coaster problem**  
Passengers and a car that runs only when full.  
*Terms:* roller coaster problem  
→ PDF pp. 165–176 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch6"></a>
## Not-so-classical problems

*PDF pp. 177–194*

Problems that need more careful categorical exclusion.

**The search-insert-delete problem**  
Searchers, inserters and deleters on a shared list.  
*Terms:* search-insert-delete, categorical mutual exclusion  
→ PDF pp. 177–181 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The unisex bathroom problem**  
Exclusion between categories without starvation.  
*Terms:* unisex bathroom, starvation  
→ PDF pp. 182–188 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Baboon crossing problem**  
Baboons crossing a rope in one direction at a time.  
*Terms:* baboon crossing  
→ PDF p. 189 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The Modus Hall Problem**  
Tracking which group holds the majority.  
*Terms:* Modus Hall, majority  
→ PDF pp. 190–194 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch7"></a>
## Not remotely classical problems

*PDF pp. 195–250*

The author’s original problems.

**The sushi bar problem**  
Seats that empty fully before new diners join.  
*Terms:* sushi bar  
→ PDF pp. 195–205 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The child care problem**  
Keeping an adult-to-child ratio.  
*Terms:* child care, ratio  
→ PDF pp. 206–216 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The room party problem**  
A dean entering a party under conditions.  
*Terms:* room party  
→ PDF pp. 217–222 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The Senate Bus problem**  
Riders boarding a bus that leaves when full or empty.  
*Terms:* Senate Bus  
→ PDF pp. 223–230 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The Faneuil Hall problem**  
Immigrants, judges and spectators at a ceremony.  
*Terms:* Faneuil Hall  
→ PDF pp. 231–240 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Dining Hall problem**  
Students who must not eat alone.  
*Terms:* dining hall  
→ PDF pp. 241–250 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch8"></a>
## Synchronization in Python

*PDF pp. 251–264*

Running the patterns with Python threads.

**Mutex checker problem**  
Checking that a mutex really excludes.  
*Terms:* Python threading, mutex checker  
→ PDF pp. 252–258 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**The coke machine problem**  
A coke machine as a bounded buffer.  
*Terms:* coke machine, bounded buffer  
→ PDF pp. 259–264 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch9"></a>
## Synchronization in C

*PDF pp. 265–282*

The same ideas in C with POSIX threads.

**Mutual exclusion**  
Mutual exclusion in C.  
*Terms:* C, pthreads, mutex  
→ PDF pp. 265–272 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Make your own semaphores**  
Building semaphores from mutexes and condition variables.  
*Terms:* semaphore implementation, condition variable  
→ PDF pp. 273–282 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch10"></a>
## Cleaning up Python threads

*PDF pp. 283–286*

Utility code for Python examples.

**Semaphore methods**  
Wrapping semaphore methods.  
*Terms:* Python semaphore  
→ PDF p. 283 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Creating threads**  
Starting threads.  
*Terms:* threads  
→ PDF p. 283 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Handling keyboard interrupts**  
Exiting cleanly on Ctrl-C.  
*Terms:* KeyboardInterrupt  
→ PDF pp. 284–286 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)


---

<a id="ch11"></a>
## Cleaning up POSIX threads

*PDF pp. 287–291*

Utility code for C examples.

**Compiling Pthread code**  
Compiler flags for pthreads.  
*Terms:* pthread compilation  
→ PDF p. 287 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Creating threads**  
pthread_create.  
*Terms:* pthread_create  
→ PDF pp. 288–289 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Joining threads**  
pthread_join.  
*Terms:* pthread_join  
→ PDF p. 290 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

**Semaphores**  
POSIX semaphores.  
*Terms:* sem_t, POSIX semaphores  
→ PDF pp. 290–291 in [the PDF](https://drive.google.com/file/d/1mo1TxMNkZvsp_l0vkHuT5KNSpQShBkfH/view)

