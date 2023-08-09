from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if os.environ.get('RUNNING_IN_CONTAINER', False):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1235@db:5432/bookairfreight_database'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1235@localhost:5432/bookairfreight_database'

db = SQLAlchemy(app)

from quote_api import routes