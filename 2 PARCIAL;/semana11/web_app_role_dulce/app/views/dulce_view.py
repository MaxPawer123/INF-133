from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de
# animales y renderiza el template `animales.html`
def list_dulces(libros):
    return render_template(
        "dulce.html",
        animals=libros,
        title="Lista de dulces",
        current_user=current_user,
    )


# La función `create_animal` renderiza el
# template `create_animal.html` o devuelve un JSON
# según la solicitud
def create_dulce():
    return render_template(
        "create_dulce.html", title="Crear Dulce", current_user=current_user
    )


# La función `update_animal` recibe un animal
# y renderiza el template `update_animal.html`
def update_dulce(dulce):
    return render_template(
        "update_dulce.html",
        title="Editar Dulce",
        dulce=dulce,
        current_user=current_user,
    )
