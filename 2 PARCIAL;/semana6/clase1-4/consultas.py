# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

#Encuentra todos los pedidos realizados junto con los nombres de los #platos y los números de mesa (JOIN)

print("\PEDIDOS JOIN:")
cursor = conn.execute(
    """
    SELECT  PLATOS.nombre, MESAS.numero
    FROM PEDIDOS
    JOIN PLATOS ON PLATOS.id = PEDIDOS.plato_id
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id;
    """
)
for row in cursor:
    print(row)

#Encuentra todos los platos que han sido pedidos, incluso aquellos #que no se han pedido aún (LEFT JOIN)
print("\PEDIDOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT PLATOS.id, PLATOS.nombre, PLATOS.precio,PEDIDOS.id
    FROM PLATOS
    LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id;
    """
    
)
for row in cursor:
    print(row)
    
    
    
    
    
    