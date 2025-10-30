from . import db
from sqlalchemy import Numeric, Date

class Vendedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True)
    ventas = db.relationship("Venta", backref="vendedor", lazy=True)

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendedor_id = db.Column(db.Integer, db.ForeignKey("vendedor.id"), nullable=False)
    fecha = db.Column(Date, nullable=False)
    monto = db.Column(Numeric(12, 2), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

class ReglaComision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), unique=True, nullable=False)
    porcentaje = db.Column(Numeric(5, 2), nullable=False)  # 5.00 = 5%
