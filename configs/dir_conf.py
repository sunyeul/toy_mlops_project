from dataclasses import dataclass

import os


@dataclass
class DirConfig:
    base_dir_path: str
    data_dir_path: str
    raw_data_dir_path: str
    features_dir_path: str
    models_dir_path: str


@dataclass
class LocalDirConfig(DirConfig):
    base_dir_path: str = "/Users/junhyeong.kim/Private_Workspaces/toy_mlops_project"
    data_dir_path: str = os.path.join(base_dir_path, "data")
    raw_data_dir_path: str = os.path.join(data_dir_path, "raw")
    features_dir_path: str = os.path.join(base_dir_path, "features")
    models_dir_path: str = os.path.join(base_dir_path, "features")


@dataclass
class ColabDirConfig(DirConfig):
    base_dir_path: str = "/content/kaggle-child-mind-institute-detect-sleep-states"
    data_dir_path: str = os.path.join(base_dir_path, "data")
    raw_data_dir_path: str = os.path.join(data_dir_path, "raw")
    features_dir_path: str = os.path.join(base_dir_path, "features")
    models_dir_path: str = os.path.join(base_dir_path, "features")
