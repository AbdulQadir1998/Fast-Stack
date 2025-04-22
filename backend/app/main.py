from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth.routes import router as auth_router
from app.product.routes import router as products_router
from fastapi.security import HTTPBearer

app = FastAPI(
    title="FastAPI + Rackbeat Backend",
    description="JWT-protected product API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(products_router, prefix="/api", tags=["products"])
