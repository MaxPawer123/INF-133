from http.server import HTTPServer,SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    try:  
        server_address = ('localhost', 8000)  # Cambia el puerto según sea necesario

        httpd=server_class(server_address,handler_class)
        print('Iniciando servidor web en https://localhost:8000/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando el servidor web')
        httpd.socket.close()


#Sebastian Guis 
#Levantar el servidor 
            
if __name__== "__main__" :
 run()
