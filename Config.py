"""
Application configuration.
Loads settings from environment variables / .env file.
"""
from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --- App ---
    APP_NAME: str = "AI Sales & Support Agent"
    ENVIRONMENT: str = Field(default="development")
    DEBUG: bool = Field(default=True)
    API_V1_PREFIX: str = "/api/v1"

    # --- Security / Auth ---
    SECRET_KEY: str = Field(default="CHANGE_ME_IN_PRODUCTION")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # --- Database ---
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/ai_sales_agent"
    )
    DATABASE_URL_SYNC: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/ai_sales_agent"
    )

    # --- CORS ---
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    # --- LLM Providers ---
    LLM_PROVIDER: str = Field(default="openai")  # "openai" | "gemini"
    OPENAI_API_KEY: str = Field(default="")
    OPENAI_MODEL: str = Field(default="gpt-4o-mini")
    GEMINI_API_KEY: str = Field(default="")
    GEMINI_MODEL: str = Field(default="gemini-1.5-pro")

    # --- Embeddings / Vector store ---
    EMBEDDING_MODEL: str = Field(default="all-MiniLM-L6-v2")
    CHROMA_PERSIST_DIR: str = Field(default="./chroma_db")
    CHROMA_COLLECTION_NAME: str = Field(default="company_documents")

    # --- File uploads ---
    UPLOAD_DIR: str = Field(default="./uploads")
    MAX_UPLOAD_SIZE_MB: int = 20

    # --- Rate limiting / misc ---
    ESCALATION_CONFIDENCE_THRESHOLD: float = 0.55


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
