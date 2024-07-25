from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    allowed_hosts: str = Field(alias="ALLOWED_HOSTS", default="localhost")
    debug: str = Field(alias="DEBUG", default="false")
    secret_key: str = Field(alias="SECRET_KEY", default="Undefined")
    session_cookie_time: int = Field(alias="COOKIE_TIME", default=14)  #  Pass in days.

    db_name: str = Field(alias="DB_NAME", default="management")
    db_username: str = Field(alias="DB_USERNAME", default="postgres")
    db_password: str = Field(alias="DB_PASSWORD", default="postgres")
    db_host: str = Field(alias="DB_HOST", default="localhost")
    db_port: int = Field(alias="DB_PORT", default=5432)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.debug = self.__str_to_bool(self.debug)

    def __str_to_bool(self, val: str | bool) -> bool:
        if isinstance(val, str):
            return val.lower() in ("true", "yes", "y")
        
        return val

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
