"""All Configs Here"""

# Libraries
from os import getenv
from typing import Dict
from enum import Enum
from pathlib import Path
from dotenv import load_dotenv


env_path = Path() / ".env"
load_dotenv(env_path)

# Classes
class ModeServer(str, Enum):
    PRODUCTION = "production"
    TESTING = "testing"
    DEVELOP = "develop"


class ApiEntrypoint(str, Enum):
    FASTAPI = "fastapi"


class ORMMOdule(str, Enum):
    SQLALCHEMY = "sqlalchemy"


MODE = getenv("MODE", "production").lower()


class Config:
    DEBUG: bool = getenv("DEBUG", "false").lower() in ["true", "t", "1", "ok", "on"]
    MODE: ModeServer = ModeServer(MODE)
    API_ENTRYPOINT: ApiEntrypoint = ApiEntrypoint(getenv("API_ENTRYPOINT", "fastapi").lower())
    ORM_MODULE: ORMMOdule = ORMMOdule(getenv("ORM_MODULE", "sqlalchemy").lower())


class TestConfig(Config):
    pass


class DevelopConfig(Config):
    pass


class ProductionConfig(Config):
    pass


modes_config: Dict[ModeServer, Config] = {
    ModeServer.DEVELOP: DevelopConfig(),
    ModeServer.TESTING: TestConfig(),
    ModeServer.PRODUCTION: ProductionConfig(),
}
config: Config = modes_config[ModeServer(MODE)]
