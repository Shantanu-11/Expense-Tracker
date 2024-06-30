from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(100), unique=True)

class Expense(Base):
    __tablename__ = "expense"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    amount = Column(Float)
    detail = Column(String(100))
    mode = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey('users.id'))
    user_id = Column(Integer, ForeignKey('users.id'))


class Category(Base):
    __tablename__ = "category"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Token(Base):
    __tablename__ = "usertoken"

    id = Column(Integer, primary_key=True)
    token = Column(String)
    expiry = Column(DateTime)

class OTP(Base):
    __tablename__ = "otp"

    id = Column(Integer, primary_key=True)
    user_email = Column(String(50))
    otp = Column(Integer)
    expiry = Column(DateTime)