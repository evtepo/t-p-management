from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    secret_key: str = Field(alias="SECRET_KEY", default="Undefined")
    debug: bool = bool(Field(alias="DEBUG", default=False))

    session_cookie_time: int = Field(alias="COOKIE_TIME", default=14)  #  Pass in days.

    db_name: str = Field(alias="DB_NAME", default="management")
    db_username: str = Field(alias="DB_USERNAME", default="postgres")
    db_password: str = Field(alias="DB_PASSWORD", default="postgres")
    db_host: str = Field(alias="DB_HOST", default="localhost")
    db_port: int = Field(alias="DB_PORT", default=5432)


settings = Settings()
