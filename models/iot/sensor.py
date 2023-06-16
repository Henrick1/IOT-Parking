from models import db, Device

class Sensor(db.Model):
    __tablename__ = "sensors"
    id = db.Column("id", db.Integer, db.ForeignKey(Device.id), primary_key = True)
    measure = db.Column(db.String(20))

    reads = db.relationship("Read", backref="sensors", lazy=True)

    def get_sensors():
        sensors = Sensor.query.join(Device, Device.id == Sensor.id)\
                    .add_columns(Sensor.id, Device.name, Device.brand, Device.model, 
                                 Device.voltage, Device.description,  Device.is_active, Sensor.measure).all()
        
        return sensors
    
    def save_sensor(name, description, brand, model, voltage, is_active, measure):
        device = Device(name = name, description = description, brand=brand, 
                           model = model, voltage = voltage, is_active = is_active)
    
        sensor = Sensor(id = device.id, measure = measure)
        
        device.sensors.append(sensor)
        db.session.add(device)
        db.session.commit()

    def delete_sensor(id):
        try:
            Sensor.query.filter_by(id=id).delete()
            Device.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False

    def delete_sensor_by_measure(measure):
        Sensor.query.filter_by(measure=measure).delete()
        db.session.commit()

    def update_sensor(data):
        Device.query.filter_by(id=data['id'])\
                .update(dict(name = data['name'], brand=data['brand'], model = data['model'], 
                        voltage = data['voltage'], description = data['description'], 
                        is_active = data['is_active']))
        
        Sensor.query.filter_by(id=data['id'])\
                        .update(dict(measure = data['measure']))
        db.session.commit()