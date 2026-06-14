from fastapi import APIRouter, status
from typing import Dict, List
from app.schemas.expense import ExpenseCreate, ExpenseResponse

router = APIRouter()

EXPENSE_DATABASE: Dict[int, dict] = {}
EXPENSE_ID_COUNTER = 1

@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create_expense(expense: ExpenseCreate):
    global EXPENSE_ID_COUNTER
    expense_data = expense.dict()
    expense_data["id"] = EXPENSE_ID_COUNTER
    EXPENSE_DATABASE[EXPENSE_ID_COUNTER] = expense_data
    EXPENSE_ID_COUNTER += 1
    return expense_data

@router.get("/", response_model=List[ExpenseResponse], status_code=status.HTTP_200_OK)
def get_expenses():
    return list(EXPENSE_DATABASE.values())