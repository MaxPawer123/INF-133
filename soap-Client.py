from zeep import Client 

client =Client(
    "http://localhost:8000/"
)
# peticion o requests
result = client.service.Saludar("David")
result2 = client.service.Sumar(1,2)
result3 = client.service.EsPalindromo('A luna ese anula')
print(result)
print(result2)
print(result3)




