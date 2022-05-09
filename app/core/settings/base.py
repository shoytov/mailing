# Base project config
from typing import Dict, List

from starlette.config import Config

config = Config(".env")

# ####### Main application settings #########
DEBUG: bool = config.get("DEBUG", cast=bool, default=True)
SERVICE_NAME: str = config.get("SERVICE_NAME", cast=str, default="")
VERSION: str = config.get("VERSION", cast=str, default="local")
TAGS_METADATA: List[Dict[str, str]] = [
    {
        "name": "v1",
        "description": "ver 1.0"
    }
]

# ################ Logging ##################
LOGGING_LEVEL = "info"
LOGGING_SERIALIZE = False

# ################ Formats ##################
DATE_FORMAT: str = config.get("DATE_FORMAT", cast=str, default="%d-%m-%Y")
DATETIME_FORMAT: str = config.get(
    "DATETIME_FORMAT", cast=str, default="%d-%m-%YT%H:%M:%S"
)
