from typing import Optional, List, ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    debug: Optional[bool] = False
    redis_host: str = ""
    redis_port: str = ""

    url_api: str = ""

    email_host: str = ""
    email_port: int = 587
    email_host_user: str = ""
    email_host_password: str = ""
    allowed_hosts: ClassVar[List[str]] = ["https://emagiceyes.rainscales.com"]


settings = Settings()
