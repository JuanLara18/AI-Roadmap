# Emerging Frontiers

> The cutting edge — where AI is heading next. These areas are rapidly evolving and full of research opportunities.

**Prerequisites:** Varies by topic. [Deep Learning](../03-deep-learning/README.md) is a good foundation for all of them.

---

## Core Topics

### Multimodal AI

Models that understand and generate across multiple modalities — text, images, audio, video.

| Model / Approach | Modalities | Description |
|---|---|---|
| **GPT-4o / o1** | Text, image, audio, computer use | Frontier multimodal reasoning and vision-based tool use |
| **Claude 3.5 Sonnet** | Text, image, code, computer use | State-of-the-art visual coding, reasoning, and agentic desktop control |
| **Gemini 1.5 Pro / 2.0 Flash** | Text, image, audio, video | Google's native multimodal models supporting up to 2M tokens context |
| **Llama 3.2 Vision** | Text, image | Open-source multimodal family with native image understanding |
| **LLaVA / LLaVA-Next** | Text, image | Highly popular open-source vision-language models |
| **CLIP** | Text, image | Contrastive vision-language pretraining bridging vision and text |
| **ImageBind (Meta)** | 6 modalities | Binding images, text, audio, depth, thermal, IMU |
| Any-to-Any Models | All | Models that take any input and produce any output |

### Reinforcement Learning

Agents that learn by interacting with environments.

| Concept | Description |
|---|---|
| Markov Decision Processes | The mathematical framework for RL |
| Policy Gradients (REINFORCE) | Learning policies directly |
| PPO (Proximal Policy Optimization) | Stable policy optimization, used in RLHF |
| DQN / Rainbow | Value-based methods for discrete actions |
| Model-Based RL | Learning environment models to plan ahead |
| Multi-Agent RL | Multiple agents learning simultaneously |
| Offline RL | Learning from fixed datasets without interaction |

| Application | Example |
|---|---|
| Game Playing | AlphaGo, OpenAI Five, AlphaStar |
| Robotics | Sim-to-real transfer, manipulation |
| LLM Alignment | RLHF, GRPO for preference tuning |
| Autonomous Driving | Decision-making in complex environments |

### Robotics & Embodied AI

AI systems that interact with the physical world.

| Area | Description |
|---|---|
| Simulation | MuJoCo, Isaac Sim, PyBullet for training before real-world deployment |
| Sim-to-Real Transfer | Bridging the gap between simulation and reality |
| Foundation Models for Robotics | RT-2, Octo, MolmoWeb — applying LLM-style models to robotics and web |
| Manipulation | Grasping, assembly, dexterous hands |
| Navigation | Autonomous movement in complex environments |
| Human-Robot Interaction | Natural language commands, collaborative work |

### AI for Science

AI accelerating scientific discovery.

| Domain | Breakthrough |
|---|---|
| Protein Folding | **AlphaFold 2/3** — predicting 3D protein structures |
| Drug Discovery | Molecular generation, virtual screening, ADMET prediction |
| Materials Science | Predicting material properties, discovering new materials |
| Climate & Weather | **GenCast**, Pangu-Weather — AI weather forecasting |
| Mathematics | AI-assisted theorem proving, conjecture generation |
| Genomics | Variant effect prediction, gene expression modeling |

### World Models & Simulation

AI systems that build internal models of how the world works.

| Concept | Description |
|---|---|
| World Models | Learning predictive models of environments |
| Video Prediction | Predicting future frames from past observations |
| State Space Models (Mamba) | Linear-time alternatives to transformers, hybrid architectures (Nemotron) |
| Neural Radiance Fields (NeRFs) | 3D scene reconstruction from images |
| Gaussian Splatting | Real-time 3D scene rendering |
| Digital Twins | Virtual replicas of physical systems |
| Autonomous Driving Simulation | CARLA, Waymo Open Dataset |

### Edge AI & On-Device Inference

Running AI on constrained devices — phones, IoT, embedded systems.

| Technique | Purpose |
|---|---|
| Model Quantization (INT8, INT4) | Reducing model precision for speed and size |
| Knowledge Distillation | Training small models from large teachers |
| Pruning | Removing unnecessary model parameters |
| TinyML | ML on microcontrollers |
| ONNX Runtime | Cross-platform model inference |
| TensorRT | NVIDIA GPU-optimized inference |
| Core ML / TFLite | Mobile deployment (Apple / Android) |

### Other Emerging Areas

| Area | Description |
|---|---|
| Quantum Machine Learning | Quantum computing for ML speedups |
| Neuromorphic Computing | Brain-inspired computing hardware |
| Continual / Lifelong Learning | Models that learn incrementally without forgetting |
| Causal Inference | Understanding cause and effect, not just correlation |
| Synthetic Data Generation | Creating training data artificially |
| Computer Use Agents | Models controlling desktop/browser interfaces autonomously (e.g. Claude 3.5 Sonnet, Browser Use) |
| AI Governance & Policy | Shaping the future of AI regulation |

---

## Recommended Resources

### Courses
- [DeepMind x UCL — Reinforcement Learning](https://www.youtube.com/playlist?list=PLqYmG7hTraZDVH599EItlEWsUOsJbAodm) (free)
- [Stanford CS330 — Deep Multi-Task and Meta Learning](https://cs330.stanford.edu/) (free)
- [MIT 6.S094 — Deep Learning for Self-Driving Cars](https://selfdrivingcars.mit.edu/) (free)
- [Hugging Face — Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course) (free)

### Books
- *Reinforcement Learning: An Introduction* — Sutton & Barto ([free online](http://incompleteideas.net/book/the-book-2nd.html))
- *Probabilistic Robotics* — Thrun, Burgard, Fox
- *The Coming Wave* — Mustafa Suleyman

### Key Papers
- [AlphaFold 2](https://www.nature.com/articles/s41586-021-03819-2) — Jumper et al.
- [World Models](https://arxiv.org/abs/1803.10122) — Ha & Schmidhuber
- [NeRF](https://arxiv.org/abs/2003.08934) — Neural Radiance Fields
- [3D Gaussian Splatting](https://arxiv.org/abs/2308.14737) — Kerbl et al.
- [RT-2: Vision-Language-Action Models](https://arxiv.org/abs/2307.15818)

---

## Project Ideas

| Project | Difficulty | Description |
|---|---|---|
| **RL Game Agent** | Intermediate | Train an agent to play Atari games or CartPole with PPO |
| **Scientific Paper Analyzer** | Intermediate | Use LLMs to extract insights from research papers |
| **Edge-Deployed Classifier** | Intermediate | Quantize and deploy an image classifier on a Raspberry Pi or phone |
| **3D Scene Reconstruction** | Advanced | Build a NeRF or Gaussian Splatting pipeline from photos |
| **Molecular Property Predictor** | Advanced | ML model for predicting chemical properties |
| **Sim-to-Real Robot Control** | Expert | Train a robot controller in simulation and deploy to hardware |

---

## Keep Exploring

The frontier moves fast. Stay current by following:
- [arXiv cs.AI](https://arxiv.org/list/cs.AI/recent) and [cs.LG](https://arxiv.org/list/cs.LG/recent)
- [Papers With Code](https://paperswithcode.com/)
- [Hugging Face Daily Papers](https://huggingface.co/papers)
- [The Batch (DeepLearning.AI)](https://www.deeplearning.ai/the-batch/)
- [AI Twitter/X](https://x.com/) — follow researchers and practitioners

[Back to Roadmap](../../README.md)
