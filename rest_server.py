from http.server import HTTPServer,BaseHTTPRequestHandler
import json


estudiante={
    "id":3,
    "nombre":"david",
"apellido":"Mamani",
"carrer":"INFORMatica"
}

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GIT(self):
        if self.path=="/lista_estudiante": 
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_response()
            self.wfile.write(json.dumps(estudiante).encode('utf-8'))

def run_server(port=8000):
    try:  
        server_address = ('localhost', port)  # Cambia el puerto según sea necesario

        httpd=HTTPServer(server_address,RESTRequestHandler)
        print('Iniciando servidor web en https://localhost:8000/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando el servidor web')
        httpd.socket.close()

if __name__== "__main__" :
    run_server()
