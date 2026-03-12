---
title: Infrastructure, Cloud & DevOps
created: 2026-02-25
source: personal notes (self.md, self-1.md)
---

# Infrastructure, Cloud & DevOps

> Derived from personal notes · Created: 2026-02-25

Notes, links, and resources on cloud infrastructure, DevOps tools, containers, and deployment pipelines.

---

## Nix

**The Determinate Nix Installer · Zero to Nix**
Your guide to learning Nix and flakes
zero-to-nix.com
https://zero-to-nix.com/concepts/nix-installer

Zero to Nix is a guided tutorial for learning Nix from scratch, covering flakes, reproducible development environments, and the Determinate Nix Installer — a more reliable alternative to the official Nix installer with better multi-user and macOS support. **[→ infrastructure-devops; scala-functional-programming]**

## AWS / Cloud

**Introducing Distill CLI: An efficient, Rust-powered tool for media summarization**
Uses AWS services: S3, Transcribe, and Bedrock. Open-source tool written in Rust for summarizing meetings and other media.
allthingsdistributed.com
https://www.allthingsdistributed.com/2024/06/introducing-distill-cli.html

Werner Vogels' blog post introducing Distill CLI — an open-source Rust tool that uses AWS Transcribe for speech-to-text and AWS Bedrock (Claude) for summarisation. A worked example of building a practical AI-powered tool on AWS serverless infrastructure using Rust. **[→ infrastructure-devops; machine-learning-ai]**

## Garmin (fitness + data)

**Garmin Epix Pro In-Depth Review: Now In Three Sizes!**
The Epix AMOLED display-enabled watch in three sizes (42mm, 47mm, 51mm) with flashlight.
www.dcrainmaker.com
https://www.dcrainmaker.com/2023/05/garmin-depth-review-three.html

DC Rainmaker's comprehensive review of the Garmin Epix Pro — the AMOLED display version of Garmin's flagship GPS sports watch — covering accuracy, battery life, display quality, and sport modes across three sizes. The flashlight feature distinguishes it from the Fenix line. **[→ health-fitness]**

**Tips to Improve Accuracy of Pool Swim Activities | Garmin Customer Support**
https://support.garmin.com/en-US/?faq=iS2KcmGiVb4djrE1lri8i7

Garmin support article covering techniques for improving lap count accuracy in pool swimming: correct pool length setup, wrist placement, stroke detection calibration, and when to use open water vs pool mode. **[→ health-fitness]**

**Swim Terminology Used for Garmin Watches and Garmin Connect**
https://support.garmin.com/en-US/?faq=z7QHGpBDDH7wDJsSKjxRi9

Garmin's glossary of swimming metrics — Swolf score, stroke rate, stroke count, distance per stroke, SWOLF — and how they are computed and displayed in Garmin Connect. **[→ health-fitness]**

**Garmin HRM-TRI & HRM-SWIM In-Depth Review**
https://www.dcrainmaker.com/2015/11/garmin-hrm-swimtri-review.html

DC Rainmaker's detailed review of Garmin's dedicated heart rate monitor straps for swimming and triathlon — covering water transmission protocol (ANT+), accuracy in pool vs open water, and compatibility with Garmin devices. **[→ health-fitness]**

**How Garmin Training Load Works: Everything You Need to Know**
https://runningwithrock.com/garmin-training-load/

A thorough explanation of Garmin's Training Load feature — how it calculates acute and chronic training load from heart rate and GPS data, and how the Training Status indicator uses the ratio to assess fitness trajectory. **[→ health-fitness]**

## CI / Build Systems

**sbt-assembly**
https://github.com/sbt/sbt-assembly

The sbt plugin for building fat JARs (uber-JARs) from Scala/Java projects — merging all dependencies into a single executable JAR. Essential for deploying Spark jobs and standalone services without managing a classpath. **[→ scala-functional-programming; infrastructure-devops]**

**scala-cli**
https://scala-cli.virtuslab.org/

Scala CLI is a modern command-line tool for running, compiling, and packaging Scala code — designed as a simpler alternative to sbt for scripts and small projects. Supports Scala 3, direct execution, and packaging to native images. **[→ scala-functional-programming; infrastructure-devops]**

