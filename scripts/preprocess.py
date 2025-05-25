import pandas as pd

df = pd.read_csv("data/raw/data_v1.csv")

# Simple normalization (optional)
df.iloc[:, :-1] = df.iloc[:, :-1] / df.iloc[:, :-1].max()

df.to_csv("data/processed/processed_v1.csv", index=False)
print("✅ Data preprocessing complete.")
