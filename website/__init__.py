from flask import Flask
from flask_assets import Environment
from website.utils.assets import bundles
from website.db import DB
from website.config import Config


db = DB()
assets = Environment()

def create_app (config_class=Config):
    app = Flask (__name__)
    app.config.from_object(Config)
    assets.init_app(app)
    db.init_app(app)

    from website.main.routes import main

    assets.register(bundles)
    app.register_blueprint  (main)

    return app