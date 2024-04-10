
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse,parse_qs  

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
        "carrera": "Economia",
    },
    
    {
        "id": 6,
        "nombre": "Jose",
        "apellido": "Mamani",
        "carrera": "Economia",
    },
    {
        "id": 7,
        "nombre": "Maria",
        "apellido": "Queso",
        "carrera": "Medicina",
    },

]
    

class EstudiantesService:
    @staticmethod
    def find_student(self, id):
        return next(
            (estudiante for estudiante in estudiantes if estudiante["id"] == id),
            None,
        )
            
        

class RESTRequestHandler(BaseHTTPRequestHandler):

    def add_student(self,data):
        data = self.read_data()
        data["id"] = len(estudiantes) + 1
        estudiantes.append(data)
  
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data
    
    #Despues de signo de interogacion les parece un monton de coueri parse
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path == "/estudiantes":
            if "apellido" in query_params:
                apellido = query_params["apellido"][0]
                estudiantes_filtrados = [
                    estudiante
                        for estudiante in estudiantes
                        if estudiante["apellido"] == apellido
                ]
                if estudiantes_filtrados != []:
                    self.response_handler(200, estudiantes_filtrados)
                else:
                    self.response_handler(204, [])
            else:
                self.response_handler(200, estudiantes)
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id)
            if estudiante:
                self.response_handler(200, [estudiante])
            else:
                self.response_handler(204, [])
        

        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    
    def do_POST(self):
        if self.path == "/estudiantes":
            data = self.read_data()
            data["id"] = len(estudiantes) + 1
            estudiantes.append(data)
            self.response_handler(201, estudiantes)

        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id)
            data = self.read_data()
            if estudiante:
                estudiante.update(data)
                self.response_handler(200, [estudiantes])
            else:
                self.response_handler(404, {"Error": "Estudiante no encontrado"})
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_DELETE(self):
        if self.path == "/estudiantes":
            estudiantes.clear()
            self.response_handler(200, estudiantes)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})




class HTTPResponseHandler:
    @staticmethod
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()

