import requests

# URL del servidor Flask
url = 'http://localhost:5000/'

# Realizar una solicitud GET al servidor Flask
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
params = {'nombre': 'tu_nombre'}
response = requests.get(url+'saludar', params=params)

response = requests.get(url+'/sumar?num1=5&num2=3')
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

# Verificar si una cadena es un palíndromo
payload_palindromo = {'cadena': 'reconocer'}
response_palindromo = requests.post(url + 'palindromo', json=payload_palindromo)
if response_palindromo.status_code == 200:
    data_palindromo = response_palindromo.json()
    mensaje_palindromo = data_palindromo['mensaje']
    print("Respuesta del servidor (Palíndromo):", mensaje_palindromo)
else:
    print("Error al conectar con el servidor (Palíndromo):", response_palindromo.status_code)

# Contar una vocal en una cadena
payload_contar = {'cadena': 'excepciones', 'vocal': 'e'}
response_contar = requests.post(url + 'contar', json=payload_contar)
if response_contar.status_code == 200:
    data_contar = response_contar.json()
    resultado_contar = data_contar['resultado']
    print("Número de veces que aparece la vocal 'e':", resultado_contar)
else:
    print("Error al conectar con el servidor (Contar):", response_contar.status_code)