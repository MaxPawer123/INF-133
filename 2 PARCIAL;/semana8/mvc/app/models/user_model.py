from database import db
# `db.Model` es una clase base para todos los modelos de SQLAlchemy
# Define la clase `User` que hereda de `db.Model`
# `User` representa la tabla `users` en la base de datos
#Son la representacion de una bd
class User(db.Model):
    __tablename__ = 'users'
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False) #nombre
    last_name = db.Column(db.String(50), nullable=False) #apellido
    email = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)  # Cambio aquí

    # Inicializa la clase `User`
    def __init__(self, first_name, last_name,email,contraseña,fecha_nacimiento):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contraseña = contraseña
        self.fecha_nacimiento = fecha_nacimiento  # Asignación aquí


    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit() # lo guarda
    #La forma que se consulta la informacion
    # Obtiene todos los usuarios de la base de datos
    @staticmethod
    def get_all():
        return User.query.all()