from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.db.session import SessionLocal
from app.cruds import user as user_crud
from app.schemas.user import UserLogin, Token
from app.core.security import create_access_token
from app.cruds.user import verify_password
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

# Dependency — подключение к базе
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sign-up/", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
    return user_crud.create_user(db, user)

@router.post("/login/", response_model=Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, user_login.email)
    if not db_user or not verify_password(user_login.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Неверный email или пароль")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/users/me/", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user