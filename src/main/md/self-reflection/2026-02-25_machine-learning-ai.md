---
title: Machine Learning & AI
created: 2026-02-25
source: ../self.md
---

# Machine Learning & AI

> Derived from [`self.md`](../self.md) · Created: 2026-02-25

Links, notes, papers, and code snippets on LLMs, RAG, fine-tuning, neural architectures, and AI infrastructure.

---

## Large Language Models — Foundations

Cameron R. Wolfe: Training specialized LLMs
https://cameronrwolfe.substack.com/

Attention in transformers, visually explained (3Blue1Brown Chapter 6)
https://www.youtube.com/watch?v=eMlx5fFNoYc

Deep Learning Foundations by Soheil Feizi: Large Language Models Part II (YouTube)
https://www.youtube.com/watch?v=2yjzZfDQxy8

A Primer on Inner Workings of Transformer-based Language Models
arxiv 2405.00208
https://arxiv.org/abs/2405.00208

What is ChatGPT doing and why does it work? (Wolfram Media)
https://www.wolfram-media.com/products/what-is-chatgpt-doing-and-why-does-it-work/

Petar Velickovic: Transformers and GNNs softmax issue

Model Parallelism chapter ML Engineering (Stas Bekman tweet)

Machine Learning Street Talk: Control Theory of LLM Prompting
LLM Control Theory paper (Aman Bhargava)

## RAG — Retrieval-Augmented Generation

DSPy paper — Declarative Language Model Calls into Self-Improving Pipelines
arxiv 2310.03714
https://arxiv.org/abs/2310.03714

Bill Chambers: Gentle intro to DSPy

Santiago (@svpino) RAG tutorials (multiple tweets)
https://twitter.com/svpino

LlamaIndex RAG guide tweet

Lance Martin RAG From Scratch tutorial (freeCodeCamp)

Jerry Liu: Firecrawl for LLM apps

Akshay tweet: RAG with Llama-3 locally

Santiago: RAG hallucinations 35%, @eyelevelai release

Listening with LLM (paul.mou.dev)
https://paul.mou.dev/

## Fine-Tuning & Indic LLMs

Ramsri Goutham: Training Indic LLMs — DORA vs LORA

Harman Singh: IndicGenBench (multilingual benchmark, 29 Indic languages)

IndicGenBench paper
arxiv 2404.16816
https://arxiv.org/abs/2404.16816

GitHub: google-research-datasets/indic-gen-bench
https://github.com/google-research-datasets/indic-gen-bench

Tamil-Llama (GitHub abhinand5/tamil-llama, based on Llama 2)
https://github.com/abhinand5/tamil-llama

Tamil-Llama paper
arxiv 2311.05845
https://arxiv.org/abs/2311.05845

Kannada LLAMA (Tensoic)
https://tensoic.com/

Hamel Husain (@HamelHusain): Apple talk is the best ad for fine tuning. They are also using adapters (hot swapping IIUC)
https://x.com/HamelHusain/status/1800546715277357263

Deep Learning Foundations LLMs Part II — fine-tuning, LORA, quantization, QLORA, prefix tuning, RAG

## Novel Architectures

KAN — Kolmogorov-Arnold Networks paper
arxiv 2404.19756
https://arxiv.org/abs/2404.19756

Carlos Perez: KAN networks (Kolmogorov-Arnold Networks)

API Demos for Kolmogorov Arnold Networks
https://kindxiaoming.github.io/pykan/

Novel Architecture Makes Neural Networks More Understandable | Quanta Magazine
By tapping into a decades-old mathematical principle, researchers are hoping that Kolmogorov-Arnold networks will facilitate scientific discovery.
www.quantamagazine.org
https://www.quantamagazine.org/novel-architecture-makes-neural-networks-more-understandable-20240911/

