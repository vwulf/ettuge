<a id="ch1"></a>
# Unix System Programming in OCaml

> Xavier Leroy and Didier Rémy · course notes, English edition · [the PDF in Drive](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view)

Answers to the exercises (PDF pp. 125–138) are not broken down. Each chapter and section also links to the free HTML edition on ocaml.github.io. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A course on Unix system programming that uses OCaml’s Unix library, so each system call is seen through a typed functional interface while the concepts stay the classic ones. It covers files and the file system, processes and their lifecycle, signals, pipes and redirection, sockets for network clients and servers, and threads with locks, conditions and events. Most chapters are built around complete working programs: find, cp, tar, a mini-shell, a parallel sieve, a universal client and server, an HTTP relay. Along the way it is candid about the hard parts: buffering costs, race conditions with signals, and the difficulties of combining threads with Unix calls.

**Contents**

1. [Introduction](ch1): Why Unix programming in OCaml: the system interface shown through a safe, high-level language.
2. [Generalities](ch2): The Sys and Unix modules, program arguments and exit codes, Unix errors as exceptions.
3. [Files](ch3): The file system, descriptors, permissions, directories, reading and writing, buffering, positioning, locks, with find, cp, a buffered I/O library and tar as worked programs.
4. [Processes](ch4): fork, wait and exec, with a mini-shell as the culminating example.
5. [Signals](ch5): Signal delivery, handlers, masking, interaction with system calls, timers, and why signals are hard to use correctly.
6. [Classical inter-process communication: pipes](ch6): Anonymous and named pipes, descriptor redirection, composing pipelines, and multiplexing with select.
7. [Modern communication: sockets](ch7): Sockets: addresses, client and server setup, connection-oriented and connectionless communication, and protocol examples up to HTTP.
8. [Threads](ch8): Threads: creation, joining, mutexes, condition variables, event channels, and how OCaml implements them.
9. [Going further](ch9): Pointers to further topics not covered.


---

## Introduction

*PDF pp. 5–6* · [read online](https://ocaml.github.io/ocamlunix/intro.html)

Why Unix programming in OCaml: the system interface shown through a safe, high-level language.

*Terms:* Unix, OCaml, system programming

→ PDF pp. 5–6 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/intro.html)


---

<a id="ch2"></a>
## Generalities

*PDF pp. 7–12* · [read online](https://ocaml.github.io/ocamlunix/generalities.html#sec3)

The Sys and Unix modules, program arguments and exit codes, Unix errors as exceptions.

**Modules Sys and Unix**  
The Sys and Unix modules.  
*Terms:* Sys module, Unix module  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/generalities.html#sec4)

**Interface with the calling program**  
Command-line arguments, environment, exit codes.  
*Terms:* argv, exit code, environment  
→ PDF p. 8 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/generalities.html#sec5)

**Error handling**  
Unix_error exceptions and handle_unix_error.  
*Terms:* Unix_error, exceptions  
→ PDF p. 9 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/generalities.html#sec7)

**Library functions**  
Library functions versus raw system calls.  
*Terms:* system calls  
→ PDF pp. 10–12 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/generalities.html#sec8)


---

<a id="ch3"></a>
## Files

*PDF pp. 13–44* · [read online](https://ocaml.github.io/ocamlunix/files.html#sec11)

The file system, descriptors, permissions, directories, reading and writing, buffering, positioning, locks, with find, cp, a buffered I/O library and tar as worked programs.

**The file system**  
Inodes, links and the directory tree.  
*Terms:* file system, inode, hard link  
→ PDF pp. 13–14 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec12)

**File names and file descriptors**  
Names versus descriptors.  
*Terms:* file descriptor  
→ PDF p. 15 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec13)

**Meta-attributes, types and permissions**  
stat, file kinds and permission bits.  
*Terms:* stat, permissions, file types  
→ PDF pp. 15–18 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec14)

**Operations on directories**  
Reading directories.  
*Terms:* directories, readdir  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec18)

**Complete example: search in a file hierarchy**  
A find-like recursive search.  
*Terms:* find  
→ PDF pp. 20–21 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec20)

**Opening a file**  
openfile and its flags.  
*Terms:* openfile, open flags  
→ PDF pp. 22–23 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec25)

**Reading and writing**  
read and write on descriptors.  
*Terms:* read, write  
→ PDF pp. 24–25 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec28)

