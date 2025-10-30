# MiniCore Flask MVC  
Aplicación web básica con Flask, SQLAlchemy y despliegue en Render.  

URL: https://minicore-flask-0jjr.onrender.com  

## ¿De qué trata?
Es un mini proyecto para practicar el patrón MVC con Flask:
- **Models:** SQLAlchemy (Vendedor, Venta, ReglaComisión)
- **Views:** Templates HTML sencillos
- **Controllers:** Blueprints (vendedores, ventas, comisiones)

## Cómo correrlo en local (resumen rápido)
1. Crear y activar venv  
2. `pip install -r requirements.txt`  
3. `python -m flask --app wsgi:app --debug run`  
4. Abrir `http://127.0.0.1:5000/`

## Rutas principales
- `/` → ping de vida  
- `/vendedores/` → lista y formulario  
- `/ventas/` → registro de ventas  
- `/comisiones/` → cálculo por vendedor y rango de fechas

## Despliegue
Se subió a **Render** usando `gunicorn` con:
- Procfile: `web: gunicorn wsgi:app`

## Créditos
Grupo 14 — Trabajo para la materia de Ingeniería Web.
