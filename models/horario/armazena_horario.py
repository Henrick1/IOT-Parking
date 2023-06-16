from models import db, Horario, Device
from datetime import datetime

class Armazena(db.Model):
    __tablename__ = 'armazena_horarios'
    id = db.Column('id', db.Integer(), primary_key=True)
    id_horario = db.Column("id_horario", db.Integer(), db.ForeignKey(Horario.id))
    id_device = db.Column("id_device", db.Integer(), db.ForeignKey(Device.id))