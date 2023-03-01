from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dtime

app = Flask(__name__)

app.config.from_object('app.configuration.DevelopmentConfig')

db = SQLAlchemy(app)

from app import views, models