from flask import Flask, render_template, session, g
from flask_mqtt import Mqtt
from models.auth.user import User
from controllers.admin_controller import admin
from controllers.ajuda_controller import ajuda
from controllers.auth_controller import auth
from controllers.iot_controller import iot
from flask_login import LoginManager, logout_user
from models.db import db, instance
from models import Read, Vaga, Device, Sensor, Horario, Armazena, Actuator, Activation
from datetime import datetime
from models.mqtt import mqtt_client, topic_subscribe

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", 
                        static_folder="./static/", 
                        root_path="./")
    
    app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''
    app.config['MQTT_PASSWORD'] = ''
    app.config['MQTT_KEEPALIVE'] = 5
    app.config['MQTT_TLS_ENABLED'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)
    
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(ajuda, url_prefix='/ajuda')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(iot, url_prefix='/iot')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        logout_user()
        return render_template("NHome.html")
    
    # Parte MQTT

    mqtt = Mqtt(app)  
    
    @mqtt.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            for topic in topic_subscribe:
                mqtt.subscribe(topic)
        else:
            print('Bad connection. Code:', rc)


    @mqtt.on_message()
    def handle_mqtt_message(client, userdata, message):
        data = dict(
            topic=message.topic,
            payload=message.payload.decode()
        )
        idVaga = 0
        if message.topic == "estacionamento/enviar1":
            print("Enviar 1")
            idVaga = 1
        elif message.topic == "estacionamento/enviar2":
            print("Enviar 2")
            idVaga = 2
        elif message.topic == "estacionamento/enviar3":
            print("Enviar 3")
            idVaga = 3
        elif message.topic == "estacionamento/enviar4":
            print("Enviar 4")
            idVaga = 4
        with app.app_context():
            vaga = db.session.query(Vaga).filter(Vaga.id == int(idVaga)).first()
            vaga.ocupado = eval(message.payload.decode())
            db.session.commit()

            # Agora mostrar que o sensor está ligado
            sensor = db.session.query(Device, Sensor)\
                        .join(Sensor, Sensor.id == Device.id)\
                        .filter(Sensor.id == int(idVaga)).first()
            
            device, sensor = sensor  # Separar o Device e o Sensor da tupla

            device.is_active = eval(message.payload.decode())
            db.session.commit()

            # Mesma coisa para o atuador
            # Ativar o atuador
            actuator = db.session.query(Device, Actuator)\
                        .join(Actuator, Actuator.id == Device.id)\
                        .filter(Actuator.id == int(idVaga + 4)).first()
            
            devices, actuator = actuator

            devices.is_active = eval(message.payload.decode())
            db.session.commit()

            # Pegamos a ativação
            activations = Activation(actuator_id = devices.id, date_time = datetime.now())
            db.session.add(activations)
            db.session.commit()

            # Pegamos o horario para a entrada e saida
            horario = Horario.query.filter_by(vaga_id=vaga.id, saida=None).first()
            if not device.is_active:
                if horario:
                    horario.saida = datetime.now()
                    db.session.commit()
            else:
                if not horario:
                    horario = Horario(entrada=datetime.now(), vaga_id=vaga.id)
                    db.session.add(horario)
                    db.session.commit()

            # Para armazenar os horarios
            armazenar_horarios = Armazena(id_horario = horario.id, id_device = device.id)
            db.session.add(armazenar_horarios)
            db.session.commit()

        # Link do wokwi:https://wokwi.com/projects/367261406236811265, https://wokwi.com/projects/367534832904395777
        print("Received message on topic: {0} with payload: {1}".format(message.topic, message.payload.decode()))

    
    return app