from src.preprocess import preprocess_titanic_data
from configs.prepare_features_conf import PrepareFeaturesConfig, register_configs
from tqdm import tqdm
from pathlib import Path

import polars as pl
import numpy as np
import hydra

register_configs()


def save_features_as_npy(df: pl.DataFrame, output_dir: str):
    for col in tqdm(df.columns, total=df.shape[1]):
        feature_array = df[col].to_numpy()
        np.save(f"{output_dir}/{col}.npy", feature_array)


@hydra.main(config_name="prepare_features", version_base=None)
def main(cfg: PrepareFeaturesConfig):
    raw_data_dir_path: Path = Path(cfg.dir.raw_data_dir_path)
    file_path = raw_data_dir_path / f"{cfg.phase.value}.csv"

    feature_dir_path = Path(cfg.dir.features_dir_path) / f"{cfg.phase.value}"
    feature_dir_path.mkdir(exist_ok=True, parents=True)

    df = pl.read_csv(file_path)
    preprocessed_df = preprocess_titanic_data(df)
    save_features_as_npy(df=preprocessed_df, output_dir=feature_dir_path)


if __name__ == "__main__":
    main()
