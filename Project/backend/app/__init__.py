import ibm_db_sa
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import CONFIG_TYPE

app = Flask(__name__)
app.config.from_object(CONFIG_TYPE)
db = SQLAlchemy(app)

from app.models import *

with app.app_context():
    db.create_all()
