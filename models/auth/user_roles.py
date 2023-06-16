from models import db, User, Role

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id_user = db.Column("id_user", db.Integer(), db.ForeignKey(User.id), primary_key=True)
    id_role = db.Column("id_role", db.Integer(), db.ForeignKey(Role.id), primary_key=True)