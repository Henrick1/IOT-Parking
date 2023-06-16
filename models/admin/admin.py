from models import db

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(512))

    admins = db.Relationship("Admin", back_populates="roles", secondary="user_roles")