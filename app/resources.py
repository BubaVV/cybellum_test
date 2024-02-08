from db import models
from flask import abort, current_app, jsonify, request
from flask_bcrypt import Bcrypt
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from globs import app
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
engine = create_engine(models.db_uri)
Session = sessionmaker(bind=engine) 
session = Session()

admin = models.User(id=1, username='admin', email='admin@example.com')
session.merge(admin)
session.commit()

with app.app_context():
    bcrypt = Bcrypt(current_app)

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
    def post(self):
        json_data = request.get_json(force=True)
        username = json_data.get('username', '')
        password = json_data.get('password', '')
        email = json_data.get('email', '')
        user = models.User(username=username,
                           email=email,
                           password_hash=bcrypt.generate_password_hash(password.encode('utf-8')))
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            abort(400, 'Wrong data')
            session.rollback()
        return jsonify({'id': user.id})

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
    def post(self):
        json_data = request.get_json(force=True)
        title = json_data.get('title', '')
        content = json_data.get('content', '')
        author_id = json_data.get('author_id', 1)
        post = models.Post(title=title, content=content, author_id=author_id)
        session.add(post)
        try:
            session.commit()
        except IntegrityError:
            abort(400, 'Wrong data')
            session.rollback()
        return jsonify({'id': post.id})

class Comment(Resource):
    def get(self, post_id):
        result = session.query(models.Comment).filter(models.Comment.post_id == post_id).all()
        return jsonify(result)
    def post(self, post_id):
        json_data = request.get_json(force=True)
        content = json_data.get('content', '')
        author_id = json_data.get('author_id', 1)
        comment = models.Comment(content=content, author_id=author_id, post_id=post_id)
        session.add(comment)
        try:
            session.commit()
        except IntegrityError:
            abort(400, 'Wrong data')
            session.rollback()
        return jsonify({'id': comment.id})