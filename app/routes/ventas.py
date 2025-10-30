from flask import Blueprint, render_template, request, redirect, url_for
from ..models import db, Venta, Vendedor
from datetime import date

bp = Blueprint("ventas", __name__, url_prefix="/ventas")  # <--- ESTA VARIABLE DEBE LLAMARSE bp

@bp.get("/")
def listar():
    ventas = Venta.query.order_by(Venta.fecha.desc()).all()
    vendedores = Vendedor.query.all()
    return render_template("ventas_list.html", ventas=ventas, vendedores=vendedores)

@bp.post("/crear")
def crear():
    vendedor_id = int(request.form["vendedor_id"])
    fecha = request.form.get("fecha") or date.today().isoformat()
    monto = request.form["monto"]
    categoria = request.form["categoria"]
    v = Venta(vendedor_id=vendedor_id, fecha=fecha, monto=monto, categoria=categoria)
    db.session.add(v)
    db.session.commit()
    return redirect(url_for("ventas.listar"))
