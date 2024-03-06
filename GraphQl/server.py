from http.server import HTTPServer, BaseHTTPRequestHandler
#HTTPServer
#BaseHTTPRequestHandler determina o recibir la petiicion del servidor 
import json  # este modulo texto plano a convetir objeto en python
from graphene import ObjectType,String,Int ,List, Schema

#graphene Biblioteca para contruir 
#rest es arquitectura  soap=protocolo;
#yszipi  ObjectType =tipo de objeto  es el que maneja   Schema= nos da todas las consultas 


class Query(ObjectType):
    hello=String() #los conveerte en cadena 
    goodbye=String()
    
    def resolve_hello(root, info): #tiene que ser el mismo nombre
        return "Hello ,world!"
    
    def resolve_goodbye(root, info): #tiene que ser el mismo nombre
        return "Bye Bye"
    def resolve_hello_goodbye(root, info): #tiene que ser el mismo nombre
        return "Hello ,world! Bye Bye"
    
        
schema = Schema(query=Query)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"]) 
            data = self.rfile.read(content_length)  #lee 
            data = json.loads(data.decode("utf-8"))  #tipo de codificacion que esmos
            result = schema.execute(data["query"]) #diccionario= clave o valor 
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})
            
def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run_server()


#501 error del servidor







