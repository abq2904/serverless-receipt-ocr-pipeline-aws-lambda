import logging

# Configure logger for this module
logger = logging.getLogger("receipt_pipeline")
logger.setLevel(logging.INFO)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

import re  # <-- Add this


def parse_receipt_text(ocr_input) -> dict:
    """
    Extracts merchant, date, subtotal, tax, and total from OCR output.
    ocr_input can be a string (raw OCR) or dict with key 'text'
    """
    # Extract text if dict
    if isinstance(ocr_input, dict):
        ocr_text = ocr_input.get("text", "")
    else:
        ocr_text = str(ocr_input)

    # Split into lines and remove empty lines
    lines = [line.strip() for line in ocr_text.splitlines() if line.strip()]
    
    # Merchant
    merchant = lines[0] if lines else None
    if merchant:
        merchant = re.sub(r'[^a-zA-Z\s]', '', merchant).strip()

    # Date
    date_pattern = r'(\d{1,2}/\d{1,2}/\d{2,4})'
    date_match = re.search(date_pattern, ocr_text)
    date = date_match.group(1) if date_match else None

    # Numbers
    ocr_text_norm = ocr_text.replace(',', '.')
    
    subtotal_pattern = r'Subtotal\s*\$?(\d+\.\d+)?'
    tax_pattern = r'Tax\s*\$?(\d+\.\d+)?'
    total_pattern = r'Total\s*\$?(\d+\.\d+)?'

    subtotal_match = re.search(subtotal_pattern, ocr_text_norm, re.IGNORECASE)
    tax_match = re.search(tax_pattern, ocr_text_norm, re.IGNORECASE)
    total_match = re.search(total_pattern, ocr_text_norm, re.IGNORECASE)

    subtotal = float(subtotal_match.group(1)) if subtotal_match and subtotal_match.group(1) else 0.0
    tax = float(tax_match.group(1)) if tax_match and tax_match.group(1) else 0.0
    total = float(total_match.group(1)) if total_match and total_match.group(1) else 0.0

    logger.info("[PARSER_LAMBDA] Receipt parsed")

    return {
        "merchant": merchant,
        "date": date,
        "subtotal": subtotal,
        "tax": tax,
        "total": total
    }

def handle_parse_event(ocr_output) -> dict:
    return parse_receipt_text(ocr_output)