**Closing a descriptor**  
close and descriptor leaks.  
*Terms:* close  
→ PDF p. 26 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec32)

**Complete example: file copy**  
A cp clone.  
*Terms:* file copy, cp  
→ PDF p. 26 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec33)

**The cost of system calls and buffers**  
Why system calls are expensive and buffers help.  
*Terms:* buffering, system call cost  
→ PDF pp. 27–28 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec36)

**Complete example: a small input/output library**  
A small buffered I/O library.  
*Terms:* buffered I/O library  
→ PDF pp. 29–31 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec37)

**Positioning**  
lseek and file offsets.  
*Terms:* lseek  
→ PDF p. 32 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec40)

**Operations specific to certain file types**  
Special files: devices, terminals, symbolic links.  
*Terms:* terminals, devices, symbolic links  
→ PDF pp. 33–35 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec44)

**Locks on files**  
Advisory file locking.  
*Terms:* file locks, lockf  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec50)

**Complete example: recursive copy of files**  
A recursive copy preserving attributes.  
*Terms:* recursive copy  
→ PDF pp. 36–37 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec51)

**Complete example: Tape ARchive**  
A tar implementation.  
*Terms:* tar  
→ PDF pp. 38–44 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/files.html#sec54)


---

<a id="ch4"></a>
## Processes

*PDF pp. 45–52* · [read online](https://ocaml.github.io/ocamlunix/processes.html#sec66)

fork, wait and exec, with a mini-shell as the culminating example.

**Creation of processes**  
fork creates a copy of the process.  
*Terms:* fork  
→ PDF p. 45 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/processes.html#sec67)

**Complete Example: the command leave**  
The leave command as an example.  
*Terms:* process example  
→ PDF p. 45 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/processes.html#sec68)

**Awaiting the termination of a process**  
wait and waitpid, zombies.  
*Terms:* wait, waitpid, zombie  
→ PDF pp. 46–47 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/processes.html#sec69)

**Launching a program**  
exec replaces the program.  
*Terms:* exec  
→ PDF pp. 48–49 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/processes.html#sec71)

**Complete example: a mini-shell**  
A mini-shell combining fork, exec and wait.  
*Terms:* shell  
→ PDF pp. 50–52 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/processes.html#sec75)


---

<a id="ch5"></a>
## Signals

*PDF pp. 53–62* · [read online](https://ocaml.github.io/ocamlunix/signals.html#sec78)

Signal delivery, handlers, masking, interaction with system calls, timers, and why signals are hard to use correctly.

**Default behavior**  
What signals do by default.  
*Terms:* signals  
→ PDF p. 53 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/signals.html#sec79)

**Using signals**  
Sending and catching signals.  
*Terms:* kill, signal handler  
→ PDF p. 54 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/signals.html#sec80)

**Changing the effect of a signal**  
Installing handlers.  
*Terms:* sigaction  
→ PDF pp. 55–56 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/signals.html#sec81)

**How to mask signals**  
Blocking signals with masks.  
*Terms:* signal mask  
→ PDF p. 57 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/signals.html#sec87)

**Signals and system calls**  
Interrupted system calls (EINTR).  
*Terms:* EINTR  
→ PDF pp. 57–58 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/signals.html#sec88)

**The passage of time**  
alarm, sleep and interval timers.  
*Terms:* alarm, timers  
→ PDF pp. 59–60 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/signals.html#sec91)

**Problems with signals**  
Race conditions and why signals are fragile.  
*Terms:* race conditions  
→ PDF pp. 61–62 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/signals.html#sec98)


---

<a id="ch6"></a>
## Classical inter-process communication: pipes

*PDF pp. 63–80* · [read online](https://ocaml.github.io/ocamlunix/pipes.html#sec99)

Anonymous and named pipes, descriptor redirection, composing pipelines, and multiplexing with select.

**Pipes**  
Pipes between processes.  
*Terms:* pipe  
→ PDF pp. 63–64 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/pipes.html#sec100)

**Complete example: parallel sieve of Eratosthenes**  
A pipeline of processes sieving primes.  
*Terms:* sieve of Eratosthenes, concurrency  
→ PDF pp. 65–67 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/pipes.html#sec102)

**Named pipes**  
FIFOs in the file system.  
*Terms:* named pipe, FIFO  
→ PDF p. 68 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/pipes.html#sec107)

**Descriptor redirections**  
dup2 and redirecting standard streams.  
*Terms:* dup2, redirection  
→ PDF pp. 68–70 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/pipes.html#sec108)

**Complete example: composing N commands**  
Building a pipeline of N commands.  
*Terms:* pipeline  
→ PDF p. 71 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/pipes.html#sec114)

**Input/output multiplexing**  
select for waiting on several descriptors.  
*Terms:* select, multiplexing  
→ PDF pp. 72–76 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/pipes.html#sec115)

**Miscellaneous: write**  
Partial writes and how write behaves.  
*Terms:* partial writes  
→ PDF pp. 77–80 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/pipes.html#sec118)


---

<a id="ch7"></a>
## Modern communication: sockets

*PDF pp. 81–104* · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec119)

Sockets: addresses, client and server setup, connection-oriented and connectionless communication, and protocol examples up to HTTP.

**Sockets**  
The socket abstraction.  
*Terms:* sockets  
→ PDF p. 82 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec120)

**Socket creation**  
Creating sockets: domains and types.  
*Terms:* socket domains, socket types  
→ PDF p. 83 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec121)

