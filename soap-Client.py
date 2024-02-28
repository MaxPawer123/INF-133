from zeep import Client

# Crear un cliente para el servicio web SOAP
client = Client('http://ejemplo.com/servicio?wsdl')

# Llamar a un método del servicio
result = client.service.Saludar(nombre="Tatiana")

# Hacer algo con el resultado
print(result)


