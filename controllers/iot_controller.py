from re import template
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template,redirect,url_for,request, flash
from models import Horario, Sensor, Device, Actuator, db, Vaga

iot = Blueprint("iot", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@iot.route("/")
@login_required
def iot_index():
    return render_template("/iot/Iot.html")

@iot.route("/register_sensor")
@login_required
def register_sensor():
    return render_template("/iot/register_sensor.html")

@iot.route("/register_actuator")
@login_required
def register_actuator():
    return render_template("/iot/register_actuator.html")

@iot.route("/view_sensors")
@login_required
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors = sensors)

@iot.route("/view_actuators")
@login_required
def view_actuators():
    actuators = Actuator.get_actuators()
    return render_template("iot/view_actuators.html", actuators = actuators)

#--------------------------#
# SENSOR
@iot.route("/save_sensors", methods = ["POST"])
def save_sensors():
    name = request.form.get("name")
    description = request.form.get("description")
    brand = request.form.get("brand")
    model = request.form.get("model")
    voltage = request.form.get("voltage")
    measure = request.form.get("measure")
    is_active = True if request.form.get("is_active") == "on" else False

    if not voltage.isdigit():
            flash('Por favor, insira um número válido para a Tensão')
            return redirect(url_for('iot.register_sensor'))

    Sensor.save_sensor(name, description, brand, model, voltage, is_active, measure)

    return redirect(url_for('iot.view_sensors'))

@iot.route("/update_sensor/<id>")
def update_sensor(id):
    sensor = db.session.query(Device, Sensor)\
                        .join(Sensor, Sensor.id == Device.id)\
                        .filter(Sensor.id == int(id)).first()
    
    return render_template("/iot/update_sensor.html", sensor = sensor)

@iot.route("/save_sensor_changes", methods = ["POST"])
def save_sensor_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"

    voltage = data.get("voltage")
    if not voltage.replace(".", "").isdigit():
        flash('Por favor, insira um número válido para a Tensão')
        return redirect(url_for('iot.view_sensors'))
    
    Sensor.update_sensor(data)
    return redirect(url_for("iot.view_sensors"))

@iot.route("/delete_sensor/<id>")
def delete_sensor(id):
    if Sensor.delete_sensor(id):
        flash("Dispositivo Sensor Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Sensor não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("iot.view_sensors"))
#--------------------------#
# ATUADOR

@iot.route("/save_actuators", methods = ["POST"])
def save_actuators():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    actuator_type = request.form.get("actuator_type")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    if not voltage.isdigit():
            flash('Por favor, insira um número válido para a Tensão')
            return redirect(url_for('iot.register_actuator'))

    Actuator.save_actuators(name, brand, model, actuator_type, description, is_active, voltage)

    return redirect(url_for("iot.view_actuators"))

@iot.route("/update_actuator/<id>")
def update_actuator(id):
    actuator = db.session.query(Device, Actuator)\
                        .join(Actuator, Actuator.id == Device.id)\
                        .filter(Actuator.id == int(id)).first()
    
    return render_template("/iot/update_actuator.html", actuator = actuator)

@iot.route("/save_actuator_changes", methods = ["POST"])
def save_actuator_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"

    voltage = data.get("voltage")
    if not voltage.replace(".", "").isdigit():
        flash('Por favor, insira um número válido para a Tensão')
        return redirect(url_for('iot.view_actuators'))
    
    Actuator.update_actuator(data)
    return redirect(url_for("iot.view_actuators"))

@iot.route("/delete_actuator/<id>")
def delete_actuator(id):
    if Actuator.delete_actuator(id):
        flash("Dispositivo Atuador Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Atuador não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("iot.view_actuators"))
