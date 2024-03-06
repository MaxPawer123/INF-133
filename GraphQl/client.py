import requests

# Definir la consulta GraphQL


query="""
    {
        Hello ,world
    }
"""
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
#se puede llamar el rquests

print(response.text)