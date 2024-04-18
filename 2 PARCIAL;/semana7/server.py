# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask y la asigna a la variable 'app'.
# '__name__' es un parámetro especial que representa el nombre del módulo actual.
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.
app = Flask(__name__)


# Este decorador asociará la función 'hello_world()' con la ruta raíz ('/') de la aplicación.
# Esto significa que cuando alguien acceda a la ruta raíz en el navegador, Flask ejecutará esta función.
@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

def sumar_dos_numero():
    return f"num1,{5} num2,{3}" 

# Ruta para saludar utilizando el método GET.
@app.route("/saludar", methods=["GET"])
def saludar():
    # Obtener el nombre de los argumentos de la URL.
    nombre = request.args.get("nombre")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})


@app.route("/sumar", methods=["GET"])
def sumar():
    num1 = int( request.args.get("num1"))
    num2 = int( request.args.get("num2"))
    if not num1 and num2:
        return(
            jsonify({"error": "Se requiere un num1 o num2 en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"la suma es, {num1+num2}"})

@app.route("/palindromo", methods=["POST"])  # Cambio a POST
def palindromo():
    data = request.json
    cadena = data.get("cadena")
    
    if not cadena:
        return jsonify({"error": "Se requiere una cadena en el cuerpo de la solicitud."}), 400
    
    if cadena == cadena[::-1]:
        return jsonify({"mensaje": f"La cadena '{cadena}' es un palíndromo."}), 200
    else:
        return jsonify({"mensaje": f"La cadena '{cadena}' no es un palíndromo."}), 200


@app.route("/contar", methods=["POST"])  # Cambio a POST
def contar():
    data = request.json
    cadena = data.get("cadena")
    vocal = data.get("vocal")
    
    if not cadena or not vocal:
        return jsonify({"error": "Se requiere una cadena y una vocal en el cuerpo de la solicitud."}), 400
    
    count = cadena.count(vocal)
    return jsonify({"resultado": count}), 200

# Esta condición verifica si este script se está ejecutando directamente.
# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == "__main__":
    app.run()