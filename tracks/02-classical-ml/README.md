# Classical Machine Learning

> Supervised and unsupervised learning — the algorithms that started it all and still power most production systems.

**Prerequisites:** [Foundations](../01-foundations/README.md) — linear algebra, statistics, Python basics.

---

## Core Concepts

### Supervised Learning

Learning from labeled data to make predictions.

| Algorithm | Type | Best For |
|---|---|---|
| Linear Regression | Regression | Continuous predictions, baseline models |
| Logistic Regression | Classification | Binary classification, interpretable models |
| Decision Trees | Both | Interpretable models, feature importance |
| Random Forests | Both | Robust predictions, handling noisy data |
| Gradient Boosting (XGBoost, LightGBM, CatBoost) | Both | Competition-winning tabular data models |
| Support Vector Machines | Both | High-dimensional data, small datasets |
| K-Nearest Neighbors | Both | Simple baselines, non-parametric modeling |
| Naive Bayes | Classification | Text classification, spam filtering |

### Unsupervised Learning

Discovering structure in unlabeled data.

| Algorithm | Purpose |
|---|---|
| K-Means | Cluster data into groups |
| DBSCAN | Density-based clustering, handling noise |
| Hierarchical Clustering | Tree-structured groupings |
| PCA | Dimensionality reduction, visualization |
| t-SNE / UMAP | High-dimensional data visualization |
| Isolation Forest | Anomaly detection |

### Model Evaluation & Selection

How to know if your model is actually good.

| Concept | What It Tells You |
|---|---|
| Train/Validation/Test Split | Unbiased performance estimation |
| Cross-Validation | Robust evaluation with limited data |
| Bias-Variance Tradeoff | Why models underfit or overfit |
| ROC/AUC, Precision, Recall, F1 | Classification performance metrics |
| RMSE, MAE, R-squared | Regression performance metrics |
| Confusion Matrix | Detailed classification error analysis |

### Feature Engineering

Often the difference between a mediocre model and a great one.

| Technique | When to Use |
|---|---|
| One-Hot Encoding | Categorical variables |
| Target Encoding | High-cardinality categoricals |
| Feature Scaling (StandardScaler, MinMax) | Distance-based algorithms |
| Polynomial Features | Capturing non-linear relationships |
| Feature Selection (mutual information, RFE) | Reducing dimensionality |
| Handling Imbalanced Data (SMOTE, class weights) | Rare event prediction |

### AutoML

Automating the model selection and tuning process.

| Tool | Description |
|---|---|
| **AutoGluon** | AWS's state-of-the-art AutoML platform for tabular, image, and text data |
| **Optuna** | The industry-standard hyperparameter optimization framework |
| **H2O AutoML** | Enterprise-grade AutoML platform |
| **FLAML** | Fast, lightweight AutoML by Microsoft |

---

## Recommended Resources

### Courses
- [Stanford CS229 — Machine Learning](https://cs229.stanford.edu/) (free)
- [Andrew Ng — Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) (Coursera)
- [fast.ai — Machine Learning Course](https://course.fast.ai/) (free)
- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) (free)

### Books
- *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* — Aurelien Geron
- *An Introduction to Statistical Learning (ISLR)* — James et al. ([free PDF](https://www.statlearning.com/))
- *The Elements of Statistical Learning* — Hastie, Tibshirani, Friedman ([free PDF](https://hastie.su.domains/ElemStatLearn/))
- *Pattern Recognition and Machine Learning* — Christopher Bishop

### Key Libraries
- [Scikit-learn](https://scikit-learn.org/) — the Swiss army knife of classical ML
- [AutoGluon](https://autogluon.dev/) — AWS's state-of-the-art AutoML platform
- [XGBoost](https://xgboost.readthedocs.io/) / [LightGBM](https://lightgbm.readthedocs.io/) / [CatBoost](https://catboost.ai/)
- [Optuna](https://optuna.org/) — hyperparameter optimization
- [imbalanced-learn](https://imbalanced-learn.org/) — handling class imbalance
- [SHAP](https://shap.readthedocs.io/) — model interpretability

---

## Project Ideas

| Project | Difficulty | Description |
|---|---|---|
| **Iris Flower Classification** | Beginner | Train and compare classifiers on the classic Iris dataset |
| **Titanic Survival Prediction** | Beginner | Feature engineering and classification on the Kaggle Titanic dataset |
| **Housing Price Estimator** | Intermediate | Regression with feature engineering on real estate data |
| **Customer Churn Predictor** | Intermediate | Predict churn using ensemble methods and class balancing |
| **Recommendation Engine** | Intermediate | Collaborative filtering and content-based recommendations |
| **Fraud Detection System** | Advanced | Anomaly detection on highly imbalanced transaction data |
| **Build Your Own Linear Regression** | Intermediate | Implement gradient descent from scratch with NumPy |

---

## What's Next?

Ready to go deeper? Move on to **[Deep Learning](../03-deep-learning/README.md)** to learn neural networks, or jump to a specialized track like **[NLP & LLMs](../04-nlp-and-llms/README.md)** or **[Computer Vision](../05-computer-vision/README.md)**.

[Back to Roadmap](../../README.md)
