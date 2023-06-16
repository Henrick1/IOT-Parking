from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#instance = 'sqlite:///restaurant'
instance = "mysql+pymysql://estacionamento:estacione@localhost:3306/estacionamento"