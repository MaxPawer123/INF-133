import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")
try: 
    conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla PLATOS ya existe")
try: 
    conn.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla MESAS ya existe")
try: 
    conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
        FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla PEDIDOS ya existe")
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES 
    ('Pizza', 10.99, 'Italiana'),
    ('Hamburguesa', 8.99, 'Americana'),
    ('Sushi', 12.99, 'Japonesa'),
    ('Ensalada', 6.99, 'Vegetariana')
    """
)

conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES 
    (1),
    (2),
    (3),
    (4)
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES 
    (1, 2, 2, '2024-04-01'),
    (2, 3, 1, '2024-04-01'),
    (3, 1, 3, '2024-04-02'),
    (4, 4, 1, '2024-04-02')
    """
)

print("\nPLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
print("\nMESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)
    
print("\nPEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)
    
# Actualiza el precio del plato con id 2 (Hamburguesa) a 9.99
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)
print("\nPLATOS ACTUALIZADO:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# ● Cambia la categoría del plato con id 3 (Sushi) a "Fusión"
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusión'
    WHERE id = 3
    """
)
print("\nPLATOS CAMBIA:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)


# ● Elimina el pedido con id 3
conn.execute(
    """
    DELETE FROM PEDIDOs
    WHERE id = 3
    """
)
print("\nPEDIDOS ELIMINADO ID3:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)
    


    
#Encuentra todos los pedidos realizados junto con los nombres de los #platos y los números de mesa (JOIN)
#Encuentra todos los platos que han sido pedidos, incluso aquellos #que no se han pedido aún (LEFT JOIN)

conn.commit()
conn.close()