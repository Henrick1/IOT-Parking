from models import db, Vaga, User

class Conserto(db.Model):
    __tablename__ = 'consertos'
    id = db.Column('id', db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey(User.id, ondelete='CASCADE'))
    numero_vaga = db.Column(db.Integer(), db.ForeignKey(Vaga.id, ondelete='CASCADE'))
    descricao = db.Column(db.String(512))
    status = db.Column(db.String(20), default="Inconcluido")

    vagas = db.relationship("Vaga", backref="consertos", lazy=True)

    def delete_conserto(id):
        try:
            Conserto.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
        
    def update_conserto(data):
        Conserto.query.filter_by(id=data['id'])\
                        .update(dict(numero_vaga = data['numero_vaga'], descricao = data['descricao']))
        db.session.commit()