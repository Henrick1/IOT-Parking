from models import db, Vaga, Conserto
from datetime import datetime

class Solucao(db.Model):
    __tablename__ = 'solucoes'
    id = db.Column('id', db.Integer(), primary_key=True)
    id_conserto = db.Column(db.Integer(), db.ForeignKey(Conserto.id, ondelete='CASCADE'))
    numero_vaga = db.Column(db.Integer(), db.ForeignKey(Vaga.id, ondelete='CASCADE'))
    data_hora = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    descricao = db.Column(db.String(512))
    status = db.Column(db.String(20), default="Solucionada")

    vagas = db.relationship("Vaga", backref="solucoes", lazy=True)