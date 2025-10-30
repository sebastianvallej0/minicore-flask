from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instancia global de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Inicializa la BD
    db.init_app(app)

    # Registra blueprints (centralizado en app/routes/__init__.py)
    from .routes import register_blueprints
    register_blueprints(app)

    # Importa modelos y crea tablas dentro del contexto de la app
    with app.app_context():
        from . import models  # Vendedor, Venta, ReglaComision
        db.create_all()

    # Ruta raíz (prueba de vida)
    @app.get("/")
    def index():
        return "MiniCore Flask MVC ✅"

    return app
