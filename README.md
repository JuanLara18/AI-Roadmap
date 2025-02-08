
# 🚀 AI Roadmap  

![GitHub repo size](https://img.shields.io/github/repo-size/JuanLara18/AI-Roadmap?color=blue&style=flat-square)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-orange?style=flat-square)

A structured, project-based roadmap for learning **Machine Learning & AI** through hands-on projects. Each project builds on the previous one, helping you move from beginner to advanced AI concepts.  



## 📌 **What’s Inside?**  

✔ **22 Machine Learning & AI projects** 🚀  
✔ Hands-on learning with **Jupyter Notebooks** 📒  
✔ Covers **Data Science, NLP, Computer Vision, and MLOps** 🔥  



## 🏆 **Project Roadmap**  

| **#** | **Project Name**                         | **Difficulty** | **Objective**                                           | **Key Technologies**                                                                                 | **Expected Outcome**                                           |
|-------|-------------------------------------------|----------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| **1** | **Exploratory Data Analysis Portfolio**   | 🟢 Beginner     | Learn to analyze and visualize datasets.                | Pandas, Matplotlib, Seaborn                                                                  | Master data exploration and visualization.                     |
| **2** | **Iris Flower Classification**            | 🟢 Beginner     | Train ML models to classify flower species.             | Scikit-learn, Decision Trees, Random Forests                                                 | Understand classification models and feature importance.       |
| **3** | **Titanic Survival Prediction**           | 🟢 Beginner     | Predict survival based on passenger data.               | Scikit-learn, Logistic Regression, Data Preprocessing, Feature Engineering                    | Learn to handle missing data and categorical variables.        |
| **4** | **Build Your Own Linear Regression**      | 🟡 Intermediate | Implement linear regression from scratch.               | NumPy, Gradient Descent                                                                      | Gain a deep understanding of linear regression mechanics.      |
| **5** | **Housing Price Predictor**               | 🟡 Intermediate | Predict house prices using regression models.           | Scikit-learn, Feature Engineering                                                            | Apply regression in real-world scenarios.                      |
| **6** | **Sentiment Analysis System**             | 🟡 Intermediate | Analyze sentiment in real-world text data.              | Natural Language Processing (NLP), Transformers, Text Processing                             | Learn text vectorization and model fine-tuning.                |
| **7** | **Customer Churn Predictor**              | 🟡 Intermediate | Identify customers likely to leave a service.           | Scikit-learn, Random Forests, Data Balancing                                                 | Apply predictive modeling in business scenarios.               |
| **8** | **Stock Price Predictor**                 | 🔵 Advanced     | Forecast stock prices using time-series data.           | Scikit-learn, Long Short-Term Memory Networks (LSTMs), Time Series Analysis                   | Explore financial ML modeling challenges.                      |
| **9** | **Build Your Own Neural Network**         | 🔵 Advanced     | Create a neural network from scratch.                   | NumPy, Backpropagation, Matrix Algebra                                                       | Understand deep learning at a mathematical level.              |
| **10**| **Image Classification System**           | 🔵 Advanced     | Train a Convolutional Neural Network (CNN) to classify images. | TensorFlow, Keras, Convolutional Neural Networks (CNNs)                                       | Learn the fundamentals of deep learning.                       |
| **11**| **Real-Time Face Recognition System**     | 🔵 Advanced     | Detect and recognize faces in real time.                | OpenCV, Deep Learning                                                                        | Apply AI in real-world security applications.                  |
| **12**| **Recommendation System**                 | 🟡 Intermediate | Build a system that recommends content/products.        | Scikit-learn, Collaborative Filtering, Data Mining                                           | Understand the logic behind recommendation engines.            |
| **13**| **Automated ML Pipeline**                 | 🔵 Advanced     | Automate the ML workflow from data preprocessing to model selection. | AutoML, MLOps, Cloud Computing                                                               | Learn how to scale AI models efficiently.                      |
| **14**| **Language Model from Scratch**           | 🔵 Advanced     | Build a basic Transformer-based language model.         | Natural Language Processing (NLP), Transformers, PyTorch                                     | Understand the foundations of large language models.           |
| **15**| **A/B Testing Framework**                 | 🟡 Intermediate | Evaluate ML models using statistical testing.           | Experiment Design, Hypothesis Testing                                                        | Learn proper validation techniques for ML models.              |
| **16**| **Image Generation System (GANs)**        | 🔵 Advanced     | Generate images using deep learning.                    | TensorFlow, Keras, Generative Adversarial Networks (GANs)                                    | Explore AI-based content generation.                           |
| **17**| **Multilanguage NLP Pipeline**            | 🔵 Advanced     | Process and analyze multilingual text.                  | Natural Language Processing (NLP), Machine Translation                                       | Apply AI to multilingual language processing.                  |
| **18**| **Reinforcement Learning Game**           | 🔵 Advanced     | Train an AI agent to play video games.                  | Reinforcement Learning, Policy Gradients                                                     | Learn how agents interact and improve through experience.      |
| **19**| **Real-Time Fraud Detection System**      | 🔵 Advanced     | Detect fraudulent transactions using AI.                | Scikit-learn, Fraud Detection, Anomaly Detection                                             | Apply AI for financial security and risk management.           |
| **20**| **Build Your Own AutoML**                 | 🔵 Advanced     | Create a system that automates ML model training and selection. | AutoML, Feature Engineering                                                                  | Learn how to design AutoML systems.                            |
| **21**| **MLOps Pipeline**                        | 🔵 Advanced     | Implement a scalable MLOps infrastructure.              | MLOps, DevOps, Cloud Platforms                                                               | Learn how to deploy and maintain ML models in production.      |
| **22**| **Distributed ML System**                 | 🔴 Expert       | Train ML models at scale using multiple machines.       | Distributed Computing, Big Data, Apache Spark                                                | Master high-performance AI workloads.                          |




## 📂 **Repository Structure**  

This repository follows a structured format to keep projects organized and scalable.

```
AI-Roadmap/
│── projects/                     # Contains all machine learning projects
│   ├── 01-exploratory-data-analysis/  
│   │   ├── README.md              # Project overview and instructions
│   │   ├── notebook.ipynb         # Main Jupyter Notebook
│   │   ├── images/                # Stores visualizations, plots, model outputs
│   │   ├── src/                   # Contains modular Python scripts
│   │   │   ├── preprocessing.py   # Functions for data cleaning & preprocessing
│   │   │   ├── model.py           # Machine learning model implementation
│   │   │   ├── utils.py           # Helper functions for various tasks
│   │   ├── results/               # Stores outputs like CSVs, predictions, logs
│   ├── 02-iris-flower-classification/
│   ├── ... (all 22 projects)
│── datasets/                      # Shared datasets for all projects
│── docs/                          # Guides, documentation, additional resources
│── scripts/                       # Utility scripts for setup or automation
│── CONTRIBUTING.md                 # Guidelines for contributing to the repo
│── LICENSE                        # Open-source license (MIT)
│── README.md                      # Main repository documentation
│── pyproject.toml                  # Dependency and environment management
│── .gitignore                      # Specifies which files should be ignored by Git
```


## 📦 **Managing Dependencies**  

This repository uses **pyproject.toml** to allow installing only the dependencies needed for a specific project.  

### ✅ **Installing Dependencies for a Specific Project**  
Instead of installing all libraries, you can install only what you need.  

Example: If you want to work on the **Iris Flower Classification** project, run:  
```bash
pip install -e .[iris-classification]
```

Example: If you want to work on the **Stock Price Predictor** project, run:  
```bash
pip install -e .[stock-prediction]
```

### ✅ **Installing Everything**  
If you prefer to install all dependencies at once:  
```bash
pip install -e .[eda, iris-classification, titanic, linear-regression, housing, sentiment-analysis, churn-prediction, stock-prediction, neural-network, image-classification, face-recognition, recommendation, automl, language-model, ab-testing, image-generation, multilanguage-nlp, reinforcement-learning, fraud-detection, mlops, distributed-ml]
```

---

Now you can work on **any project independently** without unnecessary dependencies! 🚀


## 🤝 **Contributing**  

Contributions are **welcome**! 🎉  
- Suggest improvements 🚀  
- Add new projects 🔥  

Read the [CONTRIBUTING.md](CONTRIBUTING.md) for details.



## 📜 **License**  

This project is licensed under the **MIT License**.

---



⭐ **If you find this useful, consider starring the repo!** 😊✨