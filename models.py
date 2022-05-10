from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()


class City_model(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    population = db.Column(db.Integer())

    def __init__(self, id, name, population):
        self.id = id
        self.name = name
        self.population = population


class Judge_model(db.Model):
    __tablename__ = 'judge'

    id = db.Column(db.Integer(), primary_key=True)
    fio = db.Column(db.String())
    city_id = db.Column(db.Integer())

    def __int__(self, id, fio, city_id):
        self.id = id
        self.fio = fio
        self.city_id = city_id


class Team_model(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    city_id = db.Column(db.Integer())
    line_up = db.Column(db.String())

    def __int__(self, id, name, city_id, line_up):
        self.id = id
        self.name = name
        self.city_id = city_id
        self.line_up = line_up


class Game_model(db.Model):
    __tablename__ = 'game'

    id = db.Column(db.Integer(), primary_key=True)
    team_owner_id = db.Column(db.Integer())
    team_guest_id = db.Column(db.Integer())
    city_id = db.Column(db.Integer())
    judge_id = db.Column(db.Integer())
    time = db.Column(db.String())
    date = db.Column(db.String())

    def __int__(self, id, team_owner_id, team_guest_id, city_id, judge_id, time, date):
        self.id = id
        self.team_owner_id = team_owner_id
        self.team_guest_id = self.team_guest_id
        self.city_id = city_id
        self.judge_id = judge_id
        self.time = time
        self.date = date


class User_model(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String())
    password = db.Column(db.String())


class Judge_schema(Schema):
    id = fields.Int(data_key='id')
    fio = fields.Str(data_key='fio')
    city_id = fields.Int(data_key='city_id')


class City_schema(Schema):
    id = fields.Integer()
    name = fields.Str(data_key='name')
    population = fields.Int(data_key='population')


class Team_schema(Schema):
    id = fields.Int(data_key='id')
    name = fields.Str(data_key='name')
    line_up = fields.Str(data_key='line_up')
    city_id = fields.Int(data_key='city_id')


class Game_schema(Schema):
    id = fields.Int(data_key='id')
    city_id = fields.Int(data_key='city_id')
    judge_id = fields.Int(data_key='judge_id')
    team_owner_id = fields.Int(data_key='team_owner_id')
    team_guest_id = fields.Int(data_key='team_guest_id')
    time = fields.Str(data_key='time')
    date = fields.Str(data_key='date')


class User_schema(Schema):
    id = fields.Int(data_key='id')
    login = fields.Str(data_key='login')
    password = fields.Str(data_key='password')
