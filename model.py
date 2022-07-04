from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

db = SQLAlchemy()


def setup_db(app):
    global db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'
    db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    emailverified = db.Column(db.Boolean(), nullable=False)
    firstname = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)


class UserRole(db.Model):
    user_id = db.Column(db.Integer())
    role_id = db.Column(db.Integer())


class UserPermission(db.Model):
    user_id = db.Column(db.Integer())


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)


class RolePermission(db.Model):
    role_id = db.Column(db.Integer())
    resource_id = db.Column(db.Integer())


class Permission(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)


class Resource(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(), unique=True, nullable=False)
