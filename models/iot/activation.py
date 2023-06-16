from models import db, Actuator
from datetime import datetime

class Activation(db.Model):
    __tablename__ = "activations"
    id = db.Column("id", db.Integer(), primary_key=True)
    actuator_id = db.Column("actuator_id", db.Integer(), db.ForeignKey(Actuator.id), nullable=False)
    date_time = db.Column("date_time", db.DateTime(), nullable=False, default=datetime.now())