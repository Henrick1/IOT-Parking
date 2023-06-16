from models import *
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def generate_seeds(db:SQLAlchemy):

    # A empresa
    empresa = Empresa(nome = "ANATEL", cnpj = "1234567891011")

    db.session.add_all([empresa])
    db.session.commit()

    # O estacionamento
    estacionamento = Estacionamento(description = " Estacionamento UrbanPark", id_estacionamento = empresa.id)

    db.session.add_all([estacionamento])
    db.session.commit()

    # As roles que um úsuario pode ter
    role1 = Role(nome = "Admin", descricao = "Admin capaz de acessar a maioria das páginas")
    role2 = Role(nome = "Funcionario", descricao = "Funcionario capaz de acessar certas páginas")

    db.session.add_all([role1,role2])
    db.session.commit()

    # Alguns usuarios
    u1 = User(name = "Roberto Junior", username = "Roberto", cpf = "11567812689", email = "Roberto@gmail.com", contato = "41 997287165", sexo = "Masculino", idade = "35", password = generate_password_hash("Senha"))
    u1.roles = [role1]
    u2 = User(name = "Ferb", username = "ferb", cpf = "12345678912", email = "ferb@gmail.com", contato = "41 997287185", sexo = "Masculino", idade = "12", password = generate_password_hash("senha"))
    u2.roles = [role1]

    db.session.add_all([u1, u2])
    db.session.commit()

    # IOT
    
    device1 = Device(brand = "ESP32", model = "ESP32", name = "Sensor de aproximação", voltage = 5, description = "Sensor de aproximação com medida em cm")
    device2 = Device(brand = "ESP32", model = "ESP32", name = "Sensor de aproximação 2", voltage = 5, description = "Sensor de aproximação com medida em cm")
    device3 = Device(brand = "ESP32", model = "ESP32", name = "Sensor de aproximação 3", voltage = 5, description = "Sensor de aproximação com medida em cm")
    device4 = Device(brand = "ESP32", model = "ESP32", name = "Sensor de aproximação 4", voltage = 5, description = "Sensor de aproximação com medida em cm")

    device5 = Device(brand = "ODM", model = "RED/GREEN LED", name = "LED 1", voltage = 5, description = "LED génerico para mostrar se vaga está ocupada")
    device6 = Device(brand = "ODM", model = "RED/GREEN LED", name = "LED 2", voltage = 5, description = "LED génerico para mostrar se vaga está ocupada")
    device7 = Device(brand = "ODM", model = "RED/GREEN LED", name = "LED 3", voltage = 5, description = "LED génerico para mostrar se vaga está ocupada")
    device8 = Device(brand = "ODM", model = "RED/GREEN LED", name = "LED 4", voltage = 5, description = "LED génerico para mostrar se vaga está ocupada")

    db.session.add_all([device1, device2, device3, device4, device5, device6, device7, device8])
    db.session.commit()

    sensor1 = Sensor(id = device1.id, measure = "cm")
    sensor2 = Sensor(id = device2.id, measure = "cm")
    sensor3 = Sensor(id = device3.id, measure = "cm")
    sensor4 = Sensor(id = device4.id, measure = "cm")

    db.session.add_all([sensor1, sensor2, sensor3, sensor4])
    db.session.commit()

    actuator1 = Actuator(id = device5.id, actuator_type = "Led")
    actuator2 = Actuator(id = device6.id, actuator_type = "Led")
    actuator3 = Actuator(id = device7.id, actuator_type = "Led")
    actuator4 = Actuator(id = device8.id, actuator_type = "Led")

    db.session.add_all([actuator1, actuator2, actuator3, actuator4])
    db.session.commit()
    
    # Algumas vagas
    v1 = Vaga(andar = 1, id_estacionamento = estacionamento.id, id_sensor = sensor1.id, id_actuator = actuator1.id)
    v2 = Vaga(andar = 2, id_estacionamento = estacionamento.id, id_sensor = sensor2.id, id_actuator = actuator2.id)
    v3 = Vaga(andar = 2, id_estacionamento = estacionamento.id, id_sensor = sensor3.id, id_actuator = actuator3.id)
    v4 = Vaga(andar = 3, id_estacionamento = estacionamento.id, id_sensor = sensor4.id, id_actuator = actuator4.id)

    db.session.add_all([v1, v2, v3, v4])
    db.session.commit()

    # Algumas chamadas de concerto
    c1 = Conserto(id_user = u1.id, numero_vaga = v1.id, descricao  = "Sensor não detecta presença", status = "Inconcluido")
    c2 = Conserto(id_user = u1.id, numero_vaga = v1.id, descricao  = "Sensor está quebrado", status = "Inconcluido")
    c3 = Conserto(id_user = u1.id, numero_vaga = v3.id, descricao  = "Sensor não recebe energia", status = "Inconcluido")

    db.session.add_all([c1, c2, c3])
    db.session.commit()
    

