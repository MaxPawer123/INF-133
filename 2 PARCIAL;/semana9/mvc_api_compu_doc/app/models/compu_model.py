from database import db

class Libro(db.Model):
    __tablename__ = "libros"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    tamano = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)

    def __init__(self, nombre, marca, tamano, cantidad):
        self.nombre = nombre
        self.marca = marca
        self.tamano = tamano
        self.disponibilidad = disponibilidad

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Libro.query.all()

    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)

    def update(self, autor=None, titulo=None, edicion=None, disponibilidad=None):
        if autor is not None:
            self.autor = autor
        if titulo is not None:
            self.titulo = titulo
        if edicion is not None:
            self.edicion = edicion
        if disponibilidad is not None:
            self.disponibilidad = disponibilidad
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()