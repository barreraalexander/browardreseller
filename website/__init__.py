from flask import Flask
from flask_assets import Environment
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_login import LoginManager
from website.db import DB
from website.config import DBConfig, cacheConfig
from website.utils.assets import bundles



assets = Environment()
bcrypt = Bcrypt()
cache = Cache(config=cacheConfig)
db = DB()

login_user = LoginManager()
login_user.login_view = 'users.login'
login_user.login_message_category = 'info'

login_manager = LoginManager()
login_manager.login_view = 'managers.backstage'
login_manager.login_message_category = 'info'



def create_app (config_class=DBConfig):
    app = Flask (__name__)
    app.config.from_object(DBConfig)
    
    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)

    login_user.init_app(app)
    login_manager.init_app(app)

    from website.blueprints.main.routes import main
    from website.blueprints.managers.routes import managers
    from website.blueprints.users.routes import users

    app.register_blueprint  (main)
    app.register_blueprint  (managers)
    app.register_blueprint  (users)

    assets.register(bundles)
    
    return app