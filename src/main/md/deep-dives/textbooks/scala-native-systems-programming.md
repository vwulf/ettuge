<a id="ch1"></a>
# Modern Systems Programming with Scala Native

> Richard Whaling · Pragmatic Bookshelf, 2020 (P1.0) · [the PDF in Drive](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Whaling teaches systems programming in Scala by compiling to native code with Scala Native, which gives direct access to C’s memory model and the POSIX APIs without a JVM. Part I works at the level of C: raw input and output, pointers, structs and manual heap allocation, a hand-written HTTP client, a minimal shell built on fork and exec, and a blocking TCP server. Part II rebuilds those tools on modern foundations: an event loop on libuv, futures and asynchronous patterns for distributed programs, streaming pipes over files and sockets, an embedded key-value database (LMDB) for durability, and finally composing it all into networked services. An appendix sets up the toolchain on macOS or in Docker.

**Contents**

1. [Systems Programming in the Twenty-First Century](ch1): What systems programming means today and why a high-level language compiled to native code fits it.
2. [Part I—Foundations of Systems Programming](ch2): C-style programming in Scala: I/O, memory, a network client, processes and a server.
3. [Part II—Modern Systems Programming](ch3): Asynchronous I/O, futures, streams, persistence and services on top of an event loop.
4. [A1. Setting Up the Environment](ch4): Installing Scala Native locally or running it in Docker.


---

## Systems Programming in the Twenty-First Century

*PDF pp. 18–23*

What systems programming means today and why a high-level language compiled to native code fits it.

**What Is Systems Programming?**  
Definitions and scope.  
*Terms:* systems programming  
→ PDF p. 18 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**Moving Toward Modern Systems Programming**  
From C to modern systems languages.  
*Terms:* C, modern systems languages  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**Why Scala Native?**  
Why Scala Native: native performance with Scala’s abstractions.  
*Terms:* Scala Native, LLVM  
→ PDF pp. 20–21 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**What Makes Scala Native Different**  
What differs from Scala on the JVM.  
*Terms:* JVM differences  
→ PDF pp. 22–23 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)


---

<a id="ch2"></a>
## Part I—Foundations of Systems Programming

*PDF pp. 24–118*

C-style programming in Scala: I/O, memory, a network client, processes and a server.

**1. The Basics: Input and Output**  
Reading and writing with C’s stdio from Scala, strings as pointers.  
*Terms:* stdio, CString, Ptr, I/O  
→ PDF pp. 25–45 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**2. Arrays, Structs, and the Heap**  
Pointer arithmetic, arrays, structs, malloc and manual memory management, with a large-data sorting example.  
*Terms:* pointers, structs, malloc, heap, qsort  
→ PDF pp. 46–64 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**3. Writing a Simple HTTP Client**  
A minimal HTTP client written directly against sockets.  
*Terms:* HTTP client, sockets  
→ PDF pp. 65–87 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**4. Managing Processes: A Deconstructed Shell**  
fork, exec, wait and pipes, assembled into a small shell.  
*Terms:* fork, exec, wait, pipe, shell  
→ PDF pp. 88–103 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**5. Writing a Server the Old-Fashioned Way**  
A blocking TCP server in the classic style.  
*Terms:* TCP server, blocking I/O  
→ PDF pp. 104–118 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)


---

<a id="ch3"></a>
## Part II—Modern Systems Programming

*PDF pp. 119–223*

Asynchronous I/O, futures, streams, persistence and services on top of an event loop.

**6. Doing I/O Right, with Event Loops**  
Non-blocking I/O with libuv and its event loop.  
*Terms:* libuv, event loop, non-blocking I/O  
→ PDF pp. 120–146 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**7. Functions and Futures: Patterns for Distributed Services**  
Futures and callbacks for distributed work.  
*Terms:* futures, callbacks, async  
→ PDF pp. 147–170 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**8. Streaming with Pipes and Files**  
Streaming data through pipes from files and sockets.  
*Terms:* streaming, pipes, backpressure  
→ PDF pp. 171–191 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**9. Durability: An Embedded Key-Value Database with LMDB**  
Persisting data with an embedded LMDB key-value store.  
*Terms:* LMDB, key-value store, durability  
→ PDF pp. 192–204 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**10. Services: Encapsulation and Abstraction for Modern Designs**  
Building networked services with clean abstractions.  
*Terms:* services, abstraction  
→ PDF pp. 205–223 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)


---

<a id="ch4"></a>
## A1. Setting Up the Environment

*PDF pp. 224–229*

Installing Scala Native locally or running it in Docker.

**Running Scala Native on Mac OS**  
macOS setup.  
*Terms:* macOS  
→ PDF p. 224 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**Why Use Containers?**  
Why use containers.  
*Terms:* containers  
→ PDF p. 225 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**Installing and Configuring Docker**  
Docker installation.  
*Terms:* Docker  
→ PDF p. 226 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

**Running Scala Native in Docker**  
Building and running in Docker.  
*Terms:* Docker build  
→ PDF pp. 227–229 in [the PDF](https://drive.google.com/file/d/1uaUINnw9-U9ZBLA8OoqtxfN_H4I65T67/view)

