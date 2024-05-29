def test_register_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"} 
    response = test_client.post("/api/register", json=new_user) #lo envia en el register
    assert response.status_code == 201 # se acreado con exito 

def test_register_duplicate_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 400 #error del servidor 
    assert response.json["error"] == "El nombre de usuario ya está en uso" #si pasa los dos 2 parrafos 


def test_login_user(test_client):
    user_credentials = {"username": "testuser", "password": "testpassword"} # para el registro del login
    response = test_client.post("/api/login", json=user_credentials) #hace los acredenciales 
    assert response.status_code == 200
