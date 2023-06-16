from models import db, User

class Empresa(db.Model):
    __tablename__ = 'empresas'
    id = db.Column('id', db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey(User.id, ondelete='CASCADE'))
    nome = db.Column(db.String(50), nullable=False, unique=True)
    cnpj = db.Column(db.String(15), nullable=False, unique=True)
