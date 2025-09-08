import pandas as pd

FEATURE_FILE = "data/features.csv"

def save_features(features_df):
    features_df.to_csv(FEATURE_FILE, index=False)

def load_features():
    return pd.read_csv(FEATURE_FILE)