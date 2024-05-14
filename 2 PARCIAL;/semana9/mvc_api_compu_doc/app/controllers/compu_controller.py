from flask import Blueprint, request, jsonify
from semana9.mvc_api_compu_doc.app.models.compu_model import Libro
from views.libro_view import render_libro_list, render_libro_detail

libro_bp = Blueprint("libro", __name__)

@libro_bp.route("/libros", methods=["GET"])
def get_libros():
    libros = Libro.get_all()
    return jsonify(render_libro_list(libros))

@libro_bp.route("/libros/<int:id>", methods=["GET"])
def get_libro(id):
    libro = Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error": "Libro no encontrado"}), 404

@libro_bp.route("/libros", methods=["POST"])
def create_libro():
    data = request.json
    autor = data.get("autor")
    titulo = data.get("titulo")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad", True)

    if not autor or not titulo or not edicion:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    libro = Libro(autor=autor, titulo=titulo, edicion=edicion, disponibilidad=disponibilidad)
    libro.save()

    return jsonify(render_libro_detail(libro)), 201

@libro_bp.route("/libros/<int:id>", methods=["PUT"])
def update_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404

    data = request.json
    autor = data.get("autor")
    titulo = data.get("titulo")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    libro.update(autor=autor, titulo=titulo, edicion=edicion, disponibilidad=disponibilidad)

    return jsonify(render_libro_detail(libro))

@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404

    libro.delete()

    return "", 204