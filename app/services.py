from .models import db, Venta, ReglaComision
from sqlalchemy import func

def calcular_comision_por_vendedor(vendedor_id, fecha_desde=None, fecha_hasta=None):
    q = db.session.query(Venta.categoria, func.sum(Venta.monto).label("monto"))\
                  .filter(Venta.vendedor_id == vendedor_id)
    if fecha_desde: q = q.filter(Venta.fecha >= fecha_desde)
    if fecha_hasta: q = q.filter(Venta.fecha <= fecha_hasta)
    q = q.group_by(Venta.categoria).all()

    total = 0.0
    detalle = []
    reglas = {r.categoria: float(r.porcentaje) for r in ReglaComision.query.all()}
    for categoria, monto in q:
        pct = reglas.get(categoria, 0.0) / 100.0
        com = float(monto) * pct
        detalle.append({"categoria": categoria, "monto": float(monto), "porcentaje": pct*100, "comision": com})
        total += com
    return {"total": total, "detalle": detalle}
