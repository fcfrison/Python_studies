'''
In this module we have the ORM classes that defines the tables.
'''
from sqlalchemy import Column, Integer, Numeric, String, Identity
from sqlalchemy import ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship, backref # these methods are related to the creation of relationships

Base = declarative_base() # All classes inherit from the declarative base

class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(Integer(), Identity(start=1), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer(), Identity(start=1), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer(), Identity(start=1), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    shipped = Column(Boolean(), default=False)
    user = relationship("User", 
            backref=backref('orders', order_by=order_id))