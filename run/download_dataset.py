from configs.download_dataset_conf import DownloadDatasetConfig, register_configs
from src.utils.timer import timer
from src.utils.kaggle_dataset_manager import KaggleDatasetManager
from pathlib import Path

import hydra
import zipfile

register_configs()


@hydra.main(config_name="download_dataset", version_base=None)
def main(cfg: DownloadDatasetConfig):
    raw_data_dir_path: Path = Path(cfg.dir.raw_data_dir_path)
    raw_data_dir_path.mkdir(exist_ok=True, parents=True)

    manager = KaggleDatasetManager()

    with timer(prefix="Downloading files took ", suffix=" seconds"):
        manager.download_from_kaggle(
            competition_name=cfg.competition_name, download_dir_path=raw_data_dir_path
        )

    with timer(prefix="Extracting files took ", suffix=" seconds"):
        path_to_zip_file = raw_data_dir_path / f"{cfg.competition_name}.zip"
        directory_to_extract_to = raw_data_dir_path

        with zipfile.ZipFile(path_to_zip_file, "r") as zip_ref:
            zip_ref.extractall(directory_to_extract_to)

        path_to_zip_file.unlink()


if __name__ == "__main__":
    main()
