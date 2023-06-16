from models import db, Empresa

class Estacionamento(db.Model):
    __tablename__ = 'estacionamentos'
    id = db.Column('id', db.Integer(), primary_key=True)
    description = db.Column(db.String(512))
    id_estacionamento = db.Column(db.Integer(), db.ForeignKey(Empresa.id, ondelete='CASCADE'))