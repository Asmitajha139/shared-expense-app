from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from typing import Optional


class SettlementCreate(BaseModel):
    group_id: int
    payer_id: int
    receiver_id: int
    amount: Decimal
    note: Optional[str] = None


class SettlementResponse(BaseModel):
    id: int
    group_id: int
    payer_id: int
    receiver_id: int
    amount: Decimal
    settlement_date: datetime
    note: Optional[str]

    class Config:
        from_attributes = True