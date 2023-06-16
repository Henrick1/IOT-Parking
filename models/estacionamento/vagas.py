from models import db, Estacionamento, Sensor, Actuator
class Vaga(db.Model):
    __tablename__ = 'vagas'
    id = db.Column('id', db.Integer(), primary_key=True)
    andar = db.Column(db.Integer(), nullable=False)
    ocupado = db.Column(db.Boolean(), default=False)
    id_sensor = db.Column(db.Integer(), db.ForeignKey(Sensor.id, ondelete='CASCADE'))
    id_actuator = db.Column(db.Integer(), db.ForeignKey(Actuator.id, ondelete='CASCADE'))
    id_estacionamento = db.Column(db.Integer(), db.ForeignKey(Estacionamento.id, ondelete='CASCADE'))

    horarios = db.relationship('Horario', backref='vaga')