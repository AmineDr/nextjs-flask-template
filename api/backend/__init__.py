from flask import Flask
from flask_session import Session as Sess
from flask_migrate import Migrate

from backend.models import *
from backend.config import DevelopmentConfig, ProductionConfig, config


app = Flask(__name__)

app.env = config.env

if app.env == 'dev':
    app.config.from_object(DevelopmentConfig)
elif app.env == 'prod':
    app.config.from_object(ProductionConfig)
else:
    raise ValueError("Invalid environment configuration")

from backend.routes import *

app.config["SESSION_SQLALCHEMY"] = db

db.init_app(app)
migrate = Migrate(app, db)

Sess(app)
CORS(app)

with app.app_context():
    db.create_all()
