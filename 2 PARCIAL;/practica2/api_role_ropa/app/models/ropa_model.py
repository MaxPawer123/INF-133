from database import db


# Define la clase `Animal` que hereda de `db.Model`
# `Animal` representa la tabla `animals` en la base de datos
class Ropa(db.Model):
    __tablename__ = "ropa"

    # Define las columnas de la tabla `animals`
    id = db.Column(db.Integer, primary_key=True)
    color=db.Column(db.String(100), nullable=False)
    talla = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)    
    tipo_tela = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    descuuento = db.Column(db.Boolean(100), nullable=False)
    
    
    # Inicializa la clase `Animal`
    def __init__(self, talla, color,precio, tipo_tela,genero,stock,tipo,descuento):
        self.talla = talla
        self.color=color
        self.precio = precio
        self.tipo_tela = tipo_tela
        self.genero = genero
        self.stock=stock
        self.tipo=tipo
        self.descuento=descuento


    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Ropa.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Ropa.query.get(id)

    # Actualiza un ropa en la base de datos
    def update(self, talla=None, precio=None, tipo_tela=None,genero=None,stock=None,tipo=None,descuento=None):
        if talla is not None:
            self.talla = talla
        if precio is not None:
            self.precio = precio
        if tipo_tela is not None:
            self.tipo_tela = tipo_tela
        if genero is not None:
            self.genero = genero
        if stock is not None:
            self.stock = stock
        if tipo is not None:
            self.tipo = tipo
        if descuento is not None:
            self.descuento = descuento
        
        
        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
