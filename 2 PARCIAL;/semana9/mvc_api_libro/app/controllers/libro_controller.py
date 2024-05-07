from flask import Blueprint, request, jsonify
from models.libro_model import Libro
from views.libro_view import render_libro_list, render_libro_detail

# Crear un blueprint para el controlador de animales
libro_bp = Blueprint("libro", __name__)


# Ruta para obtener la lista de animales
@libro_bp.route("/libros", methods=["GET"])
def get_libros():
    animals = Libro.get_all()
    return jsonify(render_libro_list(animals))


# Ruta para obtener un animal específico por su ID
@libro_bp.route("/libros/<int:id>", methods=["GET"])
def get_libro(id):
    animal = Libro.get_by_id(id)
    if animal:
        return jsonify(render_libro_detail(animal))
    return jsonify({"error": "Animal no encontrado"}), 404


# Ruta para crear un nuevo animal @animal_bp = 
@libro_bp.route("/libros", methods=["POST"])
def create_libro():
    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")

    # Validación simple de datos de entrada
    if not name or not species or age is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo animal y guardarlo en la base de datos
    animal = Libro(name=name, species=species, age=age)
    animal.save()

    return jsonify(render_libro_detail(animal)), 201


# Ruta para actualizar un animal existente
@libro_bp.route("/libros/<int:id>", methods=["PUT"])
def update_animal(id):
    animal = Libro.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    # Actualizar los datos del animal
    animal.update(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)

    return jsonify(render_libro_detail(animal))


# Ruta para eliminar un animal existente
@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Animal no encontrado"}), 404

    # Eliminar el animal de la base de datos
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