## Electric Vehicles & Mobility

**NIU KQi Air review: My new favorite electric scooter**
Light, fast, and fun.
www.tomsguide.com
https://www.tomsguide.com/home/electric-scooters/niu-kqi-air-review

Tom's Guide review of the NIU KQi Air electric scooter — a lightweight, fast urban commuter scooter. Covers range, top speed, build quality, and ride comfort. NIU is known for quality compared to budget alternatives. **[→ health-fitness; infrastructure-devops]**

**Is An Electric Boat More Dangerous Than a Shark? The Autopian Answers**
https://www.theautopian.com/no-top-is-an-electric-boat-more-dangerous-than-a-shark-trump-asks-the-autopian-answers/

The Autopian's witty rebuttal to a political claim about electric boat danger — using data to compare electrical risks in boats to shark attack statistics. A good example of evidence-based debunking of technology fear-mongering. **[→ miscellaneous]**

**Is this the best personal eVTOL aircraft? | Opener's BlackFly [Pivotal Helix] Innovative Design**
https://youtu.be/FQVAOHxFY0M

A YouTube review of the Opener BlackFly / Pivotal Helix — a single-seat, all-electric vertical takeoff and landing (eVTOL) aircraft designed for personal use without a pilot's licence in the ultralight category. Covers flight characteristics, safety systems, and the regulatory landscape. **[→ health-fitness; miscellaneous]**

**The RoadRower — Deposit**
https://roadrower.com/en-us/products/the-roadrower

The RoadRower is an outdoor exercise machine combining cycling, rowing, and elliptical mechanics — designed for use on roads and paths. A niche piece of exercise equipment for varied outdoor cardio. **[→ health-fitness]**

## Foxconn / Manufacturing

**Foxconn iPhone factory in India (restofworld.org)**
https://restofworld.org/

A Rest of World article on Foxconn's manufacturing expansion into India for iPhone production — covering working conditions, supply chain geopolitics, and India's ambition to become an alternative to China for electronics manufacturing. **[→ miscellaneous]**

## Miscellaneous Tools

**Beyond Power Voltra I home gym review (YouTube)**
https://www.youtube.com/watch?v=6iaeTJzXBV8

A YouTube review of the Beyond Power Voltra I — an all-in-one smart home gym using electronically controlled resistance (not cables or weights), allowing precise resistance programming and workout tracking. **[→ health-fitness]**

**Onyx Boox e-reader community (Reddit)**

Reference to the Reddit community for Onyx Boox e-ink Android tablet/e-reader devices — useful for reading PDFs, academic papers, and books with a note-taking stylus. Popular among academics and heavy readers. **[→ miscellaneous]**

**Impulse (@ImpulseLabs_): Impulse 30" Cooktop — state-of-the-art technology, clean energy future**
https://x.com/ImpulseLabs_/status/1744431456162824450

Impulse Labs' announcement of their high-performance induction cooktop with a built-in battery — enabling electric cooking at power levels previously requiring gas, even on standard household circuits. An example of residential electrification hardware. **[→ miscellaneous]**

**K2 Alexshay Pad Set REI (skating pads)**

Reference to K2's Alexshay protective pad set for inline skating or rollerblading — knee, elbow, and wrist protection for skating sports. **[→ health-fitness]**

---

## From self-1.md (Oct 2024 – Feb 2026)

### AI Coding Tools & Agents

**Thoughts On A Month With Devin**
answer.ai — https://www.answer.ai/posts/2025-01-08-devin.html

Answer.ai's honest retrospective after a month using Devin (Cognition's AI software engineer agent) in real work. Finds Devin impressive for well-scoped isolated tasks but unreliable for complex multi-file refactoring or tasks requiring judgment about existing codebase conventions. **[→ machine-learning-ai; infrastructure-devops]**

**GitHub Copilot for the Command Line**
christianheilmann.com — https://christianheilmann.com/2023/03/29/github-copilot-for-the-command-line-is-amazing/