**Addresses**  
Internet and Unix-domain addresses.  
*Terms:* addresses  
→ PDF p. 84 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec122)

**Connection to a server**  
connect on the client side.  
*Terms:* connect, client  
→ PDF p. 85 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec124)

**Disconnecting sockets**  
shutdown and close.  
*Terms:* shutdown  
→ PDF p. 85 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec125)

**Complete example: the universal client**  
A universal client.  
*Terms:* universal client  
→ PDF pp. 85–86 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec126)

**Establishing a service**  
bind, listen and accept on the server side.  
*Terms:* bind, listen, accept, server  
→ PDF pp. 87–89 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec127)

**Tuning sockets**  
Socket options.  
*Terms:* setsockopt  
→ PDF p. 90 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec128)

**Complete example: the universal server**  
A universal server, forking per connection.  
*Terms:* concurrent server, fork per connection  
→ PDF pp. 90–91 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec130)

**Communication in connectionless mode**  
UDP datagrams.  
*Terms:* UDP, datagrams  
→ PDF p. 92 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec132)

**Low level reads and writes**  
recv and send.  
*Terms:* recv, send  
→ PDF p. 93 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec133)

**High-level primitives**  
establish_server and higher-level helpers.  
*Terms:* establish_server  
→ PDF p. 93 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec134)

**Examples of protocols**  
Protocol design examples.  
*Terms:* protocols  
→ PDF pp. 94–97 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec135)

**Complete example: http requests**  
Making HTTP requests.  
*Terms:* HTTP  
→ PDF pp. 98–104 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/sockets.html#sec142)


---

<a id="ch8"></a>
## Threads

*PDF pp. 105–122* · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec149)

Threads: creation, joining, mutexes, condition variables, event channels, and how OCaml implements them.

**Introduction**  
Threads versus processes.  
*Terms:* threads  
→ PDF p. 105 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec150)

**Creation and termination of threads**  
Creating and ending threads.  
*Terms:* thread creation  
→ PDF p. 106 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec152)

**Waiting**  
Joining and waiting.  
*Terms:* join  
→ PDF pp. 107–110 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec153)

**Synchronization among threads: locks**  
Mutexes.  
*Terms:* mutex, locks  
→ PDF pp. 111–112 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec158)

**Complete example: http relay**  
An HTTP relay with threads.  
*Terms:* HTTP relay  
→ PDF pp. 113–114 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec161)

**Conditions**  
Condition variables.  
*Terms:* condition variables  
→ PDF pp. 115–116 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec164)

**Event-based synchronous communication**  
Event-based communication between threads.  
*Terms:* events, channels  
→ PDF pp. 117–119 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec167)

**Implementation details**  
How threads are implemented in OCaml.  
*Terms:* threads implementation  
→ PDF pp. 120–122 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/threads.html#sec170)


---

<a id="ch9"></a>
## Going further

*PDF pp. 123–143* · [read online](https://ocaml.github.io/ocamlunix/more.html)

Pointers to further topics not covered.

*Terms:* further reading

→ PDF pp. 123–143 in [the PDF](https://drive.google.com/file/d/1qGKx-lgeaigVY217RV6uuZvgBf6GK_M9/view) · [read online](https://ocaml.github.io/ocamlunix/more.html)

