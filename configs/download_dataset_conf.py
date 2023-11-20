from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf

from configs.base_conf import BaseConfig
from configs.dir_conf import DirConfig, LocalDirConfig, ColabDirConfig

import hydra


@dataclass
class DownloadDatasetConfig(BaseConfig):
    competition_name: str = "titanic"
    dir: DirConfig = DirConfig


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        name="download_dataset",
        node=DownloadDatasetConfig,
    )
    cs.store(
        group="dir",
        name="local",
        node=LocalDirConfig,
    )
    cs.store(
        group="dir",
        name="colab",
        node=ColabDirConfig,
    )


@hydra.main(
    version_base=None,
    config_name="download_dataset",
)
def my_app(cfg: DownloadDatasetConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    register_configs()
    my_app()
