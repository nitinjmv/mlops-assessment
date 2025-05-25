import json
import sys

with open("models/metrics.json") as f:
    metrics = json.load(f)

acc = metrics["accuracy"]
threshold = 0.7

print(f"📊 Model accuracy: {acc:.2f}")
if acc < threshold:
    print(f"❌ Accuracy {acc:.2f} is below threshold {threshold}")
    sys.exit(1)
else:
    print(f"✅ Accuracy {acc:.2f} meets threshold {threshold}")
