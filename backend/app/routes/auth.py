from fastapi import APIRouter, HTTPException, status
from typing import Dict

from app.schemas.auth import UserRegister, UserLogin, TokenResponse

from app.utils.security import hash_password, verify_password
from app.utils.auth import create_access_token


router = APIRouter()

USER_DATABASE: Dict[str, dict] = {}
USER_ID_COUNTER = 1


@router.post(
    "/register",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED
)
async def register(payload: UserRegister):
    global USER_ID_COUNTER

    email_clean = payload.email.strip().lower()

    if email_clean in USER_DATABASE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    

    hashed_pwd = hash_password(payload.password)

   

    new_user = {
        "id": USER_ID_COUNTER,
        "name": payload.name.strip(),
        "email": email_clean,
        "password_hash": hashed_pwd
    }

    USER_DATABASE[email_clean] = new_user

    USER_ID_COUNTER += 1

    access_token = create_access_token(
    data={"sub": email_clean}
)

return TokenResponse(
    access_token=access_token,
    token_type="bearer"
)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK
)
async def login(payload: UserLogin):

    email_clean = payload.email.strip().lower()

    user_record = USER_DATABASE.get(email_clean)

    if not user_record:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    if not verify_password(
        payload.password,
        user_record["password_hash"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    access_token = create_access_token(
        data={"sub": email_clean}
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer"
    )