Christian Heilmann's enthusiasm for GitHub Copilot in the command line — demonstrating how natural language shell assistance reduces the cognitive load of remembering complex command syntax and flags. **[→ infrastructure-devops; machine-learning-ai]**

**Create Apps Without Writing Any Code: DeepSeek-R1 and RooCode**
geeky-gadgets.com — https://www.geeky-gadgets.com/no-code-app-creation-guide/

A tutorial on using RooCode (an agentic coding assistant for VSCode) with DeepSeek-R1 as the backend to generate complete applications from natural language descriptions, demonstrating the no-code frontier of AI-assisted software development. **[→ machine-learning-ai; infrastructure-devops]**

**GitHub - RooVetGit/Roo-Code**
github.com — https://github.com/RooVetGit/Roo-Code

Roo-Code is an open-source agentic coding assistant for VSCode — a fork of Cline with additional features including custom model backends, persistent memory, and workflow automation. Supports DeepSeek, Claude, and other LLMs as the reasoning engine. **[→ machine-learning-ai; infrastructure-devops]**

**Julian Goldie: Deep Seek R1 and RooCode**
x.com — https://x.com/JulianGoldieSEO/status/1884960230804783591

A tweet demonstrating how to use DeepSeek-R1 (a low-cost reasoning model) with RooCode to build complete web applications at minimal cost — part of the wave of "local AI coding" content following DeepSeek's release. **[→ machine-learning-ai]**

**Cline: DeepSeek R1 as 'code archaeologist'**
x.com — https://x.com/thankscline/status/1883201442682720700

Cline's tweet showing DeepSeek-R1 being used as a "code archaeologist" — using the model's reasoning capabilities to navigate and understand large existing codebases rather than generating new code from scratch. **[→ machine-learning-ai; infrastructure-devops]**

**John Rush: Browser-Use tools review**
x.com — https://x.com/johnrushx/status/1883872256121774401

John Rush's evaluation of browser automation tools that allow LLMs to control a web browser — including Browser-Use, Playwright-based agents, and OpenAI's Operator. Compares reliability, cost, and task completion rates. **[→ machine-learning-ai; infrastructure-devops]**

**I replaced CoPilot AI with DeepSeek**
androidauthority.com — https://www.androidauthority.com/deepseek-vs-copilot-3520404/

An Android Authority comparison of DeepSeek vs Microsoft Copilot for daily coding assistance — finding DeepSeek competitive on quality at a fraction of the cost, contributing to discussion of the "DeepSeek moment" in the AI industry. **[→ machine-learning-ai]**

**Tech with Mak: The person who built Claude Code just mass-leaked the thinking behind it**
45 minutes of design decisions, mistakes, and where it's all going — x.com — https://x.com/techNmak/status/2024041443837526375?s=20

A tweet pointing to a 45-minute talk by the Claude Code creator covering the design philosophy, technical decisions, early mistakes, and future direction of Claude Code as an agentic coding tool — one of the most candid insider accounts of AI coding agent design. **[→ machine-learning-ai; infrastructure-devops]**

**Sentient: Anthropic free short course on Claude Code agents**
x.com — https://x.com/sentientt_media/status/2025142906051498085?s=20

A tweet announcing Anthropic's free short course on building and deploying Claude Code agents and skills — covering the Claude Agent SDK, hooks, MCP servers, and workflow automation deployable across Claude Code, API, and VS Code. **[→ machine-learning-ai; infrastructure-devops]**

**Paweł Huryn: Claude Code — The Ultimate Guide for PMs**
x.com — https://x.com/PawelHuryn/status/2025470280945041547?s=20

Paweł Huryn's guide to Claude Code aimed at product managers — explaining how to use Claude Code for product discovery, spec writing, and light coding tasks, bridging the gap between PM workflows and AI-assisted development. **[→ machine-learning-ai; infrastructure-devops]**

**Matthew Berman: OpenClaw (Claude Code) 21 use cases**
x.com — https://x.com/MatthewBerman/status/2023843493765157235?s=20

Matthew Berman's thread listing 21 practical use cases for OpenClaw (a framework built on Claude Code) — ranging from automated PR review and code generation to data analysis pipelines and agent orchestration. **[→ machine-learning-ai; infrastructure-devops]**

