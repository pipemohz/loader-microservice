import os
from decouple import config

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')\
        or os.environ.get('SECRET_KEY')\
        or '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or \
        "IBQj^J9(HEAf#v0l'dvsdK3JcM4*ET"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # Flask-JSON Settings
    JSON_ADD_STATUS = False
    JSON_SORT_KEYS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config('POSTGRES_URI_TEST', None)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = config('POSTGRES_URI_TEST', None)


class ProductionConfig(Config):
    PRODUCTION = True
    SQLALCHEMY_DATABASE_URI = config('POSTGRES_URI', None)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
