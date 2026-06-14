from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class ExpenseCreate(BaseModel):
    group_id: int
    title: str
    amount: Decimal
    paid_by: int


class ExpenseResponse(BaseModel):
    id: int
    group_id: int
    title: str
    amount: Decimal
    paid_by: int
    expense_date: datetime

    class Config:
        from_attributes = True