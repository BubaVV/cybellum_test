from datetime import datetime
import os
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, create_engine


from sqlalchemy.ext.declarative import declarative_base

db_name = os.environ['PG_DB']
db_user = os.environ['PG_USER']
db_pass = os.environ['PG_PASS']
db_uri = f'postgresql://{db_user}:{db_pass}@cybellum_db:5432/{db_name}'
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

engine = create_engine(db_uri)
Base.metadata.create_all(engine)