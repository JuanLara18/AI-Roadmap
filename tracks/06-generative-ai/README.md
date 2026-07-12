# Generative AI

> Creating new content — text, images, audio, video, and code. The technology reshaping every creative industry.

**Prerequisites:** [Deep Learning](../03-deep-learning/README.md). For text generation, also see [NLP & LLMs](../04-nlp-and-llms/README.md).

---

## Core Concepts

### Image Generation

From GANs to diffusion models — the evolution of AI-generated images.

| Approach | Description | Key Models |
|---|---|---|
| GANs | Generator vs discriminator adversarial training | StyleGAN, BigGAN |
| VAEs | Variational autoencoders for smooth latent spaces | VQ-VAE, DALL-E (v1) |
| Diffusion Models | Iterative denoising from random noise | Stable Diffusion 3.5, DALL-E 3, Midjourney |
| Flow Matching | Optimal transport-based generation | Flux, Stable Diffusion 3.5 |
| Consistency Models | Few-step generation from diffusion | LCM, SDXL Turbo |

| Component | What It Does |
|---|---|
| DiT (Diffusion Transformer) / U-Net | The backbone network that predicts noise (DiT used in Flux, SD3+) |
| Text Encoder (CLIP, T5) | Converts text prompts to conditioning vectors |
| VAE | Encodes/decodes between pixel and latent space |
| Scheduler (DDPM, Euler, DPM++) | Controls the denoising process |
| ControlNet / IP-Adapter | Fine-grained control over generation |

### Text Generation

How LLMs generate text, and the techniques that make it work.

| Concept | Description |
|---|---|
| Autoregressive Generation | Predicting one token at a time |
| Sampling Strategies | Temperature, top-k, top-p (nucleus sampling) |
| Beam Search | Finding high-probability sequences |
| Speculative Decoding | Using small models to speed up large ones |
| Structured Generation | Constraining output to valid JSON, code, etc. |

### Audio & Music Generation

| Area | Key Models/Tools |
|---|---|
| Text-to-Speech | Bark, XTTS, StyleTTS 2, Fish Speech |
| Voice Cloning | Real-time voice conversion, speaker embedding |
| Music Generation | Suno, Udio, MusicGen, Stable Audio |
| Audio Understanding | Whisper (transcription), AudioLM |

### Video Generation

The newest frontier — still rapidly evolving.

| Model / Tool | Description |
|---|---|
| **Sora (OpenAI)** | Hyper-realistic video from text prompts |
| **Veo (Google)** | Cinematic video with rich details and native audio sync |
| **Kling (Kuaishou)** | High-fidelity video generation, multilingual lip-sync, motion control |
| **Runway Gen-3 Alpha** | Production-grade video generation and editing |
| **Luma Dream Machine** | Fast, high-quality, physics-consistent video generation |
| **AnimateDiff** | Open-source framework for adding motion to image generation |
| **Temporal consistency** | The core challenge — keeping videos coherent across frames |

### Code Generation

AI as a programming partner.

| Tool | Description |
|---|---|
| **GitHub Copilot** | Inline code completion and generation |
| **Cursor** | AI-native code editor |
| **Aider** | Terminal-based AI pair programming and multi-file editing |
| **Code LLMs (Qwen2.5-Coder, DeepSeek-Coder-V2)** | State-of-the-art open-source code models |
| **Benchmarks (HumanEval, SWE-bench)** | Standardized datasets for evaluating code generation and autonomous software engineering |

---

## Recommended Resources

### Courses
- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) (free)
- [DeepLearning.AI — Generative AI Short Courses](https://www.deeplearning.ai/short-courses/) (free)
- [Stanford CS236 — Deep Generative Models](https://deepgenerativemodels.github.io/) (free)

### Books
- *Generative Deep Learning* — David Foster (O'Reilly)
- *Understanding Deep Learning* — Simon Prince ([free PDF](https://udlbook.github.io/udlbook/))

### Key Papers
- [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) — Goodfellow et al., 2014
- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) — Ho et al., 2020
- [High-Resolution Image Synthesis with Latent Diffusion](https://arxiv.org/abs/2112.10752) — Stable Diffusion
- [Photorealistic Text-to-Image Generation (DALL-E 2)](https://arxiv.org/abs/2204.06125)
- [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747)

### Key Tools
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers) — diffusion model library
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) — node-based generation workflow
- [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) — Stable Diffusion web UI
- [Replicate](https://replicate.com/) — run generative models via API

---

## Project Ideas

| Project | Difficulty | Description |
|---|---|---|
| **Image Generation with GANs** | Intermediate | Train a GAN to generate faces or art |
| **Style Transfer App** | Intermediate | Apply artistic styles to photos using neural style transfer |
| **Text-to-Image Prompt Playground** | Beginner | Build a UI for experimenting with Stable Diffusion prompts |
| **AI Music Composer** | Advanced | Generate music with MusicGen or custom models |
| **ControlNet Pipeline** | Advanced | Guided image generation with pose, edge, and depth control |
| **Fine-Tune a Diffusion Model** | Advanced | Train a custom LoRA for Stable Diffusion on your own images |

---

## What's Next?

Combine generative models with autonomous reasoning in **[AI Agents](../07-ai-agents/README.md)**, or learn to deploy them in **[MLOps](../08-mlops-production/README.md)**.

[Back to Roadmap](../../README.md)
