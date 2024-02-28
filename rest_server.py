
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
    
    {
        "id": 2,
        "nombre": "Pepe",
        "apellido": "Zamora",
        "carrera": "Seguridad de la Informacion",
    },
    {
        "id": 3,
        "nombre": "David",
        "apellido": "Mamani",
        "carrera": "Seguridad de la Informacion",
    },
     {
        "id": 4,
        "nombre": "Fabricio",
        "apellido": "Quispe",
        "carrera": "Ingeniería de Sistemas",
    },
    
    {
        "id": 5,
        "nombre": "Ariel",
        "apellido": "Quizaya",
        "carrera": "Seguridad de la Informacion",
    },

   

]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
            if self.path == '/lista_estudiantes':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
            elif self.path == '/buscar_nombre':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                nombres_con_P = [estudiante['nombre'] for estudiante in estudiantes if estudiante['nombre'].startswith('P')]
                self.wfile.write(json.dumps({"nombres que inician con P": nombres_con_P}).encode('utf-8'))
            elif self.path == '/contar_carreras':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()            
                carreras = [carrera['carrera'] for carrera in estudiantes]
                # cnt_carreras = carreras.count('Ingeniería de software')
                cnt_carreras = {}
                for carrera in carreras:
                    if carrera in cnt_carreras:
                        cnt_carreras[carrera] += 1
                    else:
                        cnt_carreras[carrera] = 1            
                self.wfile.write(json.dumps({"alumnos por carrera": cnt_carreras}).encode('utf-8'))
            elif self.path == '/total_estudiantes':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                #estudiantes = [estudiante for estudiante in estudiantes]
                cnt_estudiantes = len(estudiantes)
                self.wfile.write(json.dumps({"estudiantes totales": cnt_estudiantes}).encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))

            
    def do_POST(self):
        if self.path == '/agrega_estudiante':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
def run_server(port = 8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        print(f'Ir a <a href="http://localhost:{port}/buscar_nombre">buscar_nombre</a>')
        print(f'Ir a <a href="http://localhost:{port}/contar_carreras">contar_carreras</a>')
        print(f'Ir a <a href="http://localhost:{port}/total_estudiantes">total_estudiantes</a>')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()


