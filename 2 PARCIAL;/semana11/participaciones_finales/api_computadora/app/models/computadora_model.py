from database import db

class Computadora(db.Model):
    __tablename__ = "computadoras"

    #marca, peso, sabor, origen
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    acesorios = db.Column(db.String(100), nullable=False)

    
    def __init__(self, marca, precio, tipo, acesorios):
        self.marca = marca
        self.precio = precio
        self.tipo = tipo
        self.acesorios = acesorios

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Computadora.query.all()

    @staticmethod
    def get_by_id(id):
        return Computadora.query.get(id)

    def update(self, marca=None, precio=None, sabor=None, origen=None):
        if marca is not None:
            self.marca = marca
        if precio is not None:
            self.peso = precio
        if sabor is not None:
            self.sabor = sabor
        if origen is not None:
            self.origen = origen
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()