from pathlib import Path
import pandas as pd
from sklearn import datasets
from .base import DataSource

class SklearnSource(DataSource):
    """Handles downloading datasets from scikit-learn"""
    def download(self, dataset_id: str, output_path: Path) -> None:
        loader = getattr(datasets, dataset_id)
        data = loader()
        
        if hasattr(data, 'data') and hasattr(data, 'target'):
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['target'] = data.target
            df.to_csv(output_path, index=False)
        else:
            raise ValueError(f"Unexpected dataset format for {dataset_id}")