import os

from db import models
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db_name = os.environ['PG_DB']
db_user = os.environ['PG_USER']
db_pass = os.environ['PG_PASS']
db_uri = f'postgresql://{db_user}:{db_pass}@cybellum_db:5432/{db_name}'
Base = declarative_base()

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.secret_key = 'secret!!1'
db = SQLAlchemy()
db.init_app(app)
bcrypt = Bcrypt(app)
