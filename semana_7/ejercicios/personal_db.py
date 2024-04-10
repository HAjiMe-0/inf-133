import sqlite3

conn = sqlite3.connect("personal.db")

conn.execute(
    """
    CREATE TABLE DEPARTAMENTO
    (id INTERGER,
    nombre TEXT NOT NULL,
    fechas_creacion TEXT NOT NULL
    );
    """
)

conn.execute(
    """
    INSERT INTO DEPARTAMENTO( nombre, fechas_creacion)
    VALUES ('Ventas', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTO(nombre, fechas_creacion)
    VALUES ( 'Markeitng', '11-04-2020')
    """
)
#crear tablas de salarios
conn.execute(
    """
    CREATE TABLE SALARIOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    salario REAL NOT NULL,
    fecha_init date NOT NULL,
    fecha_fin date NOT NULL,
    fecha_create text NOT NULL);
    """)


#crear tablas de empleados
conn.execute(
    """
    CREATE TABLE EMPLEADOS 
    (id_empleado INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido_materno TEXT NOT NULL,
    apellido_paterno TEXT NOT NULL,
    fecha_de_contratacion DATE NOT NULL,
    departamento_id INTERGEER NOT NULL,
    cargo_id INTERGER NOT NULL,
    fecha_de_creacion TEXT NOT NULL);
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS(id_empleado,nombre,apellido_materno,apellido_paterno,fecha_de_contratacion,departamento_id,cargo_id,fecha_de_creacion)
    VALUES (1,'Juan','Gonzales','perez','15-05-23','Ventas','Gerente de ventas','15-05-23')
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS(id_empleado,nombre, apellido_materno,apellido_paterno,fecha_de_contratacion,departamento_id,cargo_id,fecha_de_creacion)
    VALUES (2,'Maria','Lopez','Martinez','20-06-23','Marketing','Analisis de Marketing','20-06-23')
    """
)


conn.execute(
    """
    CREATE TABLE CARGOS
    (id INTERGER ,
    nombre TEXT NOT NULL,
    nivel TEXT NOT NULL,
    fechas_creacion TEXT NOT NULL
    );
    """
)
conn.execute(
    """
    INSERT INTO CARGOS( nombre,nivel, fechas_creacion)
    VALUES ( 'Gerente de ventas','Senior', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS( nombre,nivel, fechas_creacion)
    VALUES ('Analisis de marketing','Junior', '11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS( nombre,nivel, fechas_creacion)
    VALUES ('Representantes de ventas','Junior', '12-04-2020')
    """
)

conn.commit()
