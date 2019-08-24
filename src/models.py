import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type_of_post = Column(String(250))
    likes = Column(String(250))
    comments = Column(String(250), nullable=False)


class DM(Base):
    __tablename__ = 'DM'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    messages = Column(String(250))
    user2_id = Column(Integer, ForeignKey('user2_id.id'))

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(String(250))
    following_id = Column(String(250))

class Stories(Base):
    __tablename__ = 'stories'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type_of_story = Column(String(250))
    views = Column(String(250))



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)



    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')