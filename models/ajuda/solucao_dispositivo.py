from models import db, Device, Solucao

class SolucaoDevice(db.Model):
    __tablename__ = 'solucao_device'
    id_device = db.Column("id_device", db.Integer(), db.ForeignKey(Device.id), primary_key=True)
    id_solucao = db.Column("id_solucao", db.Integer(), db.ForeignKey(Solucao.id), primary_key=True)