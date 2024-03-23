import requests
#NOS JALA los que tiene una deuda de 5 años
#no encontrar 

# Listar todos los posts
response = requests.get("http://localhost:8000/posts")
print(response.json())

# Obtener el post 2
response = requests.get("http://localhost:8000/post/2")
print(response.json())

# Crear un nuevo post y podemos la nueva post
new_post_data = {
    "title": "Mi experiencia como dev",
    "content": "Mi experiencia como desarrollador es increíble.",
}
response = requests.post("http://localhost:8000/posts", data=new_post_data)
print(response.json())

# Actualizar el contenido del post 3
update_data = {
    "title": "Post 3 Actualizado",
    "content": "En Progreso",
}
response = requests.put("http://localhost:8000/post/3", data=update_data)
print(response.json())

# Eliminar el post 2
## Debería devolver 204 si se eliminó correctamente
response = requests.delete("http://localhost:8000/post/2")
print(response.status_code)  





