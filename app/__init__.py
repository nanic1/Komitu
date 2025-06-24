from flask import Flask
from app.database import start_db
from app.routes import bp

def create_app():
    app = Flask(__name__)
    start_db()

    
    app.register_blueprint(bp)

    return app