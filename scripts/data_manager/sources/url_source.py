import requests
import pandas as pd
import io
from pathlib import Path
from .base import DataSource

class URLSource(DataSource):
    """Handles downloading datasets from direct URLs"""
    def download(self, dataset_id: str, output_path: Path) -> None:
        response = requests.get(dataset_id)
        response.raise_for_status()
        
        if output_path.suffix == '.csv':
            df = pd.read_csv(io.StringIO(response.text))
            df.to_csv(output_path, index=False)
        else:
            with open(output_path, 'wb') as f:
                f.write(response.content)