from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Producto: Pizza
class Pizza:
    def __init__(self):
        self.tamaño = None
        self.masa = None
        self.toppings = []

    def __str__(self):
        return f"Tamaño: {self.tamaño}, Masa: {self.masa}, Toppings: {', '.join(self.toppings)}"

# Builder: Constructor de pizzas
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_tamaño(self, tamaño):
        self.pizza.tamaño = tamaño

    def set_masa(self, masa):
        self.pizza.masa = masa

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)

    def get_pizza(self):
        return self.pizza

class PizzaService:
    def build_pizza(self, data):
        tamaño = data.get('tamaño', None)
        masa = data.get('masa', None)
        toppings = data.get('toppings', [])
        builder = PizzaBuilder()
        pizzeria = Pizzeria(builder)
        pizza = pizzeria.create_pizza(tamaño, masa, toppings)

        response = {
            'tamaño': pizza.tamaño,
            'masa': pizza.masa,
            'toppings': pizza.toppings
        }
        return response
# Director: Pizzería
class Pizzeria:
    def __init__(self, builder):
        self.builder = builder

    def create_pizza(self, tamaño, masa, toppings):
        self.builder.set_tamaño(tamaño)
        self.builder.set_masa(masa)
        for topping in toppings:
            self.builder.add_topping(topping)
        return self.builder.get_pizza()

class HTTPResponseHandler:
    @staticmethod
    def handler_response(handler,status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

# Manejador de solicitudes HTTP
class PizzaHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/pizza':
            data = self.read_data()
            response = PizzaService.build_pizza(self, data)
            HTTPResponseHandler.handler_response(self,200,response)
        else:
            HTTPResponseHandler.handler_response(self,200,{"Error"})

    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data

def run(server_class=HTTPServer, handler_class=PizzaHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
    
    