from models import db, User

class Reclamacao(db.Model):
    __tablename__ = 'reclamacoes'
    id = db.Column('id', db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey(User.id, ondelete='CASCADE'))
    titulo = db.Column(db.String(20))
    descricao = db.Column(db.String(512))

    def delete_reclamacao(id):
        try:
            Reclamacao.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
