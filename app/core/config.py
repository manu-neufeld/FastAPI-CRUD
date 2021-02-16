from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings
from typing import List

config = Config(".env")

API_PREFIX = "/api"
PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)
DEBUG: bool = config("DEBUG", cast=bool, default=False)
VERSION = "0.0.1"