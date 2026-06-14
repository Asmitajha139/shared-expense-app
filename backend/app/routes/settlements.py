from fastapi import APIRouter, status
from typing import Dict, List
from app.schemas.settlement import SettlementCreate, SettlementResponse

router = APIRouter()

SETTLEMENT_DATABASE: Dict[int, dict] = {}
SETTLEMENT_ID_COUNTER = 1

@router.post("/", response_model=SettlementResponse, status_code=status.HTTP_201_CREATED)
def create_settlement(settlement: SettlementCreate):
    global SETTLEMENT_ID_COUNTER
    settlement_data = settlement.dict()
    settlement_data["id"] = SETTLEMENT_ID_COUNTER
    SETTLEMENT_DATABASE[SETTLEMENT_ID_COUNTER] = settlement_data
    SETTLEMENT_ID_COUNTER += 1
    return settlement_data

@router.get("/", response_model=List[SettlementResponse], status_code=status.HTTP_200_OK)
def get_settlements():
    return list(SETTLEMENT_DATABASE.values())