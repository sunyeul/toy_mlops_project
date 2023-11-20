from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf
from enum import Enum
from configs.base_conf import BaseConfig
from configs.dir_conf import DirConfig, LocalDirConfig, ColabDirConfig

import hydra


class Phase(Enum):
    TRAIN = "train"
    TEST = "test"


@dataclass
class PrepareFeaturesConfig(BaseConfig):
    phase: Phase = Phase.TRAIN
    dir: DirConfig = DirConfig


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        name="prepare_features",
        node=PrepareFeaturesConfig,
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
    config_name="prepare_features",
)
def my_app(cfg: PrepareFeaturesConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    register_configs()
    my_app()
