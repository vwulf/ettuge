<a id="ch1"></a>
# Multimodal Deep Learning

> Akkus, Chu, Dani, Ebert et al. (LMU Munich seminar booklet) · arXiv 2301.04856, January 2023 · [the PDF in Drive](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view)

A student-written seminar booklet, each section by different authors; its state of the art is early 2023. Each chapter and section also links to the free online (bookdown) edition. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A survey of deep learning that combines text and images, written by students in an LMU Munich seminar. It first reviews the state of the art separately in NLP (word embeddings to transformers and large language models) and computer vision (CNNs to vision transformers and self-supervised learning), with the datasets and benchmarks for each. The main part covers multimodal architectures in both directions: image captioning, text-to-image generation (DALL-E, diffusion models), images grounding language models, text supervising vision models (CLIP), and joint models of both modalities. Further chapters extend to audio and video, mixing structured data with text and images, multipurpose models like Gato and Perceiver, and generative art.

**Contents**

1. [1 Introduction](ch1): What multimodal deep learning is and how the booklet is organized.
2. [2 Introducing the modalities](ch2): The unimodal foundations: NLP and computer vision, and the benchmarks for each.
3. [3 Multimodal architectures](ch3): Architectures that link text and images in either direction or jointly.
4. [4 Further Topics](ch4): More modalities, tabular data, generalist models and generative art.
5. [5 Conclusion](ch5): Closing remarks.
6. [6 Epilogue](ch6): Developments after writing: new architectures and video generation.


---

## 1 Introduction

*PDF pp. 9–12* · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/introduction.html)

What multimodal deep learning is and how the booklet is organized.

**1.1 Introduction to Multimodal Deep Learning**  
Why combine modalities.  
*Terms:* multimodal deep learning  
→ PDF p. 9 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/introduction.html#introduction-to-multimodal-deep-learning)

**1.2 Outline of the Booklet**  
Booklet outline.  
*Terms:* outline  
→ PDF pp. 10–12 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/introduction.html#outline-of-the-booklet)


---

<a id="ch2"></a>
## 2 Introducing the modalities

*PDF pp. 13–88* · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c01-00-intro-modalities.html)

The unimodal foundations: NLP and computer vision, and the benchmarks for each.

**2.1 State-of-the-art in NLP**  
Word embeddings, transformers, BERT, GPT and scaling.  
*Terms:* word2vec, transformer, BERT, GPT, language models  
→ PDF pp. 15–38 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c01-00-intro-modalities.html#c01-01-sota-nlp)

**2.2 State-of-the-art in Computer Vision**  
CNNs, ResNets, vision transformers and self-supervised vision.  
*Terms:* CNN, ResNet, ViT, self-supervised learning  
→ PDF pp. 39–59 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c01-00-intro-modalities.html#c01-02-sota-cv)

**2.3 Resources and Benchmarks for NLP, CV and multimodal tasks**  
Datasets and benchmarks for NLP, vision and multimodal tasks.  
*Terms:* benchmarks, ImageNet, GLUE, COCO, datasets  
→ PDF pp. 60–88 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c01-00-intro-modalities.html#c01-03-benchmarks)


---

<a id="ch3"></a>
## 3 Multimodal architectures

*PDF pp. 89–186* · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c02-00-multimodal.html)

Architectures that link text and images in either direction or jointly.

**3.1 Image2Text**  
Image captioning with encoder–decoder and transformer models.  
*Terms:* image captioning, Image2Text  
→ PDF pp. 92–105 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c02-00-multimodal.html#c02-01-img2text)

**3.2 Text2Image**  
Text-to-image generation: GANs, DALL-E, diffusion and Imagen.  
*Terms:* text-to-image, DALL-E, diffusion, Imagen, Stable Diffusion  
→ PDF pp. 106–130 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c02-00-multimodal.html#c02-02-text2img)

**3.3 Images supporting Language Models**  
Visual grounding for language models.  
*Terms:* visual grounding, vision-language  
→ PDF pp. 131–151 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c02-00-multimodal.html#c02-03-img-support-text)

**3.4 Text supporting Vision Models**  
Vision models trained with text supervision, such as CLIP.  
*Terms:* CLIP, contrastive learning, zero-shot  
→ PDF pp. 152–164 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c02-00-multimodal.html#c02-04-text-support-img)

**3.5 Models for both modalities**  
Joint models of both modalities such as Flamingo and data2vec.  
*Terms:* Flamingo, data2vec, VilBERT, unified models  
→ PDF pp. 165–186 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c02-00-multimodal.html#c02-05-text-plus-img)


---

<a id="ch4"></a>
## 4 Further Topics

*PDF pp. 187–240* · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c03-00-further.html)

More modalities, tabular data, generalist models and generative art.

**4.1 Including Further Modalities**  
Adding audio, video and other modalities.  
*Terms:* audio, video, further modalities  
→ PDF pp. 187–202 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c03-00-further.html#c03-01-further-modalities)

**4.2 Structured + Unstructured Data**  
Combining structured (tabular) data with unstructured text and images.  
*Terms:* tabular data, structured data  
→ PDF pp. 203–214 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c03-00-further.html#c03-02-structured-unstructured)

**4.3 Multipurpose Models**  
Generalist models such as Gato, Perceiver and Pathways.  
*Terms:* Gato, Perceiver, Pathways, generalist models  
→ PDF pp. 215–231 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c03-00-further.html#c03-03-multi-purpose)

**4.4 Generative Art**  
Generative art with text-to-image models.  
*Terms:* generative art, prompting  
→ PDF pp. 232–240 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/c03-00-further.html#c03-04-usecase)


---

<a id="ch5"></a>
## 5 Conclusion

*PDF pp. 241–242* · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/conclusion-1.html)

Closing remarks.

*Terms:* conclusion

→ PDF pp. 241–242 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/conclusion-1.html)


---

<a id="ch6"></a>
## 6 Epilogue

*PDF pp. 243–272* · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/epilogue.html)

Developments after writing: new architectures and video generation.

**6.1 New influential architectures**  
Influential architectures published after the booklet.  
*Terms:* new architectures  
→ PDF p. 243 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/epilogue.html#new-influential-architectures)

**6.2 Creating videos**  
Text-to-video generation.  
*Terms:* video generation  
→ PDF pp. 244–272 in [the PDF](https://drive.google.com/file/d/16K_kCgK9HfJtcI0spXRZnLON3yk_fub9/view) · [read online](https://slds-lmu.github.io/seminar_multimodal_dl/epilogue.html#creating-videos)

