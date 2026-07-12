# NLP & Large Language Models

> From text processing to building and deploying LLM-powered applications — the hottest area in AI.

**Prerequisites:** [Deep Learning](../03-deep-learning/README.md) — especially the transformer architecture section.

---

## Core Concepts

### Text Fundamentals

How machines process and represent human language.

| Concept | Description |
|---|---|
| Tokenization | Splitting text into tokens (BPE, WordPiece, SentencePiece, Tiktoken) |
| Word Embeddings | Word2Vec, GloVe — dense vector representations |
| Contextual Embeddings | BERT-style embeddings that change based on context |
| TF-IDF | Classic term frequency method for text representation |
| Text Preprocessing | Normalization, stopwords, stemming, lemmatization |

### Transformer-Based Models

The zoo of models built on the transformer architecture.

| Model Family | Type | Best For |
|---|---|---|
| **BERT** (and RoBERTa, DeBERTa) | Encoder | Classification, NER, semantic similarity |
| **GPT** (GPT-4o, o1, o3-mini) | Decoder | General text, complex reasoning, instruction following |
| **T5 / FLAN-T5** | Encoder-Decoder | Summarization, translation, general NLU |
| **Llama 3.1 / 3.3 & Qwen 2.5** | Decoder | Open-source text generation, local deployment, tool use |
| **Claude** (3.5 Sonnet, 3 Opus) | Decoder | Long context, agentic coding, reasoning, computer use |
| **Gemini** (1.5 Pro, 2.0 Flash) | Decoder | Native multimodal, long context (up to 2M tokens), reasoning |
| **DeepSeek** (V3, R1) | Decoder (MoE) | Cost-efficient general reasoning, deep math/logic reasoning |

### LLM Fine-Tuning

Adapting foundation models to your specific task.

| Method | Description | When to Use |
|---|---|---|
| **Full Fine-Tuning** | Update all parameters | When you have lots of data and compute |
| **LoRA / QLoRA** | Low-rank adapters, quantized training | Most practical fine-tuning scenario |
| **SFT (Supervised Fine-Tuning)** | Train on instruction-response pairs | Making models follow instructions |
| **RLHF** | Reinforcement learning from human feedback | Aligning model outputs with preferences |
| **DPO** | Direct preference optimization | Simpler alternative to RLHF |
| **GRPO** | Group relative policy optimization | Efficient preference alignment |

### Retrieval-Augmented Generation (RAG)

Grounding LLM outputs in external knowledge.

| Component | Purpose |
|---|---|
| Document Chunking | Breaking documents into retrievable pieces |
| Embeddings | Converting text to vectors for similarity search |
| Vector Databases | Storing and querying embeddings (Pinecone, Weaviate, ChromaDB, Qdrant, FAISS) |
| Retrieval Strategies | Dense retrieval, hybrid search, reranking |
| Generation with Context | Prompting LLMs with retrieved documents |
| Evaluation | Faithfulness, relevance, answer correctness (RAGAS) |

> [!TIP]
> RAG is often the best starting point for LLM applications — it's cheaper than fine-tuning and keeps your data up-to-date without retraining.

### Prompt Engineering & Context Engineering

Getting the most out of LLMs without training.

| Technique | Description |
|---|---|
| System Prompts | Setting model behavior and constraints |
| Few-Shot Learning | Providing examples in the prompt |
| Chain-of-Thought (CoT) | Prompting step-by-step reasoning |
| ReAct | Combining reasoning and actions |
| Structured Output | JSON mode, function calling, grammar-constrained decoding |
| Context Window Management | Long-context strategies, summarization, compression |

### LLM Deployment & Serving

Getting models into production.

| Tool | Purpose |
|---|---|
| **vLLM** | High-throughput serving with PagedAttention |
| **TGI (Text Generation Inference)** | Hugging Face's production inference server |
| **Ollama** | Run LLMs locally with one command |
| **llama.cpp** | CPU-friendly inference with GGUF quantization |
| **SGLang** | Fast structured generation and serving |
| Quantization (GPTQ, AWQ, GGUF, FP8) | Making models smaller and faster |

---

## Recommended Resources

### Courses
- [Stanford CS224n — NLP with Deep Learning](http://web.stanford.edu/class/cs224n/) (free)
- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) (free)
- [DeepLearning.AI — ChatGPT Prompt Engineering](https://www.deeplearning.ai/short-courses/) (free)
- [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) (free)

### Books
- *Speech and Language Processing* — Jurafsky & Martin ([free draft](https://web.stanford.edu/~jurafsky/slp3/))
- *Natural Language Processing with Transformers* — Tunstall, von Werra, Wolf
- *Build a Large Language Model (from Scratch)* — Sebastian Raschka

### Key Papers
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — The Transformer
- [BERT](https://arxiv.org/abs/1810.04805) — Bidirectional encoder representations
- [GPT-3: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — foundation for in-context learning
- [LoRA](https://arxiv.org/abs/2106.09685) — Low-Rank Adaptation
- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) — Original RAG paper
- [DPO](https://arxiv.org/abs/2305.18290) — Direct Preference Optimization

### Key Tools
- [Hugging Face Transformers](https://huggingface.co/docs/transformers) — model hub and library
- [LangChain](https://www.langchain.com/) — LLM application framework
- [LlamaIndex](https://www.llamaindex.ai/) — data framework for LLM apps
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) — unified and user-friendly LLM fine-tuning framework
- [Unsloth](https://github.com/unslothai/unsloth) — fast local LLM fine-tuning
- [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) — configuration-driven fine-tuning toolkit
- [FeynRL](https://github.com/boson-ai/FeynRL) — modular post-training and RL alignment framework

---

## Project Ideas

| Project | Difficulty | Description |
|---|---|---|
| **Sentiment Analysis System** | Beginner | Classify text sentiment using pretrained transformers |
| **RAG Chatbot** | Intermediate | Build a chatbot that answers questions from your documents |
| **Multilingual NLP Pipeline** | Intermediate | Process and analyze text in multiple languages |
| **LLM Fine-Tuning** | Advanced | Fine-tune an open-source LLM with LoRA on custom data |
| **Semantic Search Engine** | Intermediate | Build a vector search system with embeddings |
| **LLM-Powered Code Reviewer** | Advanced | Build a tool that reviews pull requests using an LLM |

---

## What's Next?

Explore **[AI Agents](../07-ai-agents/README.md)** to build autonomous LLM-powered systems, or **[Generative AI](../06-generative-ai/README.md)** for creative applications.

[Back to Roadmap](../../README.md)
