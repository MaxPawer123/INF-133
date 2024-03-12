import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'



query_actulizar =  """
mutation {
        ActulizarEstudiante(id: 2) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
# Solicitud POST al servidor GraphQL
response_mutation = requests.post(url, json={'query': query_actulizar})
print(response_mutation.text)

