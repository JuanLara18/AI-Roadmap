from pathlib import Path
import kaggle
from .base import DataSource

class KaggleSource(DataSource):
    """Handles downloading datasets from Kaggle"""
    def download(self, dataset_id: str, output_path: Path) -> None:
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(
            dataset_id,
            path=output_path.parent,
            unzip=True
        )