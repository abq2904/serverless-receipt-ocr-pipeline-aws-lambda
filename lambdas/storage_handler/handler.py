import json
from pathlib import Path
from shared.logger import get_logger

logger = get_logger()

with open("config.json") as f:
    config = json.load(f)

PROCESSED_BUCKET = Path(config["processed_bucket"])
PROCESSED_BUCKET.mkdir(parents=True, exist_ok=True)

def handle_storage_event(event: dict):
    object_key = event["object_key"]
    receipt = event["receipt"]

    output_path = PROCESSED_BUCKET / f"{object_key}.json"

    with open(output_path, "w") as f:
        json.dump(receipt, f, indent=2)

    logger.info(f"[STORAGE_LAMBDA] Stored {output_path}")

    return receipt
