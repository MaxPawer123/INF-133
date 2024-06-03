# se va almacenar el cuerpo de la ruta 
def test_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 404  #pench for word


def test_swagger_ui(test_client):
    response = test_client.get("/api/docs/")  #hacemos una ruta en api 
    assert response.status_code == 200
    #buscamos una pagina en swager.iu
    assert b'id="swagger-ui"' in response.data
#id="swagger-ui se agrga al data