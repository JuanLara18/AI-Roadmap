from dataclasses import dataclass
from enum import Enum
from typing import Optional, List

class SourceType(Enum):
    KAGGLE = "kaggle"
    URL = "url"
    SKLEARN = "sklearn"
    KERAS = "keras"

@dataclass
class DatasetConfig:
    name: str
    source_type: SourceType
    source_id: str
    filename: str
    description: str
    project_number: int

DATASETS = {
    # Project 1: Exploratory Data Analysis
    "netflix": DatasetConfig(
        name="Netflix Shows",
        source_type=SourceType.KAGGLE,
        source_id="shivamb/netflix-shows",
        filename="netflix_titles.csv",
        description="Netflix movies and TV shows catalog",
        project_number=1
    ),
    
    # Project 2: Iris Classification
    "iris": DatasetConfig(
        name="Iris Dataset",
        source_type=SourceType.SKLEARN,
        source_id="load_iris",
        filename="iris.csv",
        description="Classic iris flower dataset",
        project_number=2
    ),
    
    # Project 3: Titanic Survival Prediction
    "titanic": DatasetConfig(
        name="Titanic Dataset",
        source_type=SourceType.KAGGLE,
        source_id="c/titanic",
        filename="titanic.csv",
        description="Titanic survival prediction dataset",
        project_number=3
    ),
    
    # Project 4: Linear Regression
    "boston_housing": DatasetConfig(
        name="Boston Housing",
        source_type=SourceType.SKLEARN,
        source_id="load_boston",
        filename="boston_housing.csv",
        description="Boston housing prices dataset",
        project_number=4
    ),
    
    # Project 5: Housing Price Predictor
    "house_prices": DatasetConfig(
        name="House Prices",
        source_type=SourceType.KAGGLE,
        source_id="c/house-prices-advanced-regression-techniques",
        filename="house_prices.csv",
        description="Advanced house prices regression dataset",
        project_number=5
    ),
    
    # Project 6: Sentiment Analysis
    "imdb_reviews": DatasetConfig(
        name="IMDB Reviews",
        source_type=SourceType.KERAS,
        source_id="imdb",
        filename="imdb_reviews.csv",
        description="IMDB movie reviews for sentiment analysis",
        project_number=6
    ),
    
    # Project 7: Customer Churn
    "telco_churn": DatasetConfig(
        name="Telco Customer Churn",
        source_type=SourceType.KAGGLE,
        source_id="blastchar/telco-customer-churn",
        filename="customer_churn.csv",
        description="Telco customer churn dataset",
        project_number=7
    ),
    
    # Project 8: Stock Price Predictor
    "sp500": DatasetConfig(
        name="S&P 500 Stocks",
        source_type=SourceType.KAGGLE,
        source_id="camnugent/sandp500",
        filename="sp500_stocks.csv",
        description="S&P 500 stock market data",
        project_number=8
    ),
    
    # Project 9: Neural Network
    "mnist": DatasetConfig(
        name="MNIST Dataset",
        source_type=SourceType.KERAS,
        source_id="mnist",
        filename="mnist.npz",
        description="MNIST handwritten digits dataset",
        project_number=9
    ),
    
    # Project 10: Image Classification
    "cifar10": DatasetConfig(
        name="CIFAR-10 Dataset",
        source_type=SourceType.KERAS,
        source_id="cifar10",
        filename="cifar10.npz",
        description="CIFAR-10 image classification dataset",
        project_number=10
    ),
    
    # Project 11: Face Recognition
    "lfw_people": DatasetConfig(
        name="Labeled Faces in the Wild",
        source_type=SourceType.SKLEARN,
        source_id="fetch_lfw_people",
        filename="lfw_people.pkl",
        description="Labeled Faces in the Wild dataset",
        project_number=11
    ),
    
    # Project 12: Recommendation System
    "movielens": DatasetConfig(
        name="MovieLens Dataset",
        source_type=SourceType.KAGGLE,
        source_id="grouplens/movielens-20m-dataset",
        filename="ratings.csv",
        description="MovieLens 20M ratings dataset",
        project_number=12
    ),
    
    # Project 13: Automated ML Pipeline
    "credit_card": DatasetConfig(
        name="Credit Card Fraud",
        source_type=SourceType.KAGGLE,
        source_id="mlg-ulb/creditcardfraud",
        filename="creditcard.csv",
        description="Credit card fraud detection dataset",
        project_number=13
    ),
    
    # Project 14: Language Model
    "wikitext": DatasetConfig(
        name="WikiText-2",
        source_type=SourceType.URL,
        source_id="https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-2-v1.zip",
        filename="wikitext-2.zip",
        description="WikiText-2 language modeling dataset",
        project_number=14
    ),
    
    # Project 15: A/B Testing
    "ab_data": DatasetConfig(
        name="A/B Testing Dataset",
        source_type=SourceType.KAGGLE,
        source_id="zhangluyuan/ab-testing",
        filename="ab_data.csv",
        description="E-commerce A/B testing dataset",
        project_number=15
    ),
    
    # Project 16: Image Generation
    "celeba": DatasetConfig(
        name="CelebA Dataset",
        source_type=SourceType.KAGGLE,
        source_id="jessicali9530/celeba-dataset",
        filename="celeba.zip",
        description="CelebA face generation dataset",
        project_number=16
    ),
    
    # Project 17: Multilanguage NLP
    "ted_talks": DatasetConfig(
        name="TED Talks",
        source_type=SourceType.KAGGLE,
        source_id="rounakbanik/ted-talks",
        filename="ted_talks.csv",
        description="Multilingual TED talks dataset",
        project_number=17
    ),
    
    # Project 18: Reinforcement Learning
    "gym_data": DatasetConfig(
        name="OpenAI Gym",
        source_type=SourceType.URL,
        source_id="none",  # Will be handled by gym library
        filename="gym_data",
        description="OpenAI Gym environments",
        project_number=18
    ),
    
    # Project 19: Fraud Detection
    "ieee_fraud": DatasetConfig(
        name="IEEE Fraud Detection",
        source_type=SourceType.KAGGLE,
        source_id="ieee-fraud-detection",
        filename="ieee_fraud.csv",
        description="IEEE fraud detection dataset",
        project_number=19
    ),
    
    # Project 20: AutoML
    "otto_products": DatasetConfig(
        name="Otto Product Classification",
        source_type=SourceType.KAGGLE,
        source_id="otto-group-product-classification-challenge",
        filename="otto_products.csv",
        description="Otto product classification dataset",
        project_number=20
    ),
    
    # Project 21: MLOps Pipeline
    "wine_quality": DatasetConfig(
        name="Wine Quality",
        source_type=SourceType.URL,
        source_id="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
        filename="wine_quality.csv",
        description="Wine quality dataset for MLOps",
        project_number=21
    ),
    
    # Project 22: Distributed ML
    "spotify_tracks": DatasetConfig(
        name="Spotify Tracks",
        source_type=SourceType.KAGGLE,
        source_id="yamaerenay/spotify-dataset-19212020-160k-tracks",
        filename="spotify_tracks.csv",
        description="Spotify tracks dataset for distributed processing",
        project_number=22
    )
}

def get_project_datasets(project_number: int) -> List[DatasetConfig]:
    """Returns all datasets needed for a specific project"""
    return [config for config in DATASETS.values() if config.project_number == project_number]