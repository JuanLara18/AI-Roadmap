from pathlib import Path
from typing import Dict, Type
from .sources.base import DataSource
from .sources.kaggle_source import KaggleSource
from .sources.url_source import URLSource
from .config.datasets import DATASETS, SourceType

class DatasetDownloader:
    """Manages dataset downloading from various sources"""
    
    def __init__(self):
        self.sources = {
            SourceType.KAGGLE: KaggleSource(),
            SourceType.URL: URLSource(),
            SourceType.SKLEARN: SklearnSource(),
            SourceType.KERAS: KerasSource()
        }
    
    def download_project(self, project_number: int) -> None:
        """Downloads all datasets needed for a specific project"""
        datasets = get_project_datasets(project_number)
        for dataset_config in datasets:
            self.download_dataset(dataset_config)
    
    def download_dataset(self, config: DatasetConfig) -> None:
        project_folder = f"{config.project_number:02d}-{config.name.lower().replace(' ', '-')}"
        output_path = Path(f"projects/{project_folder}/data") / config.filename
        
        source = self.sources.get(config.source_type)
        if not source:
            raise ValueError(f"Source type {config.source_type} not supported")
        
        source.download(config.source_id, output_path)