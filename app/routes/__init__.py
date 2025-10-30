from .vendedores import bp as vendedores_bp
from .ventas import bp as ventas_bp
from .comisiones import bp as comisiones_bp

def register_blueprints(app):
    app.register_blueprint(vendedores_bp)
    app.register_blueprint(ventas_bp)
    app.register_blueprint(comisiones_bp)
