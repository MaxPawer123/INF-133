def test_get_animals(test_client, auth_headers):
    response = test_client.get("/api/libros", headers=auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_animal(test_client, auth_headers):
    data = {"autor": "David", "titulo": "chanchos", "edicion": "primera edicion","disponibilidad":"bueno"}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "David"


def test_get_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"autor": "Jose", "titulo": "ovejas", "edicion": "segunda edicion","disponibilidad":"mal"}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora obtén el animal
    response = test_client.get(f"/api/libros/{libro_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Jose"


def test_update_animal(test_client, auth_headers):
    # Primero crea un animal
    data ={"autor": "Ariel", "titulo": "gatos negros", "edicion": "segunda_edicion","disponibilidad":"buena"}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora actualiza el animal
    update_data = {"autor": "Ariel", "titulo": "gatos negros", "edicion": "segunda_edicion","disponibilidad":"buena"}
    response = test_client.put(
        f"/api/animals/{animal_id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json["edicion"] == "tercero_edicion"
    assert response.json["disponibilidad"] == "mal"


def test_delete_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"autor": "Maria", "titulo": "vacas", "edicion": "primera edicion","disponibilidad":"mal"}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora elimina el animal
    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 204

    # Verifica que el animal ha sido eliminado
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 404
