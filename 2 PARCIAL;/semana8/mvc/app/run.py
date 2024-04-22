from flask import Flask
# Importamos el controlador de usuarios
from controllers import user_controller
# Importamos la base de datos
from database import db 

# Inicializa la aplicación Flask
app = Flask(__name__) # el app es un objeto
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # ese si o si el nombre
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializa `db` con la aplicación Flask
db.init_app(app)  
# Registra el Blueprint de usuarios
app.register_blueprint(user_controller.user_bp)

if __name__ == '__main__':
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all() #intenta crear todas las tablas y recien se levanta el servidor 
    app.run(debug=True)