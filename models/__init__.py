from models.db import db, instance
from models.auth.user import User
from models.auth.role import Role
from models.empresa.empresa import Empresa
from models.estacionamento.estacionamento import Estacionamento
from models.auth.user_roles import UserRoles
from models.iot.device import Device
from models.iot.sensor import Sensor
from models.iot.actuator import Actuator
from models.iot.activation import Activation
from models.iot.read import Read
from models.estacionamento.vagas import Vaga
from models.ajuda.conserto import Conserto
from models.ajuda.solucao import Solucao
from models.ajuda.reclamacao import Reclamacao
from models.horario.horario import Horario
from models.horario.armazena_horario import Armazena
from models.ajuda.solucao_dispositivo import SolucaoDevice
