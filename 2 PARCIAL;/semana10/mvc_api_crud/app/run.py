from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.book_controller import book_bp
from controllers.user_controller import user_bp
from database import db
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

#Configuramos la clave secreta para JWT
app.config["JWT_SECRET_KEY"] = "tu_clave_secreta_aqui"
# Configuración de la URL de la documentación OpenAPI
# Ruta para servir Swagger UI
SWAGGER_URL = "/api/docs"
# Ruta de tu archivo OpenAPI/Swagger
API_URL = "/static/swagger.json"


# Configura la URL de la documentación OpenAPI
SWAGGER_URL = "/api/docs"  # Ruta para servir Swagger UI
API_URL = "/static/swagger.json"  # Ruta de tu archivo OpenAPI/Swagger
# Inicializa el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Bliblioteca API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)



#Configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializa la base de datos
db.init_app(app)
#Iniciaza la extension JWTManager
jwt = JWTManager(app)

#Registra el blueprint de libros y usuarios en la aplicaion
app.register_blueprint(book_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

#Crea las tablas si no existen
with app.app_context():
    #Crea las tablas
    db.create_all()

#Ejecuta la aplicacion
if __name__ == "__main__":
    app.run(debug=True)