Understanding the Difference Between Kolmogorov-Arnold Networks (KAN) and Multi-Layer Perceptrons
medium.com
https://medium.com/@kingstonkishanthan/understanding-the-difference-between-kolmogorov-arnold-networks-kan-and-multi-layer-perceptrons-ad3c2238097c

ThunderKittens — Flash Attention, 100 lines, 30% faster

Tim Clicks (@timClicks): If this is accurate, then NVIDIA's grip on the tech industry has just vanished. Matrix matrix multiplication (MatMul) can be avoided.
https://x.com/timClicks/status/1799926065642852725

Carlos Perez: Multi-Token Prediction

ScrapeGraphAI (Elvis/omarsar0 tweet)

Vincent Abbott (@vtabbott_): Neural Circuit Diagrams (NCDs) + using them to optimize deep learning algorithms
https://x.com/vtabbott_/status/1830812531293856239

## LLM Evaluation & Benchmarks

Jim Fan: 3 types of LLM evaluations (tweet)

Gergely Orosz: SWE-agent (Princeton, 4x better than LLMs)

Dwarkesh Patel: ARC-AGI — Buck and Ryan beat SOTA in 6 days, 85% human accuracy on held-out set
https://x.com/dwarkesh_sp/status/1802771055016378554

Machine Learning Street Talk: ARC challenge winners — Jack Cole, Mohamed Osman, Michael Hodel
https://x.com/MLStreetTalk/status/1803189533980144113

Foyle: Logging Implicit Human Feedback
https://foyle.io/

Musings on Building a Generative AI Product (LinkedIn)

## AI Tools & Infrastructure

Groq's Lightning Fast AI Chip (techopedia)

Daniel San: Groq + VSCode + Llama3

Vector DB Comparison (superlinked.com)
https://superlinked.com/

Ilya 30u30 reading list (arc.net)

Cursor — The AI Code Editor
https://www.cursor.com/

Jaynit Makwana (@JaynitMakwana): These 4 guys completely revolutionized coding. Anyone can code using Cursor.
https://x.com/JaynitMakwana/status/1829390237107200046

## AI for Science

AI Discovers New Antibiotics (DeepLearning.AI batch issue 231)

Artificial Intelligence to Solve Production Scheduling Problems in Real Industrial Settings
Systematic Literature Review — particle swarm optimization, neural networks, reinforcement learning
www.mdpi.com
https://www.mdpi.com/2079-9292/12/23/4732

Optimization Methods in NN (Kaggle notebook)
https://www.kaggle.com/code/nadaahassan/optimization-methods-in-nn

Google Personal Health LLM (PH-LLM) — Shrey Jain (@shreyjaineth):
Google just released A Personal Health Large Language Model (PH-LLM), a version of Gemini fine-tuned for personal health and wellness.
https://x.com/shreyjaineth/status/1800586918117453911

## ML Theory & Education

Machine Learning Course - Lecture 1 - Microsoft Research
www.microsoft.com
https://www.microsoft.com/en-us/research/video/machine-learning-course-lecture-1/

Understanding Machine Learning — From Theory to Algorithms (449-page PDF eBook)
Kirk Borne tweet
https://x.com/KirkDBorne/status/1831074777487827058

Santiago 7 baby steps for ML

Practical Machine Learning With Rust — San Mateo County Libraries
https://smcl.bibliocommons.com/v2/record/S76C3263013

## Hallucination, Alignment, Verification

Vishal Misra (@vishalmisra): The current LLM architecture cannot recursively self improve because it has no way of knowing if anything is correct or not. They generate things probabilistically and that is that.
https://x.com/vishalmisra/status/1801982071713276275

What's next for AI agentic workflows ft. Andrew Ng of AI Fund (Sequoia Capital AI Ascent)
https://youtu.be/sal78ACtGTc

## NLP

Large Linguistic Models paper — analyzing theoretical linguistic abilities of LLMs
arxiv 2305.00948
https://arxiv.org/abs/2305.00948

