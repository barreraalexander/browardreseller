from flask import Flask
from flask_assets import Environment
from browardreseller.utils.assets import bundles
from browardreseller.db import DB
from browardreseller.config import Config


db = DB()
assets = Environment()

def create_app (config_class=Config):
    app = Flask (__name__)
    app.config.from_object(Config)
    assets.init_app(app)
    db.init_app(app)

    from browardreseller.main.routes import main

    assets.register(bundles)
    app.register_blueprint  (main)

    return app