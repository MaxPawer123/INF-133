from flask import Blueprint, request, jsonify
from models.book_model import Book
from views.book_view import render_book_detail, render_book_list
from utils.decorators import jwt_required, roles_required

#Crear un blueprint para el controlador
book_bp = Blueprint("book", __name__)



#Ruta para obtener la lista de libros
@book_bp.route("/books", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_books():
    books = Book.get_all()
    return jsonify(render_book_list(books))


#Ruta para obtener un libro especifico por id 
@book_bp.route("/books/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_book(id):
    book = Book.get_by_id(id)
    if book:
        return jsonify(render_book_detail(book))
    return jsonify({"error":"Libro no encontrado"}), 404

#Ruta para crear un nuevo libro y guardarlo en la base de datos
@book_bp.route("/books", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_book():
    data = request.json
    title = data.get("title")
    author = data.get("author")
    edition = data.get("edition")
    availability = data.get("availability")

    #Validadcion simple de datos de entrada
    if not title or not author or not edition or not availability:
        return jsonify({"error":"Faltan datos"}), 400
    #Crear un nuevo libro
    book = Book(title=title, author=author, edition=edition, availability=availability)
    book.save()
    return jsonify(render_book_detail(book)), 201


#Ruta para actualizar un libro existente
@book_bp.route("/books/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_book(id):
    book = Book.get_by_id(id)
    if not book:
        return jsonify({"error":"Libro no encontrado"}), 404
    
    data = request.json
    title = data.get("title")
    author = data.get("author")
    edition = data.get("edition")
    availability = data.get("availability")

    #Actualziar los datos del libro
    book.update(title=title, author=author, edition=edition, availability=availability)
    return jsonify(render_book_detail(book))

#Ruta para eliminar un animal existente
@book_bp.route("/books/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_animal(id):
    book = Book.get_by_id(id)
    if not book:
        return jsonify({"error":"libro no encontrado"}),404
    
    #eliminar el libro de la base de datos
    book.delete()
    
    #Respuesta vacia con codigo de estado 204
    return "", 204

