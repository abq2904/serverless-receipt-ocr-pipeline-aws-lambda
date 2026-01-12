from pydantic import BaseModel
from typing import Optional

class Receipt(BaseModel):
    merchant: Optional[str]
    date: Optional[str]
    subtotal: Optional[float]
    tax: Optional[float]
    total: Optional[float]
