"""
Create feature CSVs for train and test datasets
"""
import json
import numpy as np
import pandas as pd


def featurization():
    # Load data-sets
    print("Loading data sets...")
    train_data = pd.read_csv('./data/raw/train_data.csv', header=None, dtype=float)
    test_data = pd.read_csv('./data/raw/test_data.csv', header=None, dtype=float)
    print("done.")

    # Normalize the train data
    print("Normalizing data...")
    # We choose all columns except the first, since that is where our labels are
    train_mean = train_data.values[:, 1:].mean()
    train_std = train_data.values[:, 1:].std()

    # Normalize train and test data according to the train data distribution
    train_data.values[:, 1:] -= train_mean
    train_data.values[:, 1:] /= train_std
    test_data.values[:, 1:] -= train_mean
    test_data.values[:, 1:] /= train_std

    print("done.")

    print("Saving processed datasets and normalization parameters...")
    # Save normalized data-sets
    np.save('./data/processed/train_data.npy', train_data)
    np.save('./data/processed/test_data.npy', test_data)

    # Save mean and std for future inference
    with open('./data/processed/norm_params.json', 'w') as f:
        json.dump({'mean': train_mean, 'std': train_std}, f)

    print("done.")


if __name__ == '__main__':
    featurization()
