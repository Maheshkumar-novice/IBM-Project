from dotenv import load_dotenv
load_dotenv()

import os

basedir = os.path.abspath(os.path.dirname(__file__))

CONFIG_OBJECT_NAME = os.getenv('CONFIG_OBJECT_NAME', 'config.DevelopmentConfig')

class Config():
    EMAIL_CONFIRMATION_SENDER_EMAIL =os.getenv('EMAIL_CONFIRMATION_SENDER_EMAIL')
    EMAIL_CONFIRMATION_SALT = 'email-confirmation'
    EMAIL_CONFIRMATION_TOKEN_MAX_AGE_SECONDS = 300
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    API_VERSION_PREFIX = os.getenv('API_VERSION_PREFIX', '/api/v1/')
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "app.db")}'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
