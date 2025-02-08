from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

class DataSource(ABC):
    """Base class for all data sources"""
    @abstractmethod
    def download(self, dataset_id: str, output_path: Path) -> None:
        """Downloads dataset from the source"""
        pass