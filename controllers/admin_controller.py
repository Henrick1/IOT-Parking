from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.auth.user import User
from models import db, Vaga, Device, Horario

admin = Blueprint("admin", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@admin.route("/")
@login_required
def admin_index():
    return render_template("/admin/admin_home.html")

@admin.route("/ver_vagas")
@login_required
def ver_vagas():
    vagas = Vaga.query.all()
    return render_template("/admin/admin_vagas.html", vagas = vagas)

@admin.route("/ver_horarios")
@login_required
def ver_horarios():
    horario = Horario.query.all()
    return render_template("/admin/admin_horario.html", horario= horario)
