import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json

df = pd.read_csv("data/processed/processed_v1.csv")
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

with open("models/model_v1.pkl", "wb") as f:
    pickle.dump(model, f)

# Save accuracy to a JSON file
with open("models/metrics.json", "w") as f:
    json.dump({"accuracy": acc}, f)

print(f"✅ Model trained with accuracy: {acc:.2f}")
