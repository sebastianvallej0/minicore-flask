from datetime import datetime, date
from decimal import Decimal, InvalidOperation

from flask import Blueprint, render_template, request, redirect, url_for, abort
from .. import db
from ..models import Vendedor, Venta

# Blueprint de Ventas
bp = Blueprint("ventas", __name__, url_prefix="/ventas")


@bp.get("/")
def listar():
    """Lista de ventas + formulario de registro."""
    ventas = Venta.query.order_by(Venta.fecha.desc()).all()
    vendedores = Vendedor.query.order_by(Vendedor.nombre.asc()).all()
    return render_template(
        "ventas_list.html",
        ventas=ventas,
        vendedores=vendedores,
        active="ventas",  # para marcar el menú activo
    )


@bp.post("/crear")
def crear():
    """Crea una venta a partir del formulario."""
    # --- vendedor ---
    try:
        vendedor_id = int(request.form["vendedor_id"])
    except (KeyError, ValueError):
        abort(400, description="vendedor_id inválido")

    # Valida que exista (opcional, pero útil)
    if not Vendedor.query.get(vendedor_id):
        abort(400, description="Vendedor no existe")

    # --- fecha ---
    fecha_str = (request.form.get("fecha") or "").strip()
    if fecha_str:
        # input type="date" -> 'YYYY-MM-DD'
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            abort(400, description="Fecha inválida. Formato esperado YYYY-MM-DD.")
    else:
        fecha = date.today()

    # --- monto ---
    monto_str = (request.form.get("monto") or "0").strip().replace(",", ".")
    try:
        monto = Decimal(monto_str)
    except InvalidOperation:
        abort(400, description="Monto inválido.")

    # --- categoría ---
    categoria = (request.form.get("categoria") or "").strip()
    if not categoria:
        abort(400, description="La categoría es obligatoria.")

    # Crear y guardar
    venta = Venta(
        vendedor_id=vendedor_id,
        fecha=fecha,          # <- datetime.date (no string)
        monto=monto,          # <- Decimal compatible con Numeric
        categoria=categoria,
    )
    db.session.add(venta)
    db.session.commit()

    return redirect(url_for("ventas.listar"))
