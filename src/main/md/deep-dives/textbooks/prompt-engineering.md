<a id="ch1"></a>
# Prompt Engineering

> Lee Boonstra · Google whitepaper, v7 (2025) · [the PDF in Drive](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

A practitioner’s whitepaper written around Gemini on Vertex AI, with each technique shown as a filled-in prompt table (goal, model, temperature, top-K/top-P, prompt, output). Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Prompting is treated as an engineering loop: pick a model, set the sampling configuration, choose a technique, and record every attempt. The paper first explains the output controls (length, temperature, top-K, top-P) and how they interact, including the repetition loops that extreme settings cause. It then walks through the standard techniques, from zero- and few-shot through system, contextual and role prompts, step-back prompting, chain of thought, self-consistency, tree of thoughts, ReAct, automatic prompt engineering and prompts for writing, explaining, translating and debugging code. The last part is a list of habits: give examples, keep it simple, say what you want rather than what you don’t, use variables, structured output and schemas, and document attempts in a standard template.

**Contents**

1. [Introduction and output configuration](ch1): What a prompt is, why the paper uses the API rather than the chat app, and the sampling settings that shape every output.
2. [Prompting techniques](ch2): The main prompting techniques, each with a worked prompt and its configuration.
3. [Best Practices](ch3): Practical habits for writing, testing and maintaining prompts.
4. [Summary](ch4): A recap, the prompt-documentation template, and references.


---

## Introduction and output configuration

*PDF pp. 6–12*

What a prompt is, why the paper uses the API rather than the chat app, and the sampling settings that shape every output.

**Introduction**  
Anyone can write a prompt, but getting reliable output depends on wording, examples, structure and model settings together.  
→ PDF p. 6 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Prompt engineering**  
Prompt engineering is iterative design of the input so the model predicts the output you want; it works best with direct access to model settings.  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Output length**  
Limiting output tokens only cuts generation off; it doesn’t make the model concise, so the prompt must ask for brevity too.  
→ PDF p. 8 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Sampling controls**  
Temperature, top-K and top-P each restrict which tokens can be sampled, and they combine; the paper gives starting values and warns that very low or very high settings cause repetition loops.  
→ PDF pp. 9–12 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)


---

<a id="ch2"></a>
## Prompting techniques

*PDF pp. 13–53*

The main prompting techniques, each with a worked prompt and its configuration.

**General prompting / zero shot**  
A plain instruction with no examples; works for simple tasks and is the baseline.  
→ PDF pp. 13–14 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**One-shot & few-shot**  
One or a few examples show the format and the pattern; the examples should be varied and high quality.  
→ PDF pp. 15–17 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**System, contextual and role prompting**  
System prompts set the task and output format, contextual prompts give background, role prompts give a voice; JSON output is recommended for structure.  
→ PDF pp. 18–24 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Step-back prompting**  
First ask a broader question, then feed its answer into the specific task, to bring relevant background into play.  
→ PDF pp. 25–28 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Chain of Thought (CoT)**  
Asking for step-by-step reasoning improves answers on reasoning tasks, especially combined with few-shot examples; it costs more tokens.  
→ PDF pp. 29–31 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Self-consistency**  
Sample several reasoning paths at higher temperature and take the majority answer.  
→ PDF pp. 32–35 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Tree of Thoughts (ToT)**  
Explore a tree of intermediate thoughts rather than a single chain, for problems that need search.  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**ReAct (reason & act)**  
Interleave reasoning with tool calls (for example, search), observing results before the next step.  
→ PDF pp. 37–39 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Automatic Prompt Engineering**  
Use a model to generate candidate prompts, score them, and keep the best.  
→ PDF pp. 40–41 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Code prompting**  
Prompts for writing, explaining, translating and debugging code, with the caution that generated code must be read and tested.  
→ PDF pp. 42–53 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)


---

<a id="ch3"></a>
## Best Practices

*PDF pp. 54–65*

Practical habits for writing, testing and maintaining prompts.

**Provide examples**  
Examples are the most effective single tool.  
→ PDF p. 54 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Design with simplicity**  
Short, clear prompts with action verbs work better than complex ones.  
→ PDF p. 55 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Be specific about the output**  
State the desired output precisely.  
→ PDF p. 56 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Use Instructions over Constraints**  
Positive instructions tend to work better than lists of prohibitions.  
→ PDF pp. 56–57 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Control the max token length**  
Cap output length in the configuration or ask for it in the prompt.  
→ PDF p. 58 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Use variables in prompts**  
Variables make prompts reusable across inputs.  
→ PDF p. 58 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Experiment with input formats and writing styles**  
Wording, style and prompt type all change results, so try variants.  
→ PDF p. 59 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**For few-shot prompting with classification tasks, mix up the classes**  
In few-shot classification, shuffle the order of classes so the model doesn’t learn the order.  
→ PDF p. 59 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Adapt to model updates**  
Retest prompts when the model changes.  
→ PDF p. 60 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Experiment with output formats**  
Structured formats like JSON reduce hallucination and make output parseable.  
→ PDF p. 60 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**JSON Repair**  
JSON is verbose and can be cut off; repair libraries fix truncated output.  
→ PDF p. 61 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Working with Schemas**  
JSON Schemas can structure the input too, focusing the model on the relevant fields.  
→ PDF p. 62 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Experiment together with other prompt engineers**  
Compare prompts written by several people.  
→ PDF p. 63 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**CoT Best practices**  
For chain of thought: put the answer after the reasoning, extract it separately, and use temperature 0.  
→ PDF p. 64 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

**Document the various prompt attempts**  
Log every attempt (goal, model, settings, prompt, output) in a standard table so results can be compared.  
→ PDF pp. 64–65 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)


---

<a id="ch4"></a>
## Summary

*PDF pp. 66–68*

A recap, the prompt-documentation template, and references.

→ PDF pp. 66–68 in [the PDF](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)

