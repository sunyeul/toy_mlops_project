from pathlib import Path
import shutil
import json
from kaggle.api.kaggle_api_extended import KaggleApi

# Constants
TEMP_DIR_PATH = "./tmp"


class KaggleDatasetManager:
    def __init__(self):
        self.api = KaggleApi()
        self.api.authenticate()

    @staticmethod
    def copy_files(source_dir: Path, dest_dir: Path, target_file_list: list):
        """Copy specified files from source to destination directory."""
        for target_file in target_file_list:
            for source_path in source_dir.rglob(f"*{target_file}"):
                relative_path = source_path.relative_to(source_dir)
                dest_path = dest_dir / relative_path
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_path, dest_path)
                print(f"Copied {source_path} to {dest_path}")

    @staticmethod
    def create_temp_dir() -> Path:
        """Create and return a temporary directory."""
        tmp_dir = Path(TEMP_DIR_PATH)
        tmp_dir.mkdir(parents=True, exist_ok=True)
        return tmp_dir

    @staticmethod
    def delete_temp_dir(tmp_dir: Path):
        """Delete the specified temporary directory."""
        shutil.rmtree(tmp_dir)

    @staticmethod
    def create_dataset_metadata(tmp_dir: Path, user_name: str, title: str):
        """Create dataset metadata file in the specified directory."""
        dataset_metadata = {
            "id": f"{user_name}/{title}",
            "licenses": [{"name": "CC0-1.0"}],
            "title": title,
        }
        with open(tmp_dir / "dataset-metadata.json", "w") as f:
            json.dump(dataset_metadata, f, indent=4)

    def upload_to_kaggle(self, tmp_dir: Path, new: bool):
        """Upload dataset to Kaggle."""
        if new:
            self.api.dataset_create_new(
                folder=tmp_dir, dir_mode="tar", convert_to_csv=False, public=False
            )
        else:
            self.api.dataset_create_version(
                folder=tmp_dir, version_notes="", dir_mode="tar", convert_to_csv=False
            )

    def download_from_kaggle(self, competition_name: str, download_dir_path: str):
        """Download competition files from Kaggle."""
        self.api.competition_download_files(
            competition=competition_name, path=Path(download_dir_path)
        )


# Example usage:
# manager = KaggleDatasetManager()
# tmp_dir = manager.create_temp_dir()
# manager.copy_files(Path('source'), tmp_dir, ['file1.txt', 'file2.txt'])
# manager.create_dataset_metadata(tmp_dir, 'username', 'dataset_title')
# manager.upload_to_kaggle(tmp_dir, new=True)
# manager.delete_temp_dir(tmp_dir)


# Example usage:
# manager = KaggleDatasetManager()
# manager.download_from_kaggle('titanic', './download')
