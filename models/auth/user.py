from turtle import back
from flask_login import UserMixin
from models import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    cpf = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    contato = db.Column(db.String(30), nullable=False, unique=True)
    sexo = db.Column(db.String(20), nullable=False)
    idade = db.Column(db.Integer(), nullable=False)
    password = db.Column(db.String(1024), nullable=False)

    roles = db.Relationship("Role", back_populates="users", secondary="user_roles")
    #reads = db.Relationship("Read", backref="users", lazy=True)
    #actvations = db.Relationship("Activation", backref="users", lazy=True)