from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456789'  # Adicione esta linha com uma chave secreta forte
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    csrf = CSRFProtect(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

