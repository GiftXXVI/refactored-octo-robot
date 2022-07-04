from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def setup_db(app):
    global db
    global migrate
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    return db, migrate, app


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    emailverified = db.Column(db.Boolean(), nullable=False)
    firstname = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    roles = db.relationship('UserRole', backref=db.backref('users', lazy=True))
    permissions = db.relationship(
        'UserPermission', backref=db.backref('users', lazy=True))


class UserRole(db.Model):
    __tablename__ = "userroles"
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id'), primary_key=True)
    role_id = db.Column(db.Integer(), db.ForeignKey(
        'roles.id'), primary_key=True)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    role = db.relationship('UserRole', backref=db.backref('roles', lazy=True))


class UserPermission(db.Model):
    __tablename__ = "userpermissions"
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id'), primary_key=True)
    permission_id = db.Column(db.Integer(), db.ForeignKey(
        'permissions.id'), primary_key=True)


class RolePermission(db.Model):
    __tablename__ = "rolepermissions"
    role_id = db.Column(db.Integer(), db.ForeignKey(
        'roles.id'), primary_key=True)
    permission_id = db.Column(db.Integer(), db.ForeignKey(
        'permissions.id'), primary_key=True)


class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    users = db.relationship(
        'UserPermission', backref=db.backref('permissions', lazy=True))
    roles = db.relationship(
        'RolePermission', backref=db.backref('permissions', lazy=True))
    resources = db.relationship(
        'ResourcePermission', backref=db.backref('permissions', lazy=True))


class ResourcePermission(db.Model):
    __tablename__ = "resourcepermissions"
    permission_id = db.Column(db.Integer(), db.ForeignKey(
        'permissions.id'), primary_key=True)
    resource_id = db.Column(db.Integer(), db.ForeignKey(
        'resources.id'), primary_key=True)


class Resource(db.Model):
    __tablename__ = "resources"
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(), unique=True, nullable=False)
    permissions = db.relationship(
        'ResourcePermission', backref=db.backref('resources', lazy=True))