Do We Need Language to Think?
A group of neuroscientists argue that our words are primarily for communicating, not for reasoning.
www.nytimes.com
https://www.nytimes.com/2024/06/19/science/brain-language-thought.html

Indian Languages and Text Normalization Part 1 (kavyamanohar.com)
https://kavyamanohar.com/

VictorTaelin repositories (GitHub)
https://github.com/VictorTaelin

## Topos Institute

Topos Institute: Understanding UMAP
https://topos.site/

## Misc AI Notes

"The hardest things in computer science is Caching and .."

NotebookLM's summary of notes (Sep 17, 2024):
I. Health and Fitness — Uncommon Mobility in Your 40s
II. Technology and Science — KAN networks (Quanta), OSSU (GitHub), X rearchitecting (@cambridgemike)
III. Anthropology — Neanderthal extinction, modern humans interbreeding site (ScienceAlert)
IV. Biology and Consciousness — "Third State" of existence (Earth.com)
V. Miscellaneous — UCSF Parnassus Campus (Google Maps)

---

## From self-1.md (Oct 2024 – Feb 2026)

**Understanding Transformer Reasoning on Graph Algorithms**
Research on how transformers solve graph algorithm tasks internally; Oct 2024.
arxiv.org — https://arxiv.org/

**nvidia/Llama-3.1-Nemotron-70B**
NVIDIA's instruction-tuned 70B model release; Oct 2024.
huggingface.co — https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct

**TapeAgent AI framework**
Framework for structured, tape-based agentic AI workflows.
github.com — https://github.com/

**Santiago: RAG pipelines tweet**
Multi-step RAG pipeline explanation with evaluation strategies.
x.com — https://x.com/svpino/

**DeepSeek-R1 PDF**
Full technical report for DeepSeek-R1 reasoning model; Jan 2025.
arxiv.org — https://arxiv.org/

**Scale test-time compute (HuggingFace)**
HuggingFace blog on scaling inference-time computation for better reasoning.
huggingface.co — https://huggingface.co/blog/scaling-test-time-compute

**Jeff Dean NeurIPS 2024 talk**
Jeff Dean's talk at NeurIPS 2024 on the future of AI and ML.
youtube.com — https://www.youtube.com/

**DeepSeek-v3 101**
Overview article on DeepSeek-v3 architecture and training; Jan 2025.
huggingface.co — https://huggingface.co/

**7B Model RLHF reasoning**
Training a 7B parameter model with RLHF for improved reasoning; Jan 2025.
arxiv.org — https://arxiv.org/

**Hugging Face Journal Club: DeepSeek R1**
Deep dive paper reading on DeepSeek R1 methodology.
huggingface.co — https://huggingface.co/

**GRPO explained (tweet)**
Group Relative Policy Optimization — the RL algorithm behind DeepSeek R1's reasoning training.
x.com — https://x.com/

**RAT — Retrieval Augmented Thinking**
New prompting technique combining retrieval with chain-of-thought reasoning.
arxiv.org — https://arxiv.org/

**Open Thoughts reasoning dataset**
Open-source dataset for training reasoning models; Jan 2025.
github.com — https://github.com/

**One Hot Encoding in ML**
Explanation of one-hot encoding for categorical features.
towardsdatascience.com — https://towardsdatascience.com/

**Beyond Black Box LLMs**
Article on interpretability and understanding what LLMs actually do internally.
quanta.org — https://www.quantamagazine.org/

**SUP — State Update Prompts**
Prompting technique for tracking state across long agentic interactions.
arxiv.org — https://arxiv.org/

**AI Engineering book (Chip Huyen)**
Book on building production AI engineering systems.
oreilly.com — https://www.oreilly.com/

**Create apps without code using DeepSeek + RooCode**
Tutorial on using agentic coding tools with local models; Jan 2025.
youtube.com — https://www.youtube.com/

**GitHub: Roo-Code**
Open-source agentic coding assistant.
github.com — https://github.com/RooVetGit/Roo-Code

