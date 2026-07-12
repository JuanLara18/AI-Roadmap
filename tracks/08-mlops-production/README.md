# MLOps & Production AI

> Taking models from notebooks to reliable, scalable production systems — where the real engineering happens.

**Prerequisites:** Any ML track (you need a model to deploy). Basic familiarity with Docker and cloud platforms is helpful.

---

## Core Concepts

### Experiment Tracking

Keeping track of what you tried, what worked, and why.

| Tool | Description |
|---|---|
| **MLflow** | Open-source platform for the full ML lifecycle |
| **Weights & Biases (W&B)** | Experiment tracking, visualization, model registry |
| **Trackio** | Lightweight Hugging Face-integrated tracking |
| **Neptune** | Metadata management for ML teams |
| **DVC (Data Version Control)** | Versioning data and models alongside code |

### Model Serving & Deployment

Getting predictions to users in real time.

| Tool / Framework | Best For |
|---|---|
| **vLLM / SGLang** | High-throughput, low-latency LLM serving with structured generation |
| **Triton Inference Server** | High-performance, multi-framework GPU/CPU serving (NVIDIA) |
| **FastAPI** | Building custom REST APIs for classical ML and lightweight models |
| **BentoML** | Packaging, containerizing, and deploying general ML services |
| **Ollama** | Quick local LLM and embedding model deployment |
| **Hugging Face Inference Endpoints** | Fully managed serverless model hosting |
| **TorchServe / TF Serving** | PyTorch-native and TensorFlow-native serving (increasingly specialized/legacy) |

### Containerization & Orchestration

Packaging models for consistent deployment.

| Technology | Purpose |
|---|---|
| **Docker** | Containerize your model and dependencies |
| **Kubernetes** | Orchestrate containers at scale |
| **KServe** | Kubernetes-native model serving |
| **Helm Charts** | Packaging Kubernetes deployments |
| **Docker Compose** | Multi-container local development |

### CI/CD for ML

Automating the ML pipeline from data to deployment.

| Concept | Description |
|---|---|
| Automated Testing | Unit tests for data, models, and pipelines |
| Pipeline Orchestration | Airflow, Prefect, Dagster, Kubeflow Pipelines |
| Automated Retraining | Trigger retraining on data drift or schedule |
| Model Registry | Version and stage models (staging, production) |
| GitHub Actions for ML | CI/CD workflows for ML projects |
| Feature/Training/Serving Skew | Ensuring consistency across environments |

### Monitoring & Observability

Knowing when things go wrong in production.

| Concern | Tools & Techniques |
|---|---|
| Data Drift Detection | Evidently, Great Expectations, Alibi Detect |
| Model Performance Monitoring | Tracking accuracy, latency, throughput over time |
| Logging & Alerting | Prometheus, Grafana, custom dashboards |
| A/B Testing | Comparing model versions in production |
| Shadow Deployment | Running new models alongside old ones without serving |

### Feature Stores

Managing features consistently across training and serving.

| Tool | Description |
|---|---|
| **Feast** | Open-source feature store |
| **Tecton** | Managed feature platform |
| **Hopsworks** | End-to-end ML platform with feature store |

### Cloud ML Platforms

The major cloud providers offer fully managed ML platforms that bundle many of the above concepts into integrated services.

| Platform | Key Service | Strengths |
|---|---|---|
| **AWS** | SageMaker, Bedrock | Largest ecosystem, mature tooling, broadest model access |
| **Google Cloud** | Vertex AI, Gemini API | Strong AutoML, BigQuery integration, TPU access |
| **Microsoft Azure** | Azure ML, Azure OpenAI | Enterprise integration, Microsoft ecosystem, OpenAI partnership |

Each platform handles training, deployment, pipelines, and monitoring differently. For a deep comparison, platform-specific workflows, and lighter alternatives (managed APIs, local deployment), see the dedicated **[End-to-End AI Platforms](../11-end-to-end-platforms/README.md)** track.

### LLMOps

MLOps specific to LLM-powered applications.

