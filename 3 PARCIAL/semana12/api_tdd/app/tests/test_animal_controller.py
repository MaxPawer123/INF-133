"""
def test_get_animals(test_client, auth_headers):
    response = test_client.get("/api/animals", headers=auth_headers) #que vemos la lista de animales y la cabecera 
    assert response.status_code == 200
    assert response.json == []


def test_create_animal(test_client, auth_headers):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5} # creamos los aniamles 
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Lion"

#para obtener un amimal
def test_get_animal(test_client, auth_headers):
    # Primero crea un animal 
    data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora obtén el animal
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Tiger"


def test_update_animal(test_client, auth_headers): #auth_headers= token 
    # Primero crea un animal
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora actualiza el animal
    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(
        f"/api/animals/{animal_id}", json=update_data, headers=auth_headers #aqui verificamos ne la base de datos 
    )
    assert response.status_code == 200
    assert response.json["species"] == "Loxodonta africana"
    assert response.json["age"] == 12


def test_delete_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora elimina el animal
    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers) #borramos el animal girafa 
    assert response.status_code == 204 #con exito sin respuesta

    # Verifica que el animal ha sido eliminado
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 404
"""

def test_get_animals(test_client, auth_headers_admin):
    response = test_client.get("/api/animals", headers=auth_headers_admin)
    assert response.status_code == 200
    assert response.json == []

def test_create_animal_unauthorized(test_client, auth_headers_user):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data, headers=auth_headers_user)
    assert response.status_code == 403  # Forbidden, user role should not allow creating animals

def test_create_animal_no_auth(test_client):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data)
    assert response.status_code == 401  # Unauthorized, no token provided

def test_get_animal_unauthorized(test_client, auth_headers_user):
    data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=auth_headers_admin)
    assert response.status_code == 201
    animal_id = response.json["id"]

    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers_user)
    assert response.status_code == 403  # Forbidden, user role should not allow viewing a specific animal

def test_update_animal_unauthorized(test_client, auth_headers_user):
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=auth_headers_admin)
    assert response.status_code == 201
    animal_id = response.json["id"]

    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(f"/api/animals/{animal_id}", json=update_data, headers=auth_headers_user)
    assert response.status_code == 403  # Forbidden, user role should not allow updating animals

def test_delete_animal_unauthorized(test_client, auth_headers_user):
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=auth_headers_admin)
    assert response.status_code == 201
    animal_id = response.json["id"]

    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers_user)
    assert response.status_code == 403  # Forbidden, user role should not allow deleting animals

def test_register_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 201

def test_register_duplicate_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 400
    assert response.json["error"] == "El nombre de usuario ya está en uso"

def test_login_user(test_client):
    user_credentials = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/login", json=user_credentials)
    assert response.status_code == 200