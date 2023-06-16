from models import db, Sensor, User
from datetime import datetime

class Read(db.Model):
    __tablename__ = "reads"
    id = db.Column("id", db.Integer(), primary_key=True)
    user_id = db.Column("user_id", db.Integer(), db.ForeignKey(User.id))
    sensor_id = db.Column("sensor_id", db.Integer(), db.ForeignKey(Sensor.id), nullable=False)
    value = db.Column("value", db.Float(), nullable=False, default=0.0)
    date_time = db.Column("date_time", db.DateTime(), nullable=False, default=datetime.now())