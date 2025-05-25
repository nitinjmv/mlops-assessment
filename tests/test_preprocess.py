import pandas as pd
import os

def test_preprocessed_file_exists():
    assert os.path.exists("data/processed/processed_v1.csv"), "Processed file missing"

def test_preprocessed_data_shape():
    df = pd.read_csv("data/processed/processed_v1.csv")
    assert df.shape[1] == 4, "Expected 4 columns (3 features + 1 target)"
    assert "target" in df.columns, "Target column missing"
