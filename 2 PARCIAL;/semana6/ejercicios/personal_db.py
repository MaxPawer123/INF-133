
import sqlite3

conn = sqlite3.connect('personal.db')

cursor = conn.cursor()

try:
    conn.execute(
        '''CREATE TABLE DEPARTAMENTOS (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL
        )'''
    )
except sqlite3.OperationalError:
    print("La tabla Departamentos ya existe")

try:
    cursor.execute('''CREATE TABLE CARGOS (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    nivel TEXT NOT NULL,
                    fecha_creacion TEXT NOT NULL
                )''')
except sqlite3.OperationalError:
    print("La tabla de cargos ya existe")

try:
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLEADOS (
                    id INTEGER PRIMARY KEY,
                    nombres TEXT NOT NULL,
                    apellido_paterno TEXT NOT NULL,
                    apellido_materno TEXT NOT NULL,
                    fecha_contratacion DATE NOT NULL,
                    departamento_id INTEGER NOT NULL,
                    cargo_id INTEGER NOT NULL,
                    fecha_creacion TEXT NOT NULL,
                    FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
                    FOREIGN KEY (cargo_id) REFERENCES CARGOS(id)
                )''')
except sqlite3.OperationalError:
    print("la tabla enpleados ya existe")

try:
    cursor.execute('''CREATE TABLE SALARIOS (
                    id INTEGER PRIMARY KEY,
                    empleado_id INTEGER NOT NULL,
                    salario REAL NOT NULL,
                    fecha_inicio DATE NOT NULL,
                    fecha_fin DATE NOT NULL,
                    fecha_creacion TEXT NOT NULL,
                    FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id)
                )''')
except sqlite3.OperationalError:
    print("La tabla de salarios ya existe")


# Insertar datos de departamentos
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Ventas', '10-04-2020'), ('Marketing', '11-04-2020')
    """
)
#Insertar datos de cargos
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES('Gerente de Ventas', 'Senior', '10-04-2020'), ('Analista de Marketing', 'Junior', '11-04-2020'), ('Representante de Ventas', 'Junior', '12-04-2020')
    """
)

##Crea dos nuevos empleados
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES('Juan', 'Gonzáles', 'Pérez', '15-05-2023', 1, 1, '15-05-2023'),
            ('María', 'López', 'Martínez', '20-06-2023', 2, 2, '20-06-2023')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
    VALUES(1,3000,'01-04-2024','30-04-2025','01-04-2024'),
            (2,3500,'01-07-2023','30-04-2024','01-07-2023')
    
    """
)

# Lista los empleados y sus salarios
cursor.execute('''SELECT e.nombres, e.apellido_paterno, e.apellido_materno, s.salario
                  FROM EMPLEADOS e
                  INNER JOIN SALARIOS s ON e.id = s.empleado_id''')
print("-----EMPLEADOS ------")
for row in cursor:
    print(row)

# Lista los empleados, el departamento en el que trabajan y el cargo que ocupan y el salario que ganan
cursor.execute('''SELECT e.nombres, e.apellido_paterno, e.apellido_materno, d.nombre AS departamento, c.nombre AS cargo
                  FROM EMPLEADOS e
                  INNER JOIN DEPARTAMENTOS d ON e.departamento_id = d.id
                  INNER JOIN CARGOS c ON e.cargo_id = c.id''')

print("------ Empleados, departamento y cargo  ------")
for row in cursor:
    print(row)


                 
# Lista los empleados, el departamento en el que trabajan, el cargo que ocupan y el salario que ganan
cursor.execute(
    """
    SELECT e.*, d.nombre, c.nombre, s.salario
    FROM EMPLEADOS e
    INNER JOIN DEPARTAMENTOS d ON e.departamento_id = d.id
    INNER JOIN CARGOS c ON e.cargo_id = c.id
    INNER JOIN SALARIOS s ON e.id = s.empleado_id
    """)

print("------ Empleados, departamento y cargo  ------")
for row in cursor:
    print(row)

# Actualizar el precio del plato id 2
conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = 3
    WHERE id = 2
    """
)

conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE empleado_id = 2
    """
)

cursor.execute(
    """
    SELECT e.*, d.nombre, c.nombre, s.salario
    FROM EMPLEADOS e
    INNER JOIN DEPARTAMENTOS d ON e.departamento_id = d.id
    INNER JOIN CARGOS c ON e.cargo_id = c.id
    INNER JOIN SALARIOS s ON e.id = s.empleado_id
    """)

print("------ Empleados, departamento y cargo  ------")
for row in cursor:
    print(row)

print("----------------------------")


cursor.execute(
    """ 
    DELETE 
    FROM EMPLEADOS
    WHERE id = 2 
    """
)
cursor.execute(
    """ 
    DELETE 
    FROM SALARIOS
    WHERE id = 2 
    """
)

print("--INSERTAR ")

conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES('Carlos', 'Sanchez', 'Rodriguez', '09-04-2024', 1, 3, '09-04-2024')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
    VALUES(2,3500,'05-05-2023','05-12-2024','05-05-2023')
    
    """
)

# Lista los empleados, el departamento en el que trabajan, el cargo que ocupan y el salario que ganan
cursor.execute(
    """
    SELECT e.*, d.nombre, c.nombre, s.salario
    FROM EMPLEADOS e
    INNER JOIN DEPARTAMENTOS d ON e.departamento_id = d.id
    INNER JOIN CARGOS c ON e.cargo_id = c.id
    INNER JOIN SALARIOS s ON e.id = s.empleado_id
    """)
for row in cursor:
    print(row)
    
    
conn.commit()
conn.close()

