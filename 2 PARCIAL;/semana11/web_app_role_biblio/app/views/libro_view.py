from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de
# animales y renderiza el template `animales.html`
def list_libros(libros):
    return render_template(
        "libro.html",
        libros=libros,
        title="Lista de libros",
        current_user=current_user,
    )


# La función `create_animal` renderiza el
# template `create_animal.html` o devuelve un JSON
# según la solicitud
def create_libro():
    return render_template(
        "create_libro.html", title="Crear Libro", current_user=current_user
    )


# La función `update_animal` recibe un animal
# y renderiza el template `update_animal.html`
def update_libro(libro):
    return render_template(
        "update_libro.html",
        title="Editar Libro",
        animal=libro,
        current_user=current_user,
    )
