from flask import Blueprint, render_template, request, redirect
from app.models import Users
from app.database import get_db

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    db = next(get_db())
    users = db.query(Users).all()
    return render_template("index.html", users=users)
