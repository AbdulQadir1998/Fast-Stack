from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    email: str
    access_token: str

class TokenData(BaseModel):
    email: str | None = None
