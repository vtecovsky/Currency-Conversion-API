from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    class Config:
        env_file = ".env.local"
        env_file_encoding = "utf-8"

    DB_URL: str
    ACCESS_KEY: str


settings = Settings()
