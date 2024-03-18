import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

mi_pizza = {
    "tamaño": "Pequeño",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso","Picante"]
}
response = requests.post(url, json=mi_pizza, headers=headers)
print(response.json())