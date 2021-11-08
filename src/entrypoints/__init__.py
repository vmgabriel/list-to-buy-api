"""All Entrypoints configuration"""

# Modules
from .fastapi import app as fastapi_app

# Config
from src.config import config, ApiEntrypoint

# Apps
app_restful = None

if config.API_ENTRYPOINT == ApiEntrypoint.FASTAPI:
    app_restful = fastapi_app