**GREG ISENBERG: How to use OpenClaw to spin up 24/7 digital employees**
x.com — https://x.com/gregisenberg/status/2024247983999521123?s=20

Greg Isenberg's thread on building "24/7 digital employees" using OpenClaw — AI agents that continuously monitor, respond, and execute tasks autonomously, enabling small teams to punch above their weight with AI-assisted operations. **[→ machine-learning-ai; infrastructure-devops]**

**Ziwen: How to Run a 24/7 AI Company with OpenClaw for $50/Month**
x.com — https://x.com/ziwenxu_/status/2023610499024171077?s=20

A practical cost breakdown of running continuous AI agent workflows on a Mac Mini using OpenClaw — showing that Claude API costs for autonomous agent operations can be kept under $50/month for a solo founder or small team. **[→ machine-learning-ai; infrastructure-devops]**

**Rishabh: Full OpenClaw Course in 6 Hours**
x.com — https://x.com/Rixhabh__/status/2025844767624700193?s=20

A tweet linking to a 6-hour comprehensive OpenClaw course covering setup, agent design, workflow automation, and real-world use cases — providing structured learning for those wanting to build production Claude Code agentic systems. **[→ machine-learning-ai; infrastructure-devops]**

**GitHub - duolingo/slack-mcp: OAuth-based multi-user Slack MCP server**
github.com — https://github.com/duolingo/slack-mcp

Duolingo's open-source Slack MCP (Model Context Protocol) server with OAuth-based authentication and HTTP transport — enabling AI assistants like Claude to read and write Slack messages as a properly authenticated multi-user service rather than a single bot token. **[→ infrastructure-devops; machine-learning-ai]**

**The Lobster Takeover: Developers Buying Mac Minis to Run Their Own AI Agents**
starryhope.com — https://www.starryhope.com/minipcs/clawdbot-mac-mini-ai-agent-trend/

An article on the trend of developers buying Mac Minis (M4 Pro) as always-on local AI agent servers — running Claude Code, OpenClaw, or other agents continuously at low power cost instead of paying cloud compute rates. **[→ machine-learning-ai; infrastructure-devops]**

**Signal creator Moxie Marlinspike wants to do for AI what he did for messaging**
Introducing Confer, end-to-end AI assistant — arstechnica.com — https://arstechnica.com/security/2026/01/signal-creator-moxie-marlinspike-wants-to-do-for-ai-what-he-did-for-messaging/

Ars Technica on Moxie Marlinspike's new AI assistant Confer — designed with end-to-end encryption and privacy-first architecture so the AI provider cannot read conversation content. Applies Signal's messaging privacy model to LLM assistants. **[→ machine-learning-ai; infrastructure-devops]**

**"SaaS is dying as a business category"**
As AI agents commoditize software — calcalistech.com — https://www.calcalistech.com/ctechnews/article/hjlvyl7lze

An Israeli tech media analysis arguing that AI agents are commoditising SaaS: when AI can perform tasks that previously required specialised software (CRM, project management, etc.), the moat of product-specific workflows erodes. **[→ machine-learning-ai]**

### MCP (Model Context Protocol)

**MCP introduction**
modelcontextprotocol.io — https://modelcontextprotocol.io/introduction

The official introduction to Anthropic's Model Context Protocol (MCP) — an open standard for connecting LLMs to data sources and tools. MCP defines a client-server protocol where MCP servers expose capabilities (tools, resources, prompts) that LLM clients can discover and invoke. **[→ machine-learning-ai; infrastructure-devops]**

**John Rush: What is MCP & why it's a big deal**
x.com — https://x.com/johnrushx/status/1897655569101779201

John Rush's layperson explanation of MCP's significance: by standardising how LLMs connect to external tools, MCP enables an ecosystem where any AI application can use any MCP server — analogous to how USB standardised peripheral connections. **[→ machine-learning-ai; infrastructure-devops]**

### Nix / Build Tools

**Scala Native & Nix - a match made in heaven?**
https://youtu.be/old8N9u3QKU

