from flask import Blueprint, render_template, request, redirect, url_for
from ..models import db, Vendedor

bp = Blueprint("vendedores", __name__, url_prefix="/vendedores")

@bp.get("/")
def listar():
    vendedores = Vendedor.query.all()
    return render_template("vendedores_list.html", vendedores=vendedores)

@bp.post("/crear")
def crear():
    nombre = request.form["nombre"]
    email = request.form["email"]
    v = Vendedor(nombre=nombre, email=email)
    db.session.add(v)
    db.session.commit()
    return redirect(url_for("vendedores.listar"))
