import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
{
        estudiantes{
            id
            nombre
            carrera
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL con parametros
query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
response2 = requests.post(url, json={'query': query})
print(response2.text)

#BUSCAR EL NOMBRE Y APELLido
#En la respuesta no tiene que ser el mismo atributo
query_nombreA = """
    {
        estudiantePorNombreApellido( nombre: "Jose",apellido: "Lopez"){
            id
        }
    }
"""

# Solicitud POST al servidor GraphQL
response3 = requests.post(url, json={'query': query_nombreA})
print(response3.text)


#BUSCAR EL POR CARRERA
#En la respuesta no tiene que ser el mismo atributo
query_carrera = """
    {
        estudiantePorCarrera( carrera:"Arquitectura"){
            id
        }
    }
"""

# Solicitud POST al servidor GraphQL
response4 = requests.post(url, json={'query': query_carrera})
print(response4.text)


# Definir la consulta GraphQL para crear nuevo estudiante


# Definir la consulta GraphQL para crear nuevo estudiante
query_crear_Aquitectura = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez",carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation2 = requests.post(url, json={'query': query_crear_Aquitectura})
print(response_mutation2.text)


# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation3 = requests.post(url, json={'query': query_eliminar})
print(response_mutation3.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)





"""
query_crear = """
"""mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }"""
"""

response_mutation1 = requests.post(url, json={'query': query_crear})
print(response_mutation1.text)

"""







