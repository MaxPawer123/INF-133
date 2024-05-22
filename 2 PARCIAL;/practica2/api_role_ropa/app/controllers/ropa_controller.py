from flask import Blueprint, request, jsonify
from models.ropa_model import Ropa
from views.ropa_view import render_ropa_list, render_ropa_detail
from utils.decorators import jwt_required, roles_required
from functools import wraps

# Crear un blueprint para el controlador de dulces
ropa_bp = Blueprint("ropa", __name__)

# Ruta para obtener la lista de dulces
@ropa_bp.route("/ropas", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_ropas():
    ropas = Ropa.get_all()
    return jsonify(render_ropa_list(ropas))

# Ruta para obtener un dulce específico por su ID
@ropa_bp.route("/ropas/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_ropa(id):
    ropa = Ropa.get_by_id(id)
    if ropa:
        return jsonify(render_ropa_detail(ropa))
    return jsonify({"error": "Dulce no encontrado"}), 404

# Ruta para crear un nuevo dulce
@ropa_bp.route("/ropas", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_ropa():
    data = request.json
    talla = data.get("talla")
    color = data.get("color")
    precio = data.get("precio")
    tipo_tela = data.get("tipo")
    genero = data.get("genero")
    stock = data.get("stock")
    tipo = data.get("tipo")
    descuento = data.get("descuento")

    # Validación simple de datos de entrada
    if not (talla and color and precio and genero and stock and tipo and descuento is not None):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    ropa = Ropa(talla=talla,color=color, precio=precio,tipo_tela=tipo_tela,genero=genero ,stock=stock,tipo=tipo,descuento=descuento)
    ropa.save()

    return jsonify(render_ropa_detail(ropa)), 201

# Ruta para actualizar un dulce existente
@ropa_bp.route("/ropas/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_ropa(id):
    ropa = Ropa.get_by_id(id)

    if not ropa:
        return jsonify({"error": "Dulce no encontrado"}), 404

    data = request.json
    talla = data.get("talla")
    color = data.get("color")
    precio = data.get("precio")
    tipo_tela = data.get("tipo")
    genero = data.get("genero")
    stock = data.get("stock")
    tipo = data.get("tipo")
    descuento = data.get("descuento")
    # Actualizar los datos del dulce
    ropa.update(talla=talla,color=color, precio=precio,tipo_tela=tipo_tela,genero=genero ,stock=stock,tipo=tipo,descuento=descuento)

    return jsonify (render_ropa_detail(ropa))
@ropa_bp.route("/ropas/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_ropa(id):
    ropa = Ropa.get_by_id(id)

    if not ropa:
        return jsonify({"error": "Ropa no encontrado"}), 404

    ropa.delete()

    return "", 204