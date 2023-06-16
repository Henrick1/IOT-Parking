from models import db, Vaga
from datetime import datetime

class Horario(db.Model):
    __tablename__ = 'horarios'
    id = db.Column('id', db.Integer(), primary_key=True)
    entrada = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    saida = db.Column(db.DateTime())
    vaga_id = db.Column("vaga_id", db.Integer(), db.ForeignKey(Vaga.id), nullable=False)
