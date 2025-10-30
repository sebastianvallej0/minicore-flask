from flask import Blueprint, request, render_template
from ..services import calcular_comision_por_vendedor

bp = Blueprint("comisiones", __name__, url_prefix="/comisiones")

@bp.get("/")
def ver_comisiones():
    vendedor_id = request.args.get("vendedor_id", type=int)
    desde = request.args.get("desde")
    hasta = request.args.get("hasta")
    data = calcular_comision_por_vendedor(vendedor_id, desde, hasta) if vendedor_id else None
    return render_template("comisiones.html", data=data)