**Local DeepSeek R1 hardware setup**
Guide to hardware requirements for running DeepSeek R1 locally; Jan 2025.
reddit.com — https://www.reddit.com/r/LocalLLaMA/

**MIT researchers train reliable AI agents**
MIT research on making AI agents more reliably complete multi-step tasks; Nov 2025.
mit.edu — https://news.mit.edu/

**LLM Post-Training DeepSeek tweet**
Thread on post-training techniques used in DeepSeek models.
x.com — https://x.com/

**OpenAI Operator vs Browser Use**
Comparison of OpenAI's Operator product and the Browser Use open-source agent.
reddit.com — https://www.reddit.com/r/LocalLLaMA/

**Thoughts on a Month with Devin (AI coding agent)**
Honest review of Devin's capabilities and limitations after extended use; Jan 2025.
answer.ai — https://www.answer.ai/

**LLM agent book shelved (tweet)**
Author tweets on shelving an LLM agent book due to rapid field changes.
x.com — https://x.com/

**Chatbot fundamental limitations (Quanta)**
Quanta Magazine on the core architectural limitations preventing chatbots from true reasoning.
quantamagazine.org — https://www.quantamagazine.org/

**AI decodes animal calls**
Research on using ML to decode communication signals in animals; Dec 2024.
quantamagazine.org — https://www.quantamagazine.org/

**Demystifying DeepSeek**
Accessible explanation of what makes DeepSeek models architecturally different.
huggingface.co — https://huggingface.co/

**Google AI Toolbox introduction**
Google's new toolbox for building production AI applications; Feb 2025.
ai.google.dev — https://ai.google.dev/

**State of LLM Reasoning Models**
Survey of reasoning model techniques in early 2025.
arxiv.org — https://arxiv.org/

**Building ML Systems: trillion FLOPS talk**
Talk on infrastructure considerations for training trillion-parameter models.
youtube.com — https://www.youtube.com/

**Where Does Meaning Live — Category Theory and LLMs**
Connecting categorical semantics to how language models encode meaning; Apr 2025.
arxiv.org — https://arxiv.org/

**To Make Language Models Work Better (prompting)**
Research on prompting techniques for improved model performance.
arxiv.org — https://arxiv.org/

**Virtual Machinations: LLMs as computers**
Essay on understanding LLMs through the lens of virtual machine architectures.
rachelbythebay.com — https://rachelbythebay.com/

**Understanding Attention in LLMs**
Deep technical explainer on how attention mechanisms work in transformers.
arxiv.org — https://arxiv.org/

**Generalized Transformers from Applicative Functors**
Research connecting transformer architectures to applicative functor composition; Feb 2025.
arxiv.org — https://arxiv.org/

**Indic-Parler TTS**
Text-to-speech model for Indian languages; Dec 2024.
huggingface.co — https://huggingface.co/ai4bharat/

**Pralekha Indic document alignment**
Tool for aligning Indic language documents for parallel corpus creation; Dec 2024.
github.com — https://github.com/

**Ollama deepseek-r1 local deployment**
Running DeepSeek-R1 with Ollama; Jan 2025.
ollama.ai — https://ollama.ai/library/deepseek-r1

**LLM Reasoning State (State of LLMs Mar 2025)**
Overview of where reasoning models stood in Mar 2025.
arxiv.org — https://arxiv.org/

**NotebookLM app**
Google's NotebookLM for podcast-style AI summaries; May 2025.
notebooklm.google.com — https://notebooklm.google.com/

**After Three Years: Modular CUDA**
Retrospective on Modular's work making GPU computing accessible; May 2025.
modular.com — https://www.modular.com/

**Modular DeepSeek democratizing compute**
Modular's effort to make DeepSeek models run efficiently on diverse hardware.
modular.com — https://www.modular.com/

