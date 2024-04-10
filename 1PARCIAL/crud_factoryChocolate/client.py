import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocolate_data = {
    "chocolate_type": "tablet",
    "peso": "20kg",
    "sabor": "dulce"
    
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "bonbon",
    "peso": "302kg",
    "sabor": "dulce",
    "relleno": "crema"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "truffle",
    "peso": "50kg",
    "sabor": "amargo",
    "relleno": "chocolate"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())

# PUT /deliveries/{vehicle_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "peso": "15kg"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())

# DELETE /deliveries/{vehicle_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())