import json
from pathlib import Path
import pytesseract
import cv2
from shared.logger import get_logger

logger = get_logger()

# Load config
with open("config.json") as f:
    config = json.load(f)

RAW_BUCKET = Path(config["raw_bucket"])
RAW_BUCKET.mkdir(parents=True, exist_ok=True)

def handle_ocr_event(event: dict):
    object_key = event["object_key"]
    image_path = RAW_BUCKET / object_key

    logger.info(f"[OCR_LAMBDA] Processing {object_key}")

    image = cv2.imread(str(image_path))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray, lang=config.get("ocr_languages", "eng"))

    logger.info("[OCR_LAMBDA] OCR completed")

    text = pytesseract.image_to_string(image)
    print("[OCR_LAMBDA] OCR Output:\n", text)


    return {"object_key": object_key, "ocr_text": text}

