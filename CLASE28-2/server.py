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
        "carrera": "Economia",
    },
    
    {
        "id": 6,
        "nombre": "Jose",
        "apellido": "Mamani",
        "carrera": "Economia",
    },


]
carreras = ["Ingeniería Informática", "Seguridad de la Informacion","Economia"]


class RESTRequestHandler(BaseHTTPRequestHandler):
    #Agrega una ruta para mostrar todas las carreras
    def do_POST(self):
        if self.path == "/estudiantes": 
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
    
        elif self.path.startswith("/economia/"):
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            post_data["carrera"] = "Economia"
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_PUT(self):
        if self.path.startswith("/estudiantes"):
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            id = data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(data)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_DELETE(self):
        if self.path == "/estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
     

    
    def do_GET(self):
            if self.path == "/estudiantes":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(carreras).encode("utf-8"))
            
            elif self.path.startswith("/estudiantes/carreras"):
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(carreras).encode("utf-8"))
            
            elif self.path.startswith("/estudiantes/carreras/economias"):
                estudiantes_economia = [estudiante for estudiante in estudiantes if estudiante["carrera"] == "Economía"]
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiantes_economia).encode("utf-8"))
                
            elif self.path.startswith("/estudiantes/"):
                id = int(self.path.split("/")[-1])
                estudiante = next(
                    (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                    None,
                )
                if estudiante:
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(estudiante).encode("utf-8"))
            else:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
        

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




"""
def do_POST(self):
        if self.path == "/estudiantes":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
"""