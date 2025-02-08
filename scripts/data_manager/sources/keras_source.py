from pathlib import Path
import numpy as np
from tensorflow import keras
from .base import DataSource

class KerasSource(DataSource):
    """Handles downloading datasets from Keras"""
    def download(self, dataset_id: str, output_path: Path) -> None:
        loader = getattr(keras.datasets, dataset_id)
        (x_train, y_train), (x_test, y_test) = loader.load_data()
        
        np.savez(
            output_path,
            x_train=x_train,
            y_train=y_train,
            x_test=x_test,
            y_test=y_test
        )