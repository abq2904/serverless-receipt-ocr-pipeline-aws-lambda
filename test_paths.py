from pathlib import Path
import json

with open("config.json") as f:
    config = json.load(f)

raw_bucket = Path(config["raw_bucket"])
processed_bucket = Path(config["processed_bucket"])

raw_bucket.mkdir(parents=True, exist_ok=True)
processed_bucket.mkdir(parents=True, exist_ok=True)

print("✅ Raw bucket:", raw_bucket.resolve())
print("✅ Processed bucket:", processed_bucket.resolve())
