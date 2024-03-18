from http.server import BaseHTTPRequestHandler, HTTPServer
import json

#los factory se convierte el builder 
#Objetos mas complejos pero paso a paso 
#como la fabrica
#El builder es capaz de decir la flexibilidad 

# Producto: Pizza
class Pizza:
    def __init__(self):
        self.tamaño = None
        self.masa = None
        self.toppings = []

    def __str__(self):
        return f"Tamaño: {self.tamaño}, Masa: {self.masa}, Toppings: {', '.join(self.toppings)}"

#Builder: Constructor de pizzas
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza() #Aqui viene la el objeto

    def set_tamaño(self, tamaño):
        self.pizza.tamaño = tamaño

    def set_masa(self, masa):
        self.pizza.masa = masa

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
#devuelve la pizza 
    def get_pizza(self):
        return self.pizza

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

# Manejador de solicitudes HTTP
class PizzaHandler(BaseHTTPRequestHandler):
       def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.wfile.write(json.dumps(data).encode("utf-8"))
       def do_POST(self):
        if self.path == '/pizza':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            # Crear instancia de PizzaBuilder y construir la pizza
            builder = PizzaBuilder()
            builder.set_tamaño(data.get('tamaño', None))
            builder.set_masa(data.get('masa', None))
            for topping in data.get('toppings', []):
                builder.add_topping(topping)

            pizza = builder.get_pizza()

            # Enviar la respuesta HTTP con los datos de la pizza
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(pizza).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=PizzaHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
    
    
    
    
    
    
    
    
    
    