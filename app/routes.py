from flask import Blueprint, render_template, request, redirect
from app.models import Users
from app.database import get_db

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    db = next(get_db())
    users = db.query(Users).all()
    return render_template("index.html", users=users)

@bp.route("/criar_usuario", methods=["POST"])
def criar_usuario():
    db = next(get_db())
    nickname = request.form["nickname"]
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]

    if db.query(Users).filter_by(email=email).first():
        return "E-mail já existe", 400

    novo = Users(nickname=nickname, nome=nome, email=email, senha=senha)
    db.add(novo)
    db.commit()
    return redirect("/")