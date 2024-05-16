from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.libro_controller import libro_bp
from controllers.user_controller import user_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config["JWT_SECRET_KEY"] = "tu_clave_secreta_aqui"
# Configuración de la URL de la documentación OpenAPI
# Ruta para servir Swagger UI

# Configura la URL de la documentación OpenAPI
SWAGGER_URL = "/api/docs"  # Ruta para servir Swagger UI
API_URL = "/static/swagger.json"  # Ruta de tu archivo OpenAPI/Swagger
# Inicializa el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Biblioteca API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bibl.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la base de datos
db.init_app(app)

# Inicializa la extensión JWTManager
jwt = JWTManager(app)
# Registra el blueprint de animales en la aplicación
app.register_blueprint(libro_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)