from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from app import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(60))
    street = db.Column(db.String(100))
    city = db.Column(db.String(100))
    zipcode = db.Column(db.String(100))