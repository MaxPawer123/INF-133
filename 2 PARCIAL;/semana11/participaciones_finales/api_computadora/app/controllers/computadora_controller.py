from flask import Blueprint, request, jsonify
from models.computadora_model import Computadora
from views.computadora_view import render_computadora_list, render_computadora_detail
from utils.decorators import jwt_required, roles_required
from functools import wraps

# Crear un blueprint para el controlador de libros
computadora_bp = Blueprint("computadora", __name__)


@computadora_bp.route("/computadoras", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_computadoras():
    computadoras = Computadora.get_all()
    return jsonify(render_computadora_list(computadoras))

@computadora_bp.route("/computadoras/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_computadora(id):
    computadora = Computadora.get_by_id(id)
    if computadora:
        return jsonify(render_computadora_detail(computadora))
    return jsonify({"error": "Computadora no encontrado"}), 404

@computadora_bp.route("/computadoras", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_computadora():
    data = request.json
    marca = data.get("marca")
    precio = data.get("precio")
    tipo = data.get("tipo")
    acesorios = data.get("acesorios")

    # Validación simple de datos de entrada
    if not (marca and precio and tipo and acesorios is not None):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    computadora = Computadora(marca=marca, precio=precio, tipo=tipo, acesorios=acesorios)
    computadora.save()

    return jsonify(render_computadora_detail(computadora)), 201


@computadora_bp.route("/computadoras/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_computadora(id):
    computadora = Computadora.get_by_id(id)

    if not computadora:
        return jsonify({"error": "Computadora no encontrado"}), 404

    data = request.json
    marca = data.get("marca")
    precio = data.get("precio")
    tipo = data.get("tipo")
    acesorios = data.get("acesorios")

    computadora.update(marca=marca, precio=precio, tipo=tipo, acesorios=acesorios)

    return jsonify(render_computadora_detail(computadora))


@computadora_bp.route("/computadoras/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_computadora(id):
    computadora = Computadora.get_by_id(id)

    if not computadora:
        return jsonify({"error": "Computadora no encontrado"}), 404

    computadora.delete()
    return "", 204