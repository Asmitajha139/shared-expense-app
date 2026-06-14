from fastapi import APIRouter, status
from typing import Dict, List
from app.schemas.group import GroupCreate, GroupResponse

router = APIRouter()

GROUP_DATABASE: Dict[int, dict] = {}
GROUP_ID_COUNTER = 1

@router.post("/", response_model=GroupResponse, status_code=status.HTTP_201_CREATED)
def create_group(group: GroupCreate):
    global GROUP_ID_COUNTER
    group_data = group.dict()
    group_data["id"] = GROUP_ID_COUNTER
    GROUP_DATABASE[GROUP_ID_COUNTER] = group_data
    GROUP_ID_COUNTER += 1
    return group_data

@router.get("/", response_model=List[GroupResponse], status_code=status.HTTP_200_OK)
def get_groups():
    return list(GROUP_DATABASE.values())