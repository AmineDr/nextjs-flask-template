from types import SimpleNamespace
import json
import os

from backend.errors import ConfigError

try:
    with open(os.path.abspath("./backend/config/config.json")) as f:
        config = json.loads(f.read(), object_hook=lambda x: SimpleNamespace(**x))
except json.JSONDecodeError or FileNotFoundError:
    raise ConfigError


class Config:
    """ You can add whatever to the config.json file and use it here """
    DEBUG = False
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = ""
    STATIC_FOLDER = './static'
    SESSION_TYPE = "sqlalchemy"
    SESSION_SQLALCHEMY = None


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{config.database_dev.name}"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{config.database.user}:{config.database.password}@{config.database.host}/{config.database.name}"
