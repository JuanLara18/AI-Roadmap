# Deep Learning

> Neural networks from scratch to state-of-the-art architectures — the engine behind modern AI.

**Prerequisites:** [Foundations](../01-foundations/README.md) (linear algebra, calculus), [Classical ML](../02-classical-ml/README.md) (model evaluation basics).

---

## Core Concepts

### Neural Network Fundamentals

The building blocks of deep learning.

| Concept | Why It Matters |
|---|---|
| Perceptron & Multi-Layer Perceptrons | The simplest neural network — understand forward pass |
| Activation Functions (ReLU, GELU, Sigmoid, Tanh) | Non-linearity that makes deep learning work |
| Backpropagation | How networks learn — computing gradients through layers |
| Loss Functions (Cross-Entropy, MSE, Contrastive) | Defining what "good" means for your model |
| Optimizers (SGD, Adam, AdamW, LAMB) | How gradients become parameter updates |
| Regularization (Dropout, Weight Decay, BatchNorm) | Preventing overfitting |

### Convolutional Neural Networks (CNNs)

The architecture that revolutionized computer vision.

| Architecture | Contribution |
|---|---|
| LeNet / AlexNet | Pioneered deep learning for images |
| VGG | Showed depth matters |
| ResNet | Skip connections, training very deep networks |
| EfficientNet | Compound scaling for efficiency |
| ConvNeXt | Modernizing CNNs with transformer insights |

### Recurrent Networks & Sequences

Processing sequential data — text, time series, audio.

| Architecture | Use Case |
|---|---|
| RNNs | Basic sequence processing |
| LSTMs | Long-range dependencies, time series |
| GRUs | Simplified LSTMs, faster training |
| Seq2Seq + Attention | Machine translation, summarization |
| Temporal Convolutional Networks | Alternative to RNNs for sequences |
| **Mamba / State Space Models** | Linear-time sequence modeling alternative to attention |

### The Transformer Architecture

The architecture that changed everything — the foundation for LLMs, vision transformers, and more.

| Component | Purpose |
|---|---|
| Self-Attention | Relating all positions in a sequence |
| Multi-Head Attention | Learning multiple attention patterns |
| Positional Encoding | Injecting sequence order information |
| Layer Normalization | Stabilizing training |
| Encoder-Decoder Structure | Flexible architecture for many tasks |

> [!IMPORTANT]
> Understanding transformers deeply is essential for nearly everything in modern AI — LLMs, vision models, multimodal systems, and agents all build on this architecture.

### Training at Scale

Techniques for training large models efficiently.

| Technique | Purpose |
|---|---|
| Mixed Precision Training (FP16/BF16) | Faster training, less memory |
| Gradient Accumulation | Effective larger batch sizes |
| Distributed Data Parallel (DDP) | Multi-GPU training |
| FSDP / DeepSpeed ZeRO | Memory-efficient distributed training |
| Mixture of Experts (MoE) | Sparse activation for efficient scaling (used in Mixtral, Qwen 2.5, DeepSeek-V3) |
| Learning Rate Scheduling (Cosine, Warmup) | Better convergence |
| Gradient Checkpointing | Trading compute for memory |

---

## Recommended Resources

### Courses
- [fast.ai — Practical Deep Learning](https://course.fast.ai/) (free)
- [Stanford CS231n — CNNs for Visual Recognition](http://cs231n.stanford.edu/) (free)
- [Stanford CS224n — NLP with Deep Learning](http://web.stanford.edu/class/cs224n/) (free)
- [MIT 6.S191 — Introduction to Deep Learning](http://introtodeeplearning.com/) (free)
- [deeplearning.ai — Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) (Coursera)

### Books
- *Deep Learning* — Goodfellow, Bengio, Courville ([free online](https://www.deeplearningbook.org/))
- *Dive into Deep Learning* — Zhang et al. ([free interactive](https://d2l.ai/))
- *Understanding Deep Learning* — Simon Prince ([free PDF](https://udlbook.github.io/udlbook/))

### Key Papers
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al., 2017
- [Deep Residual Learning](https://arxiv.org/abs/1512.03385) — He et al., 2015
- [Adam Optimizer](https://arxiv.org/abs/1412.6980) — Kingma & Ba, 2014
- [Batch Normalization](https://arxiv.org/abs/1502.03167) — Ioffe & Szegedy, 2015

### Frameworks
- [PyTorch](https://pytorch.org/) — the absolute industry and research standard framework
- [JAX](https://github.com/google/jax) — high-performance numerical computing for large-scale training and research
- [Keras 3](https://keras.io/) — multi-backend API (supports PyTorch, JAX, and TensorFlow)
- [Lightning](https://lightning.ai/) — structured PyTorch training for scaling up easily
- *Note on TensorFlow:* Pure [TensorFlow](https://www.tensorflow.org/) is increasingly considered legacy for new projects, though still active in maintenance.

---

## Project Ideas

| Project | Difficulty | Description |
|---|---|---|
| **Build a Neural Network from Scratch** | Intermediate | Implement forward/backward pass with only NumPy |
| **Image Classifier with Transfer Learning** | Intermediate | Fine-tune a pretrained ResNet on a custom dataset |
| **Stock Price Forecaster** | Advanced | LSTM-based time series prediction |
| **Transformer from Scratch** | Advanced | Implement the full attention mechanism in PyTorch |
| **Distributed Training Setup** | Advanced | Train a model across multiple GPUs with DDP |

---

## What's Next?

From here, specialize in **[NLP & LLMs](../04-nlp-and-llms/README.md)**, **[Computer Vision](../05-computer-vision/README.md)**, or **[Generative AI](../06-generative-ai/README.md)** — they all build on the deep learning concepts covered here.

[Back to Roadmap](../../README.md)
