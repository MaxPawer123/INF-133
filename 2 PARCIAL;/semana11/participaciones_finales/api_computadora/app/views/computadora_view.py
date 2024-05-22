def render_computadora_list(computadoras):    
    return [
        {
            "id": computadora.id,
            "marca": computadora.marca,
            "precio": computadora.precio,
            "tipo": computadora.tipo,
            "acesorios": computadora.acesorios
        }
        for computadora in computadoras
    ]


def render_computadora_detail(computadora):
    return {
            "id": computadora.id,
            "marca": computadora.marca,
            "precio": computadora.precio,
            "tipo": computadora.tipo,
            "acesorios": computadora.acesorios
    }