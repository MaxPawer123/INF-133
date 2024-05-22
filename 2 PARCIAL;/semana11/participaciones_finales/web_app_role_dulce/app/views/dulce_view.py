from flask import render_template
from flask_login import current_user

def list_dulce(dulces):
    return render_template(
        "dulces.html",
        dulces = dulces,
        title = "Lista de dulces",
        current_user = current_user,
    )

def create_dulce():
    return render_template(
        "create_dulce.html",
        title = "Crear dulce",
        current_user = current_user
    )

def update_dulce(dulce):
    return render_template(
        "update_dulce.html",
        title="Editar dulce",
        dulce=dulce,
        current_user=current_user,
    )





