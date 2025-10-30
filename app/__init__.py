from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Instancia global de SQLAlchemy (se inicializa dentro de create_app)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")  # Carga configuración (DB URI, SECRET_KEY, etc.)

    # Inicializa la BD con la app
    db.init_app(app)

    # Registra blueprints centralizados en app/routes/__init__.py
    from .routes import register_blueprints
    register_blueprints(app)

    # Importa modelos y crea tablas dentro del contexto de la app
    with app.app_context():
        from . import models  # Vendedor, Venta, ReglaComision
        db.create_all()

    # ---------- Rutas simples ----------
    @app.get("/")
    def index():
        # Renderiza la vista de inicio (con navbar y accesos a Vendedores/Ventas/Comisiones)
        return render_template("index.html", active=None)

    return app
