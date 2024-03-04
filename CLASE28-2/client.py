import requests
#DAVID MAMANI VALERIANO

# Consultando a un servidor RESTful
url = "http://localhost:8000/"

### Inciso a

# # GET para mostrar todas las carreras
ruta_get_carreras = url + "/carreras/"
get_response_carreras = requests.request(method="GET", url=ruta_get_carreras)

print(get_response_carreras.text)

### Inciso b

# # GET para mostrar a los estudiantes de la carrera de "Economia"
ruta_get_eco = url + "/economia/"

get_response_eco = requests.request(method="GET", url=ruta_get_eco)
print(get_response_eco.text)

### Inciso C 

# # POST agrega un nuevo estudiante por la ruta /economia

ruta_post_eco = url + "economia/"
nuevo_estudiante = {
    "nombre": "David",
    "apellido": "Mamani",
}
post_response_eco = requests.request(method="POST", url=ruta_post_eco, json=nuevo_estudiante)
#print(post_response_eco.text)

# segundo estudiante
ruta_post_eco = url + "economia/"
nuevo_estudiante = {
    "nombre": "Jose",
    "apellido": "Suarez",
}
post_response_eco = requests.request(method="POST", url=ruta_post_eco, json=nuevo_estudiante)
#print(post_response_eco.text)

# # GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)

print(get_response.text)