| Concern | Solution |
|---|---|
| Prompt Management | Version and test prompts, prompt registries |
| LLM Caching | Cache repeated queries to reduce cost (GPTCache, Redis) |
| Cost Optimization | Model routing, token budgets, smaller models for simple tasks |
| Guardrails | Input/output filtering, content moderation (NeMo Guardrails, Guardrails AI) |
| Evaluation | LLM-as-judge, human evaluation, automated benchmarks |
| Observability | LangSmith, Langfuse, Braintrust, Phoenix for tracing LLM calls |
| Agent Infrastructure | Durable execution, crash recovery, approval gates (Kitaru, Temporal) |

### AI System Architecture & Design Patterns

Building robust, enterprise-ready AI systems requires moving beyond simple API endpoints to resilient system architectures.

| Pattern / Concept | Description | Key Tools / Standards |
|---|---|---|
| **LLM Gateway / Proxy** | Centralized router that sits between applications and LLMs. Handles fallback models, load balancing, rate limiting, and token budgets. | LiteLLM, Portkey, Kong, Custom proxies |
| **Enterprise API Gateways** | Exposing model APIs securely to clients, managing authentication, logging, payload size checks, and enterprise security. | Apigee, Kong, AWS API Gateway |
| **Asynchronous & Event-Driven Loops** | Offloading long-running agent loops or prompt tasks using message brokers and background queues to avoid blocking HTTP timeouts. | Celery, RabbitMQ, Redis, Kafka, Temporal |
| **Semantic Caching** | Caching LLM responses based on semantic similarity of prompts rather than exact string matching, dramatically cutting costs and latency. | Redis, GPTCache, Qdrant, Milvus |
| **LLM Firewalls & Guardrails** | Intercepting incoming prompt injections, protecting against PII leaks, and validating outgoing schema compliance in real time. | Llama Guard, NeMo Guardrails, Guardrails AI |
| **Agent Gateways (MCP)** | Standardizing tool integration so autonomous agents can securely discover and call enterprise data and APIs. | Model Context Protocol (MCP) |

---

## Recommended Resources

### Courses
- [Made With ML — MLOps Course](https://madewithml.com/) (free)
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/) (free)
- [Google MLOps on Vertex AI](https://cloud.google.com/vertex-ai/docs/start/introduction-mlops) (free)
- [DeepLearning.AI — Machine Learning Engineering for Production (MLOps)](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops)
- [ByteByteGo — System Design Fundamentals](https://bytebytego.com/) (great for understanding API gateways, rate limiting, and queues)

### Books
- *Designing Machine Learning Systems* — Chip Huyen
- *Machine Learning Engineering* — Andriy Burkov ([free online](http://www.mlebook.com/))
- *Reliable Machine Learning* — Cathy Chen et al.
- *Enterprise Integration Patterns* — Gregor Hohpe (essential for asynchronous and queue architectures)
- *Building LLM Apps* — Valentina Alto

### Key Papers
- [Hidden Technical Debt in ML Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — Sculley et al.
- [Monitoring ML Models in Production](https://arxiv.org/abs/2007.06299)

---

## Project Ideas

| Project | Difficulty | Description |
|---|---|---|
| **Model API with FastAPI + Docker** | Beginner | Wrap a trained model in an API and containerize it |
| **End-to-End ML Pipeline** | Intermediate | Data ingestion, training, evaluation, deployment with MLflow |
| **Automated Retraining System** | Advanced | Detect data drift and trigger retraining automatically |
| **Enterprise LLM Gateway** | Advanced | Build a production-grade LLM proxy with routing, fallback failover, semantic caching (Redis), rate-limiting, and cost tracking |
| **Asynchronous Agent Queue** | Advanced | Build a background task queue (Celery + RabbitMQ) to process long-running agent tasks and send progress updates via WebSockets |
| **A/B Testing Framework** | Intermediate | Compare model versions in a simulated production setting |
| **ML Monitoring Dashboard** | Intermediate | Grafana dashboard tracking model performance metrics |

---

## What's Next?

Ready to ship? See **[End-to-End AI Platforms](../11-end-to-end-platforms/README.md)** for cloud, managed, and local deployment workflows. Then consider the responsibility that comes with deploying AI in **[AI Safety & Ethics](../09-ai-safety-ethics/README.md)**.

[Back to Roadmap](../../README.md)
