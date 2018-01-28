import datetime

from flask_login import UserMixin

from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class Post(Base):
    __tablename__  = 'post'
    id             = Column(Integer, primary_key=True)
    title = Column(String)
    img = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return "<Post: %s, title: %s" % (
            self.id, self.title)


