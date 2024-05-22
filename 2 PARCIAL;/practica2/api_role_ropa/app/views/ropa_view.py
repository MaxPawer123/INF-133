def render_ropa_list(ropas):
    # Representa una lista de animales como una lista de diccionarios
    return [
        {
            "id": ropa.id,
            "color": ropa.color,
            "talla": ropa.talla,
            "tipo_tela": ropa.tipo_tela,
            "genero": ropa.genero,
            "stock": ropa.stock,
            "tipo": ropa.tipo,
            "descuento": ropa.descuento,
        }
        for ropa in ropas
    ]


def render_ropa_detail(ropa):
    # Representa los detalles de un animal como un diccionario
    return {
        "id": ropa.id,
        "color": ropa.color,
        "talla": ropa.talla,
        "tipo_tela": ropa.tipo_tela,
        "genero": ropa.genero,
        "stock": ropa.stock,
        "tipo": ropa.tipo,
        "descuento": ropa.descuento,
    }
