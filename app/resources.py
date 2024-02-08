from db import models
from flask import abort, jsonify, request, session
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from globs import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
engine = create_engine(models.db_uri)
Session = sessionmaker(bind=engine)
db_session = Session()


class User(Resource):
    def get(self, id=None):
        if not id:
            if 'user_id' in session:
                id = session['user_id']
            else:
                abort(400, 'Log in or pass user id to fetch data')
        result = (
            db_session
            .query(models.User)
            .filter(models.User.id == id)
            .one_or_none()
        )
        if result:
            return jsonify(models.to_dict(result))
        else:
            abort(404, f"User id {id} doesn't exist.")

    def post(self):
        json_data = request.get_json(force=True)
        username = json_data.get('username', '')
        password = json_data.get('password', '')
        email = json_data.get('email', '')
        user = models.User(
            username=username,
            email=email,
            password_hash=bcrypt
            .generate_password_hash(password.encode('utf-8')),
        )
        db_session.add(user)
        try:
            db_session.commit()
        except IntegrityError:
            abort(400, 'Wrong data')
            db_session.rollback()
        return jsonify({'id': user.id})


class Post(Resource):
    def get(self, id=None):
        if id:
            result = (
                db_session
                .query(models.Post)
                .filter(models.Post.id == id)
                .one_or_none()
            )
            if result:
                return jsonify(result)
            else:
                abort(404, f"Post id {id} doesn't exist.")
        else:
            result = db_session.query(models.Post).all()
            return jsonify([models.to_dict(x) for x in result])

    def post(self):
        if 'user_id' in session:
            author_id = session['user_id']
        else:
            abort(403)
        json_data = request.get_json(force=True)
        title = json_data.get('title', '')
        content = json_data.get('content', '')
        post = models.Post(title=title, content=content, author_id=author_id)
        db_session.add(post)
        try:
            db_session.commit()
        except IntegrityError:
            abort(400, 'Wrong data')
            db_session.rollback()
        return jsonify({'id': post.id})


class Comment(Resource):
    def get(self, post_id):
        post = (
            db_session.query(models.Post)
            .filter(models.Post.id == post_id)
            .one_or_none()
        )
        if not post:
            abort(404, f'Post {post_id} does not exist')
        result = (
            db_session.query(models.Comment)
            .filter(models.Comment.post_id == post_id)
            .all()
        )
        return jsonify([models.to_dict(x) for x in result])

    def post(self, post_id):
        if 'user_id' in session:
            author_id = session['user_id']
        else:
            abort(403)
        json_data = request.get_json(force=True)
        content = json_data.get('content', '')
        if not author_id:
            abort(403)
        comment = models.Comment(content=content,
                                 author_id=author_id,
                                 post_id=post_id)
        db_session.add(comment)
        try:
            db_session.commit()
        except IntegrityError:
            abort(400, 'Wrong data')
            db_session.rollback()
        return jsonify({'id': comment.id})


class Login(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        username = json_data.get('username', '')
        password = json_data.get('password', '')

        user = (
            db_session.query(models.User)
            .filter(models.User.username == username)
            .one_or_none()
        )
        if user and user.authenticate(password):
            session['user_id'] = user.id
            return jsonify(f"User {user.id} logged in")
        else:
            return {'error': 'Logging error'}, 403

    def delete(self):
        if 'user_id' in session:
            session['user_id'] = None
            return {}, 204
        else:
            return {'error': 'Logout error'}, 401
