from dotenv import load_dotenv
load_dotenv()

import os

basedir = os.path.abspath(os.path.dirname(__file__))

CONFIG_TYPE=os.getenv('CONFIG_TYPE', 'config.DevelopmentConfig')

class Config():
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "app.db")}'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
