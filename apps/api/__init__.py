from flask import Flask
from config.settings import config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Init db instance
    db.init_app(app)

    from apps.common.models.records import Record

    # Register blueprints here
    from apps.api.main import main as main_blueprint
    from apps.api.loader import loader as loader_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(loader_blueprint)

    return app
