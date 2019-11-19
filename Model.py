from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class Ipath(db.Model):
    __tablename__ = 'ipath_namelist'
    nickname = db.Column(db.String(4), primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    calories = db.Column(db.Integer, server_default='0')
    record = db.Column(db.Integer, server_default='100')
    points = db.Column(db.Integer, server_default='0')

    def __init__(self, nickname, name, calories, record, points):
        self.nickname = nickname
        self.name = name
        self.calories = calories
        self.record = record
        self.points = points

class IpathSchema(ma.Schema):
    id = fields.Integer()
    nickname = fields.String(required=True)
    name = fields.String(required=True)
    calories = fields.Integer(required=True)
    record = fields.Integer(required=True)
    points = fields.Integer(required=True)