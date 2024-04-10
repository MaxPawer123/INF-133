import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

# GET /tacos
response = requests.get(url)
print(response.json())

# POST /tacos
mi_taco = {
    "base": "Grande",
    "guiso": "pollo",
    "salsa": "picante",
    "toppings": ["Jamon", "Queso","carne"]
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

# GET /tacos  
response = requests.get(url)
print(response.json())

# PUT /pizzas/1
edit_taco = {
    "base": "Mediano",
    "guiso": "carne",
    "salsa": "mostaza",
    "toppings": ["Peperoni", "Queso","Pollo"]
}
response = requests.post(url, json=edit_taco, headers=headers)
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())

# DELETE /tacos/1
response = requests.delete(url + "/1")
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())