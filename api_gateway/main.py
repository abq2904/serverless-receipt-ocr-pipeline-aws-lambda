from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil
from uuid import uuid4

from lambdas.ocr_processor.handler import handle_ocr_event
from lambdas.receipt_parser.handler import handle_parse_event
from lambdas.storage_handler.handler import handle_storage_event
from shared.logger import get_logger

logger = get_logger()

app = FastAPI(title="Serverless Receipt Processing API")
RAW_BUCKET = Path("storage/raw_receipts")
RAW_BUCKET.mkdir(parents=True, exist_ok=True)

@app.post("/upload")
async def upload_receipt(file: UploadFile = File(...)):
    # Save file to raw_receipts
    file_id = f"{uuid4()}.jpg"
    file_path = RAW_BUCKET / file_id

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"[API_GATEWAY] Uploaded {file_id}")

    # Event-driven simulation
    ocr_result = handle_ocr_event({"object_key": file_id})
    parsed_result = handle_parse_event(ocr_result)
    final_result = handle_storage_event({"object_key": file_id, "receipt": parsed_result})

    return final_result
