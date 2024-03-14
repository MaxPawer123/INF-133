from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation


class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()


class Query(ObjectType):
    estudiantes = List(Estudiante)
    estudiante_por_id = Field(Estudiante, id=Int())
    estudiante_por_nombre_apellido= Field(Estudiante, nombre=String(),apellido=String()) 
    estudiante_por_carrea=Field(Estudiante, carrera=String()) 
    def resolve_estudiante_por_id(root, info, id):
        for estudiante in estudiantes:
            if estudiante.id == id:
                return estudiante
        return None
    def resolve_estudiante_por_nombre_apellido(root, info, nombre,apellido):
        for estudiante in estudiantes:
            if estudiante.nombre == nombre and estudiante.apellido and apellido:
                return estudiante
        return None
    def resolve_estudiante_por_carrera(root, info, carrera):
        estudiante_carrera = list(estudiante for estudiante in estudiantes if estudiante.carrera == carrera)            
        return estudiante_carrera
    
    

class CrearEstudiante(Mutation):
    class Arguments:
        nombre = String()
        apellido = String()
        carrera = String()

    estudiante = Field(Estudiante)

  
    
    def mutate(root, info, nombre, apellido, carrera):
        # Añadir 3 estudiantes de la carrera Arquitectura
        for _ in range(3):
            nuevo_estudiante = Estudiante(
                id=len(estudiantes) + 1,
                nombre=nombre,
                apellido=apellido,
                carrera=carrera
            )
            estudiantes.append(nuevo_estudiante)

        # Puedes devolver una lista con los estudiantes creados si es necesario
        return [CrearEstudiante(estudiante=nuevo_estudiante) for nuevo_estudiante in estudiantes[-3:]]

class DeleteEstudiante(Mutation):
    class Arguments:
        id = Int()

    estudiante = Field(Estudiante)

    def mutate(root, info, id):
        for i, estudiante in enumerate(estudiantes):
            if estudiante.id == id:
                estudiantes.pop(i)
                return DeleteEstudiante(estudiante=estudiante)
        return None
    
class ActualizarEstudiante(Mutation):
    class Arguments:
        id = Int()
        carrera = String()

    estudiante = Field(Estudiante)

    def mutate(root, info, id, carrera):
        estudiantes = root.estudiantes
        for estudiante in estudiantes:
            if estudiante.id == id:
                estudiante.carrera = carrera
                return ActualizarEstudiante(estudiante=estudiante)
        return None

class Mutations(ObjectType):
    crear_estudiante = CrearEstudiante.Field()
    delete_estudiante = DeleteEstudiante.Field()

estudiantes = [
    Estudiante(
        id=1, nombre="Pedrito", apellido="García", carrera="Arquitectura"
    ),
    Estudiante(id=2, nombre="Jose", apellido="Lopez", carrera="Arquitectura"),
    
    Estudiante(
        id=3, nombre="David", apellido="García", carrera="Ingeniería de Sistemas"
    ),
    Estudiante(id=4, nombre="Maria", apellido="Lopez", carrera="Medicina"),
]

schema = Schema(query=Query, mutation=Mutations)


class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            print(data)
            result = schema.execute(data["query"])
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
    
    
    

    """
      def mutateaaaa(root, info, nombre, apellido, carrera):
        nuevo_estudiante = Estudiante(
            id=len(estudiantes) + 1, 
            nombre=nombre, 
            apellido=apellido, 
            carrera=carrera
        )
        estudiantes.append(nuevo_estudiante)

        return CrearEstudiante(estudiante=nuevo_estudiante)
    """