DROP DATABASE IF EXISTS estacionamento;
CREATE DATABASE estacionamento;

DROP USER IF EXISTS estacionamento;
CREATE USER estacionamento IDENTIFIED BY "estacione";
GRANT ALL ON *.* TO estacionamento WITH GRANT OPTION;
SELECT * FROM estacionamento;

SELECT * FROM estacionamento.users;
SELECT * FROM estacionamento.roles;
SELECT * FROM estacionamento.user_roles;

SELECT * FROM estacionamento.consertos;
SELECT * FROM estacionamento.vagas;
SELECT * FROM estacionamento.solucoes;
SELECT * FROM estacionamento.reclamacoes;

SELECT * FROM estacionamento.devices;
SELECT * FROM estacionamento.sensors;
SELECT * FROM estacionamento.actuators;
