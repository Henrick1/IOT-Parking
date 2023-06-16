from models import db, User

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column('id', db.Integer(), primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(512))

    users = db.Relationship("User", back_populates="roles", secondary="user_roles")