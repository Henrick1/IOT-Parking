from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.auth.user import User
from models.db import db

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@auth.route("/")
@auth.route("/login")
def login():
    logout_user()
    return render_template("auth/Login.html")

@auth.route("/cadastrar")
def cadastrar():
    logout_user()
    return render_template("auth/Cadastro.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Coisas para cadastro

@auth.route("/lista_funcionario")
def funcionario_index():
    saved_funcionario = User.query.all()
    return render_template("auth/ListaFuncionario.html", funcionarios = saved_funcionario)

@auth.route("/save_funcionario", methods=["POST","GET"])
def save_funcionario():
    if request.method == "POST":
        nome_funcionario = request.form["nome_funcionario"]
        usuario_funcionario = request.form["usuario_funcionario"]
        email_funcionario = request.form["email_funcionario"]
        contato_funcionario = request.form["contato_funcionario"]
        cpf_funcionario = request.form["cpf_funcionario"]
        sexo_funcionario = request.form["sexo_funcionario"]
        idade_funcionario = request.form["idade_funcionario"]
        senha_funcionario = request.form["senha_funcionario"]

    
    # Coisas para a autenticação
    user = User.query.filter_by(email=email_funcionario).first()

    if user:
        # Mostrar o Flask
        flash('Esse E-mail ou Usuario já existe!')
        return redirect(url_for('auth.cadastrar'))
    
    if not idade_funcionario.isdigit():
            flash('Por favor, insira um número válido para a idade.')
            return redirect(url_for('auth.cadastrar'))
    
    new_user = User(name=nome_funcionario, username=usuario_funcionario, cpf = cpf_funcionario, email=email_funcionario, contato=contato_funcionario, sexo=sexo_funcionario,idade=idade_funcionario,password=generate_password_hash(senha_funcionario, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))

# Coisas para login

@auth.route("/loginaceito")
def loginaceito():
    
    return redirect(url_for("auth.funcionario_index"))

@auth.route("/login_salvo", methods=["POST"])
def login_salvo():
    usuario = request.form.get("usuario")
    senha = request.form.get("password")
    remember = True if request.form.get('remember') else False

    user = User.query.filter((User.username==usuario) | (User.email==usuario)).first()

    if not user or not check_password_hash(user.password, senha):
        flash('Usuário ou Senha incorretos!')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)
    return redirect(url_for("auth.loginaceito"))

# Coisas para a autenticação

