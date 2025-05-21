from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import create_access_token, verify_password, get_db, get_current_user
from app.schemas.auth import UserCreate, UserRead, Token
from app.cruds.user import get_user_by_email, create_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=UserRead)
def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user_in)

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
    access_token = create_access_token({"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
def read_users_me(current_user=Depends(get_current_user)):
    return current_user
