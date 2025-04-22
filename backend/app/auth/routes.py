from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas import UserCreate, UserOut
from app.models import fake_users_db
from app.auth import jwt

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed = jwt.hash_password(user.password)
    fake_users_db[user.email] = hashed
    token = jwt.create_access_token({"sub": user.email})
    return {"email": user.email, "access_token": token}

@router.post("/signin", response_model=UserOut)
def signin(user: UserCreate):
    hashed = fake_users_db.get(user.email)
    if not hashed or not jwt.verify_password(user.password, hashed):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.create_access_token({"sub": user.email})
    return {"email": user.email, "access_token": token}
