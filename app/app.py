from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from db import models

from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = models.db_uri
db = SQLAlchemy()
db.init_app(app)

@app.route('/flask')
def hello_world():
    return 'Hello from Flask!\n'

@app.route('/db')
def db_sample():
    user = db.get_or_404(models.User, '123')


    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)