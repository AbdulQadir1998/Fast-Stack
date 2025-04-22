from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    RACKBEAT_API_KEY: str
    RACKBEAT_API_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
