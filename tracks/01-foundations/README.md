# Foundations

> Mathematics, Python, data literacy, and the building blocks for everything that follows.

**Prerequisites:** None — this is where you start.

---

## Core Concepts

### Linear Algebra

The language of machine learning. Nearly every ML algorithm is expressed as matrix operations under the hood.

| Concept | Why It Matters |
|---|---|
| Vectors & Matrices | Data representation, transformations |
| Matrix Multiplication | Neural network forward pass, embeddings |
| Eigenvalues & Eigenvectors | PCA, dimensionality reduction, spectral methods |
| Singular Value Decomposition (SVD) | Recommendations, compression, latent features |
| Norms & Distance Metrics | Loss functions, similarity measures |

### Calculus & Optimization

How models learn — every training loop is an optimization problem.

| Concept | Why It Matters |
|---|---|
| Derivatives & Gradients | Backpropagation, parameter updates |
| Chain Rule | Computing gradients through deep networks |
| Gradient Descent | SGD, Adam, learning rate scheduling |
| Convexity | Understanding loss landscapes |
| Automatic Differentiation | How PyTorch/TensorFlow compute gradients |

### Probability & Statistics

The foundation for understanding uncertainty, inference, and evaluation.

| Concept | Why It Matters |
|---|---|
| Probability Distributions | Modeling data, generative models |
| Bayes' Theorem | Bayesian inference, Naive Bayes |
| Maximum Likelihood Estimation | Training probabilistic models |
| Hypothesis Testing | A/B testing, model comparison |
| Confidence Intervals & p-values | Evaluating statistical significance |

### Python for Data Science

The primary language of ML — and its essential ecosystem.

| Tool | Purpose |
|---|---|
| **NumPy** | Numerical computing, array operations |
| **Pandas** | Data manipulation and analysis |
| **Matplotlib / Seaborn** | Data visualization |
| **Jupyter Notebooks** | Interactive development and experimentation |
| **Scikit-learn** | Classical ML algorithms and utilities |

### Software Engineering Foundations

Writing clean, maintainable, and reproducible code is just as important as the math. To build real-world AI, you need software engineering best practices.

| Skill / Tool | Why It Matters |
|---|---|
| **Git & Version Control** | Tracking model/code changes, collaboration, open-source contribution |
| **Virtual Environments (`uv`)** | Dependency management and reproducible environments (extremely fast) |
| **Clean Code & OOP** | Structuring modular pipelines, writing reusable datasets/models, SOLID principles |
| **Testing (`pytest`)** | Writing unit tests for data transforms, model outputs, and training steps |
| **APIs (`FastAPI`)** | Wrapping models into microservices, handling JSON inputs/outputs |

### Data Wrangling & EDA

Real-world data is messy. Cleaning and understanding your data is where every project starts.

| Skill | What You'll Do |
|---|---|
| Data Cleaning | Handle missing values, outliers, duplicates |
| Feature Engineering | Create new features, encode categoricals, scale numerics |
| Exploratory Data Analysis | Distributions, correlations, patterns |
| Data Pipelines | Reproducible data transformations |
| Visualization Best Practices | Telling stories with data |

---

## Recommended Resources

### Courses
- [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (free)
- [Khan Academy — Statistics and Probability](https://www.khanacademy.org/math/statistics-probability) (free)
- [fast.ai — Practical Deep Learning](https://course.fast.ai/) (free) — starts from foundations
- [Stanford CS229 — Machine Learning](https://cs229.stanford.edu/) (free)
- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) (free)
- [MIT CS — The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) (free) — essential shell, git, and tooling guides

### Books
- *An Introduction to Statistical Learning (ISLR)* — James, Witten, Hastie, Tibshirani
- *Mathematics for Machine Learning* — Deisenroth, Faisal, Ong ([free PDF](https://mml-book.github.io/))
- *Clean Code in Python* — Mariano Anaya
- *Think Stats* — Allen Downey ([free](https://greenteapress.com/thinkstats2/))

### Tools to Install
- [Python 3.11+](https://www.python.org/)
- [Git](https://git-scm.com/) for version control
- [uv](https://github.com/astral-sh/uv) — the lightning-fast Python package and environment manager
- [Ruff](https://github.com/astral-sh/ruff) — extremely fast Python linter and formatter
- [Jupyter Lab](https://jupyter.org/)

---

## Project Ideas

| Project | Difficulty | Description |
|---|---|---|
| **Exploratory Data Analysis Portfolio** | Beginner | Analyze 3-5 public datasets (Kaggle, UCI) and create a visual storytelling portfolio |
| **Statistical Hypothesis Testing Suite** | Beginner | Implement common statistical tests from scratch and compare with SciPy |
| **Tested Data Pipeline Package** | Intermediate | Build a reusable data cleaning and feature engineering pipeline as a fully tested Python package using `pytest` and `uv` |
| **Model API Service** | Intermediate | Build a microservice with FastAPI that takes JSON input, runs simple validation, processes it, and returns predictions |
| **Interactive Dashboard** | Intermediate | Create a Streamlit or Plotly Dash app for exploring a dataset interactively |

---

## What's Next?

Once you're comfortable with these foundations, move on to **[Classical Machine Learning](../02-classical-ml/README.md)** to start building models.

[Back to Roadmap](../../README.md)
