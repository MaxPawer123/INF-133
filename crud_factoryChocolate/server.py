from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
chocolates = {}


class ChocolateProduct:
    def __init__(self, peso, sabor,relleno):
        self.peso = peso
        self.sabor = sabor
        self.relleno=relleno


class Tablet(ChocolateProduct):
    def __init__(self, peso, sabor):
        super().__init__(peso, sabor)


class Bonbon(ChocolateProduct):
    def __init__(self, peso, sabor, relleno):
        super().__init__(peso, sabor)
        self.relleno = relleno


class Truffle(ChocolateProduct):
    def __init__(self, peso, sabor, relleno):
        super().__init__(peso, sabor)
        self.relleno = relleno


class ChocolateFactory:
    @staticmethod
    def create_chocolate(product_type, peso, sabor, relleno=None):
        if product_type == "tablet":
            return Tablet(peso, sabor)
        elif product_type == "bonbon":
            return Bonbon(peso, sabor, relleno)
        elif product_type == "truffle":
            return Truffle(peso, sabor, relleno)
        else:
            raise ValueError("Tipo de producto de chocolate no válido")



class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class ChocolateService:
    def __init__(self):
        self.factory = ChocolateFactory()

    def add_chocolate(self, data):
        product_type = data.get("type", None)
        weight = data.get("peso", None)
        flavor = data.get("sabor", None)
        filling = data.get("relleno", None) if product_type in ["bonbon", "truffle"] else None

        chocolate = self.factory.create_chocolate(product_type, weight, flavor, filling)
        chocolates[len(chocolates) + 1] = chocolate
        return chocolate

    def list_chocolates(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()}

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id in chocolates:
            chocolate = chocolates[chocolate_id]
            weight = data.get("peso", None)
            flavor = data.get("sabor", None)
            filling = data.get("relleno", None)
            if weight:
                chocolate.weight = weight
            if flavor:
                chocolate.flavor = flavor
            if filling:
                if isinstance(chocolate, (Bonbon, Truffle)):
                    chocolate.filling = filling
                else:
                    raise ValueError("El chocolate no admite relleno")
            return chocolate
        else:
            raise ValueError("Chocolate no encontrado")

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in chocolates:
            del chocolates[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:
            raise ValueError("Chocolate no encontrado")

class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.delivery_service = ChocolateService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.delivery_service.list_chocolate()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.update_chocolate(chocolate_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.delivery_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()