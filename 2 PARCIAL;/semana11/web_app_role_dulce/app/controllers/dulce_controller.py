from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.dulce_model import Dulce
from views import dulce_view

# Importamos el decorador de roles
from utils.decorators import role_required

#de que se encarga el comtrolar 
#que controla las rutas 
#gestionar las rutas 
# tokens es jwt
dulce_bp = Blueprint("dulce", __name__)

#toca los permisos
@dulce_bp.route("/dulces")
@login_required
def list_dulces():
    dulces = Dulce.get_all()
    return dulce_view.list_dulces(dulces)


@dulce_bp.route("/dulces/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
    
def create_dulce():
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = request.form["peso"]
            sabor = request.form["sabor"]
            origen= request.form["origen"]
            dulce = Dulce(marca=marca, peso=peso, sabor=sabor,origen=origen)
            dulce.save()
            flash("Dulce creado exitosamente", "success")
            return redirect(url_for("dulce.list_dulce"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return dulce_view.create_dulce()


@dulce_bp.route("/dulces/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_dulce(id):
    libro = Dulce.get_by_id(id)
    if not libro:
        return "Libro no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = request.form["peso"]
            sabor = request.form["sabor"]
            origen= request.form["origen"]
            dulce = Dulce(marca=marca, peso=peso, sabor=sabor,origen=origen)
           
            flash("Libro actualizado exitosamente", "success")
            return redirect(url_for("animal.list_dulces"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return dulce_view.update_animal(dulce)


@dulce_bp.route("/dulces/<int:id>/delete")
@login_required
@role_required("admin")
def delete_dulce(id):
    libro = Dulce.get_by_id(id)
    if not libro:
        return "dulce no encontrado", 404
    if current_user.has_role("admin"):
        libro.delete()
        flash("dulce eliminado exitosamente", "success")
        return redirect(url_for("dulce.list_dulce"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
