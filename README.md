# INF-133

Mi primer servidor web
python -m http.server

crear un index.html
from http.server import HTTPServer, SimpLeHTTPRequestHandler
def run(server_class=HTTPServer, handler_class=SimpLeHTTPRequestHandler):
try:
server_address = ('', 8000)
httpd = server_class(server_addres, handler_class)
print('Iniciando servidor web en http://localhost:8000/')
httpd.serve_forever()
except KeyboardInterrupt:
print('Apagando servidor web')
httpd.socked.close()
