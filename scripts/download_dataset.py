from data_manager.downloader import DatasetDownloader
from data_manager.config.datasets import DATASETS

def main():
    """Main script for downloading project datasets"""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python download_project_data.py <project_number>")
        print("\nAvailable projects:")
        for config in DATASETS.values():
            print(f"{config.project_number:2d}: {config.name} - {config.description}")
        sys.exit(1)
    
    try:
        project_number = int(sys.argv[1])
        downloader = DatasetDownloader()
        downloader.download_project(project_number)
        print(f"Successfully downloaded datasets for project {project_number}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()