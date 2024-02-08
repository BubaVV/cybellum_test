import os
from datetime import datetime

from globs import Base, bcrypt, db_uri
from sqlalchemy import (Column, DateTime, ForeignKey, Integer, LargeBinary,
                        String, create_engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(LargeBinary)
    created_at = Column(DateTime, default=datetime.utcnow())

    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password_hash, password.encode('utf-8'))


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())


engine = create_engine(db_uri)
Base.metadata.create_all(engine)