**AI is helping decode animals' speech (Nature)**
Nature article on ML models for animal communication decoding; Sep 2025.
nature.com — https://www.nature.com/articles/d41586-025-02917-9

**AI scientist Song-Chun Zhu leaves US for China**
Guardian profile on why a leading AI researcher returned to China; Sep 2025.
theguardian.com — https://www.theguardian.com/news/ng-interactive/2025/sep/16/song-chun-zhu-why-one-of-the-worlds-most-brilliant-ai-scientists-left-the-us-for-china

**AI experts return from China stunned: US grid too weak**
Fortune article on China's AI data center infrastructure advantage; Aug 2025.
fortune.com — https://fortune.com/2025/08/14/data-centers-china-grid-us-infrastructure/

**GPT-5.2 derives new result in theoretical physics**
OpenAI preprint showing GPT-5.2 proposing a new formula for gluon amplitude, later formally verified.
openai.com — https://openai.com/index/new-result-theoretical-physics/

**LLM-Generated Lean 4 Proofs (Dylan Miller)**
Research paper comparing GPT-5, Gemini on formal Lean 4 theorem proving.
github.com — https://github.com/lampless/LLM-Generated-Lean4-Proofs/blob/main/Dylan%20Miller_%20LLM-Generated%20Lean4%20Proofs.pdf

**Model Context Protocol intro**
Anthropic's MCP standard for connecting AI models to data sources and tools; Feb 2025.
anthropic.com — https://www.anthropic.com/

**OpenClaw 21 use cases (Matthew Berman)**
Thread on 21 practical use cases for OpenClaw (Claude Code agentic workflow tool).
x.com — https://x.com/MatthewBerman/status/2023843493765157235

**How to run a 24/7 AI company for $50/month (OpenClaw)**
Guide to running continuous AI agent workflows on a Mac Mini.
x.com — https://x.com/ziwenxu_/status/2023610499024171077

**OpenClaw memory fix guide**
Tips for preventing AI agents from forgetting context across long sessions.
x.com — https://x.com/KSimback/status/2024431606002319739

**Greg Isenberg: 24/7 digital employees with OpenClaw**
Thread on building cash-flowing automation businesses with AI agents.
x.com — https://x.com/gregisenberg/status/2024247983999521123

**Anthropic free short course: Build skills with Claude Code**
Free Anthropic course on building skills/workflows deployable across Claude Code, API, SDK, VS Code.
x.com — https://x.com/sentientt_media/status/2025142906051498085

**Fine-Tuning LLMs: 114-page comprehensive guide**
Paper exploring fine-tuning from foundational to advanced strategies including multimodal applications.
x.com — https://x.com/techwith_ram/status/2025255030585237931

**DOSA Code Discovery: one gene links heart, obesity, sleep apnea**
Bengaluru BRIC-inStem scientists discover KCNA2 gene mutation linking three disorders; Feb 2026.
deccanherald.com — https://www.deccanherald.com/india/karnataka/bengaluru/the-dosa-code-one-gene-three-disorders-3899925

**signal creator Moxie Marlinspike launches Confer AI**
End-to-end encrypted AI assistant; Jan 2026.
arstechnica.com — https://arstechnica.com/security/2026/01/signal-creator-moxie-marlinspike-wants-to-do-for-ai-what-he-did-for-messaging/

**Recommended AI books list (John Crickett)**
21 AI/ML book recommendations covering the full stack from theory to production.
x.com — https://x.com/johncrickett/status/2026288507312910547

**aidnn by Isotopes AI**
Multi-agentic AI platform for data analysis and decisions; Oct 2025.
isotopes.ai — https://isotopes.ai/#about-us

**User personal note: AI project ideas (Feb 2026)**
Projects: procrastination agent, Eke subtitle generation, extended Wiktionary from DNS Bhat methodology, self-history clustering into indexed book, research paper translation to ellara kannada, team-of-rivals approach for vocabulary, newsfeed auto-summarization in Kannada.
