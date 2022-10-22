from pydantic import BaseSettings


class Settings(BaseSettings):
    LONG_POLL_ACCESS_TOKEN: str
    MESSAGES_ACCESS_TOKEN: str
    GROUP_ID: str
    API_VERSION: str


settings = Settings()