A YouTube talk exploring the combination of Scala Native (Scala compiled to native code) and Nix (reproducible builds) — arguing that Nix's hermetic builds plus Scala Native's ahead-of-time compilation make for deterministic, fast, containerless Scala deployment. **[→ scala-functional-programming; infrastructure-devops]**

**typelevel-nix**
github.com — https://github.com/typelevel/typelevel-nix

A Nix flake providing development environments for Typelevel Scala projects (Cats, CE3, http4s, etc.) — pre-configured with JDK, sbt, Scala CLI, and Metals LSP, enabling reproducible dev environments with a single `nix develop` command. **[→ scala-functional-programming; infrastructure-devops]**

**Why you should flox every day (Nix/flox)**
etorreborre.blog — https://etorreborre.blog/why-you-should-flox-every-day

Eric Torreborre's blog post on Flox — a user-friendly layer on top of Nix that simplifies managing developer environments while retaining Nix's reproducibility guarantees. Argues daily use of Flox normalises environment-as-code and eliminates "works on my machine" issues. **[→ infrastructure-devops; scala-functional-programming]**

### Rust, Zig & Systems Programming

**[SEI' 24] Modern Systems Programming: Rust and Zig**
https://youtu.be/4aLy6qjhHeo

A Software Engineering Institute 2024 talk comparing Rust and Zig for modern systems programming — covering safety guarantees, performance characteristics, comptime, and which language to choose for different embedded and systems contexts. **[→ scala-functional-programming; infrastructure-devops]**

**Zig And Rust**
matklad.github.io — https://matklad.github.io/2023/03/26/zig-and-rust.html

Matklad's (the main author of rust-analyzer) thoughtful comparison of Zig and Rust: Zig as "better C" with simplicity and comptime; Rust as safe systems programming with ownership — complementary tools for different problem classes. **[→ scala-functional-programming; infrastructure-devops]**

**A new tool for visualizing Rust lifetimes**
https://youtu.be/NV6Xo_el_2o

A YouTube demo of a new IDE tool for visually rendering Rust lifetime annotations on code — helping developers understand borrow checker errors by showing lifetime scopes as overlapping regions rather than text annotations. **[→ scala-functional-programming; infrastructure-devops]**

**C++ to Rust Phrasebook**
A book to help translate C++ idioms into Rust — cel.cs.brown.edu — https://cel.cs.brown.edu/crp/

A Brown University resource mapping C++ idioms to their Rust equivalents — covering RAII, ownership, templates vs generics, exception handling vs Result, and move semantics. Useful for C++ programmers transitioning to Rust. **[→ scala-functional-programming; infrastructure-devops]**

**Forrest: Rust replacing Java and Scala (xAI x-algorithm repo)**
x.com — https://x.com/ForrestPKnight/status/2018768871474315761?s=20

A tweet noting that xAI's x-algorithm repository (the core algorithm powering X/Twitter) is written in Rust — where Java or Scala might have been expected — suggesting Rust's performance and safety advantages are drawing adoption even in traditionally JVM-based domains. **[→ scala-functional-programming; infrastructure-devops]**

**After Three Years, Modular's CUDA Alternative Is Ready**
eetimes.com — https://www.eetimes.com/after-three-years-modulars-cuda-alternative-is-ready/

EE Times reports on Modular's Mojo and MAX platform reaching production readiness — offering a CUDA alternative that runs on diverse hardware (NVIDIA, AMD, Apple Silicon) using a portable compilation stack. **[→ machine-learning-ai; infrastructure-devops]**

**Modular: DeepSeek's Impact on AI (Democratizing AI Compute, Part 1)**
modular.com — https://www.modular.com/blog/democratizing-compute-part-1-deepseeks-impact-on-ai

Modular's analysis of how DeepSeek's efficient training methodology and open-weight release is democratising AI compute — enabling capable models to run on consumer hardware and reducing the cost barrier for AI deployment. **[→ machine-learning-ai; infrastructure-devops]**

### Terminal & Dev Environment

**Ghostty is Probably The Best Terminal Emulator**
https://youtu.be/3wq0RFAvNo

A YouTube review of Ghostty — Mitchell Hashimoto's new GPU-accelerated terminal emulator for macOS and Linux. Combines the speed of Alacritty with the features of Kitty and better macOS integration, using a native rendering engine rather than web technologies. **[→ infrastructure-devops]**

**Programming in the Sun: A Year with the Daylight Computer**
wickstrom.tech — https://wickstrom.tech/2025-10-10-programming-in-the-sun-a-year-with-the-daylight-computer.html

Oskar Wickström's year-long review of the Daylight Computer — an e-ink/LCD hybrid display device designed for outdoor use and reduced eye strain. Evaluates it as a daily programming machine: editing, terminals, and the experience of a sunlight-readable developer environment. **[→ infrastructure-devops]**

### AWS / Cloud / Kubernetes

**10 Tips for AWS Lambda functions performant**
medium.com — https://medium.com/@jake.bazin/10-tips-for-keeping-your-aws-lambda-functions-performant-f0504949659a

A Medium article covering Lambda performance optimisation: cold start reduction (provisioned concurrency, container reuse), memory tuning, connection pooling, efficient serialisation, and avoiding synchronous invocations for long-running tasks. **[→ infrastructure-devops]**

**AI experts return from China stunned: The U.S. grid is so weak, the race may already be over**
Data center infrastructure comparison — fortune.com — https://fortune.com/2025/08/14/data-centers-china-grid-us-infrastructure/

Fortune's alarming report from AI researchers who visited Chinese data center facilities: China's electrical grid infrastructure can support much larger AI training clusters than equivalent US facilities — raising concerns about long-term AI compute capacity parity. **[→ machine-learning-ai; infrastructure-devops]**

**Kubernetes for Scala developers**
rockthejvm.com — https://rockthejvm.com/articles/kubernetes-for-scala-developers

Rock the JVM's guide to Kubernetes from a Scala developer's perspective — covering Pod, Deployment, Service, and ConfigMap concepts with Scala application examples, Helm chart basics, and deployment patterns relevant to Akka/ZIO services. **[→ scala-functional-programming; infrastructure-devops]**

**CNCF Tech Radar Report (Nov 2025)**
cncf.io — https://www.cncf.io/wp-content/uploads/2025/11/cncf_report_techradar_111025a.pdf

The Cloud Native Computing Foundation's November 2025 Technology Radar — surveying cloud native practitioners on Adopt/Trial/Assess/Hold recommendations for tools across observability, platforms, databases, and AI infrastructure. **[→ infrastructure-devops]**

### Electric Vehicles & E-Bikes

**GT73 Electric Dirt Bike 2000W**
amazon.com — https://www.amazon.com/GT73-Electric-Motorcycle-Hydraulic-Suspension/dp/B0DLKY63Q8

An Amazon product listing for the GT73 electric dirt bike — a 2000W off-road electric motorcycle with hydraulic suspension. Noted as a relatively affordable electric off-road option. **[→ health-fitness]**

**Rivian's ALSO E-Bike**
The Coolest E-Bike I've Ever Seen
https://youtu.be/K_vBM5eY_vk

A YouTube review of the ALSO TM-B e-bike from Rivian's micromobility startup — featuring full suspension, a mid-drive motor, and trail-focused geometry. Hailed as unlike any other e-bike due to its mountain bike DNA and Rivian's quality pedigree. **[→ health-fitness]**

**ALSO TM-B In-Depth ($4,500 NextGen Rivian eBike)**
https://youtu.be/9004qAghecM

DC Rainmaker's in-depth review of the ALSO TM-B — Rivian's premium full-suspension e-bike at $4,500. Covers motor performance, battery life, suspension behaviour, and whether the price premium over conventional e-bikes is justified. **[→ health-fitness]**

**Rivian's full-suspension e-bike is like nothing we've seen before**
singletracks.com — https://www.singletracks.com/mtb-gear/the-also-tm-b-is-a-full-suspension-e-bike-unlike-any-other-youve-seen/

Singletracks (mountain bike media) review of the ALSO TM-B from a trail riding perspective — evaluating how the full-suspension design handles technical terrain versus conventional hardtail e-MTBs. **[→ health-fitness]**

**Review: I rode the ALSO TM-B E-Bike: Rivian Micromobility Startup's First EV**
rivianforums.com — https://www.rivianforums.com/forum/threads/review-i-rode-the-also-tm-b-e-bike-rivian-micromobility-startup%E2%80%99s-first-ev.51873/

A Rivian owner community review of the ALSO TM-B e-bike — providing a user perspective from the Rivian enthusiast community, including ride impressions and comparison to other premium e-bikes. **[→ health-fitness]**

**Gearless Magnet Bike**
https://youtu.be/Dg8oVR4k5Dk?si=7lDvJArmgqjV4Ilo

A YouTube video on a gearless bicycle using a magnetic drive system — eliminating the chain and derailleur entirely. Explores how magnetic coupling can transmit power from pedals to wheel without mechanical contact. **[→ health-fitness]**

**The Insane Engineering Of A Land Speed Record Bike**
https://youtu.be/e97w4P0LB0Q?si=BueUijDM0D26mKu-

Real Engineering's breakdown of the engineering behind land speed record bicycles — aerodynamic fairings, recumbent positions, gearing ratios, and how cyclists achieve speeds over 280 km/h (175 mph) with motor pacing. **[→ health-fitness]**

**Bambuk E-Trike Tandem Recumbent Trike**
rad-innovations.com — https://www.rad-innovations.com/bambuk-tandem.html

The Bambuk is a tandem electric recumbent trike — a low-slung, fully faired cargo-capable vehicle for two riders. An unusual category combining the efficiency of recumbent cycling with electric assist and tandem capacity. **[→ health-fitness]**

**Schwinn IC4 Review (2025)**
yourexercisebike.com — https://yourexercisebike.com/schwinn-ic4-review/

A comprehensive review of the Schwinn IC4 indoor cycling bike — covering resistance feel, Bluetooth connectivity (pairs with Peloton, Zwift apps), build quality, and value comparison against the Peloton Bike at roughly one-third the price. **[→ health-fitness]**

**Upgrade Your Indoor Bike with SmartSpin2K V3**
yourexercisebike.com — https://yourexercisebike.com/smartspin2k-guide/

The SmartSpin2K is an aftermarket smart resistance controller that can be retrofitted onto existing spin bikes — adding Bluetooth ERG mode, Zwift compatibility, and automatic resistance control without buying a new smart trainer. **[→ health-fitness]**

**GitHub - Quinus/WhooshConnect: App that uploads MyWhoosh activities to Garmin Connect**
github.com — https://github.com/Quinus/WhooshConnect

An open-source tool for automatically uploading indoor cycling activities from the MyWhoosh virtual cycling platform to Garmin Connect — solving the friction of multi-platform fitness data consolidation. **[→ health-fitness; infrastructure-devops]**

### Home Gym Equipment

**Saris H3 Smart Trainer In-Depth Review**
dcrainmaker.com — https://www.dcrainmaker.com/2019/08/saris-trainer-review.html

DC Rainmaker's thorough review of the Saris H3 direct-drive smart trainer — a Zwift-compatible wheel-off trainer with accurate power measurement, quiet flywheel, and strong ERG mode. **[→ health-fitness]**

**Rogue Echo Bike Review**
morningchalkup.com — https://morningchalkup.com/2022/06/23/rogue-echo-bike-review/

Morning Chalk Up's review of the Rogue Echo Bike — the CrossFit community's favourite air resistance assault bike. Covers build quality, resistance feel, console, and why it's considered the best-in-class for high-intensity conditioning work. **[→ health-fitness]**

**Schwinn's Airdyne AD7 vs Rogue's Echo Bike**
bikevsbike.com — https://bikevsbike.com/schwinns-airdyne-ad7-vs-rogues-echo-bike/

A head-to-head comparison of two iconic air bikes: the Schwinn Airdyne AD7 (the original classic) vs the Rogue Echo Bike (the modern CrossFit standard). Covers resistance curve, durability, seat comfort, and price. **[→ health-fitness]**

**REP Strive Series Curved Treadmill**
repfitness.com — https://repfitness.com/products/rep-strive-series-curved-treadmill?variant=43288603099294

REP Fitness's non-motorised curved treadmill — a manual treadmill where the belt speed responds to the runner's position on the curved surface. Promotes natural running gait and higher metabolic cost than motorised treadmills. **[→ health-fitness]**

**Expert-Tested: Torque Relentless Ripper Review (2025) — SkiErg alternative**
garagegymreviews.com — https://www.garagegymreviews.com/torque-relentless-ripper-review

Garage Gym Reviews' evaluation of the Torque Relentless Ripper — an air-resistance pull-down machine designed as a SkiErg alternative. Tests whether it replicates the cardiovascular and upper body benefits of the Concept2 SkiErg. **[→ health-fitness]**

**The Most Underrated Conditioning Equipment for Home Gyms (Concept 2 SkiErg)**
https://youtu.be/BuhTVvLfCk4

A YouTube video making the case for the Concept2 SkiErg as the most underrated home gym conditioning tool — comparing it to rowing machines and assault bikes for cardiovascular training, lat engagement, and core activation. **[→ health-fitness]**

**Rowing Machine Vs. SkiErg: Which Is Better For Conditioning?**
fitnessprogramer.com — https://fitnessprogramer.com/rowing-machine-vs-skierg/

A structured comparison of indoor rowing and SkiErg for cardiovascular conditioning — muscle groups activated, caloric burn, impact on lower vs upper body, and which to choose for different fitness goals. **[→ health-fitness]**

**Air Bike Vs Stationary Bike: What's the Difference?**
garagegymreviews.com — https://www.garagegymreviews.com/air-bike-vs-stationary-bike

Garage Gym Reviews' comparison of fan-powered air bikes (Rogue Echo, Assault) versus magnetic resistance stationary bikes — covering resistance feel, upper body engagement, caloric burn rate, and suitability for HIIT vs steady-state cardio. **[→ health-fitness]**

**REP AB-3000 2.0 FID Adjustable Weight Bench**
repfitness.com — https://repfitness.com/products/ab-3000-fid-adjustable-bench?variant=42149286772894

REP Fitness's flat-incline-decline adjustable bench — a home gym staple for chest, shoulder, and back pressing exercises. The AB-3000 2.0 is well-regarded for stability and adjustability at a lower price than commercial benches. **[→ health-fitness]**

**WORLDS First ALL ELECTRIC Motorhome (Coachmen RVEX 2026)**
https://youtu.be/0x_ZCLjNnWE

A YouTube video on the Coachmen RVEX 2026 — claimed as the world's first all-electric motorhome, running on a large battery pack without a combustion engine or generator. Covers range, charging infrastructure, and the practical challenges of electric RV travel. **[→ miscellaneous]**

### Garmin & Health Wearables

**How does Garmin measure stress, and is it really accurate?**
digitaltrends.com — https://www.digitaltrends.com/mobile/how-does-garmin-measure-stress/

Digital Trends' investigation into Garmin's stress monitoring — explaining the HRV-based algorithm (Heart Rate Variability derived from GPS watch sensors), its accuracy compared to clinical HRV measurements, and the limitations of wrist-based stress detection. **[→ health-fitness]**

**Why Washington's all-in on smart rings (Oura)**
politico.com — https://www.politico.com/news/2026/02/09/oura-ring-lobbying-rfk-maha-washington-00770320

Politico's report on Oura Ring's successful lobbying efforts in Washington — connecting the health wearable company's growth to the MAHA (Make America Healthy Again) movement and how wearable health data is entering policy discussions. **[→ health-fitness; miscellaneous]**

**Body Pod by Hume Health: In-Home Body Composition Analysis**
humehealth.com — https://humehealth.com/pages/hume-body-pod

The Hume Body Pod is a consumer air displacement plethysmography (ADP) device — the same technology used in clinical BOD POD machines — enabling accurate body composition measurement (fat vs lean mass) at home without a clinic visit. **[→ health-fitness]**
