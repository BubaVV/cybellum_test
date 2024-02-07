from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from db import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import jsonify, abort

db = SQLAlchemy()
engine = create_engine(models.db_uri)
Session = sessionmaker(bind=engine) 
session = Session()

class User(Resource):
    def get(self, id=None):
        if id:
            result = session.query(models.User).filter(models.User.id == id).one_or_none()
            if result:
                return jsonify(result)
            else:
                abort(404, f"User id {id} doesn't exist.")
        else:
            return jsonify("Current user info - not implemented yet")
    def post(self, id):
        pass

class Post(Resource):
    def get(self, id=None):
        if id:
            result = session.query(models.Post).filter(models.Post.id == id).one_or_none()
            if result:
                return jsonify(result)
            else:
                abort(404, f"Post id {id} doesn't exist.")
        else:
            result = session.query(models.Post).all()
            return jsonify(result)
    def post(self, id):
        pass

class Comment(Resource):
    def get(self, post_id):
        result = session.query(models.Comment).filter(models.Comment.post_id == post_id).all()
        return jsonify(result)
    def post(self, post_id):
        pass