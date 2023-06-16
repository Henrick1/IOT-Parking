from models import db

class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(256), nullable = False)
    brand = db.Column(db.String(50), nullable = True)
    model = db.Column(db.String(50), nullable = True)
    voltage = db.Column(db.Float())
    is_active = db.Column(db.Boolean(), nullable = False, default = False)

    sensors = db.relationship("Sensor", backref = "devices", lazy = True)
    actuators = db.relationship("Actuator", backref="actuators", lazy=True)