# Reto (Simulación de fallo):
# En la base pokemondb, intenta insertar una nueva forma de aprendizaje
# en la tabla forma_aprendizaje (necesitarás mirar esa tabla en el SQL) y, acto seguido,
# intenta insertar su correspondiente entrada en la tabla MT.
# Condición: Si la inserción en la tabla MT falla (por ejemplo, por una MT con nombre inválido),
# la inserción en forma_aprendizaje no debe quedarse en la base de datos.
# Objetivo: Implementar un rollback real en un bloque except

import mysql.connector


def insertar_mt_con_transaccion():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="dam2",
            password="asdf.1234",
            database="pokemondb"
        )

        if connection.is_connected():
            # Desactivamos el autocommit para controlar nosotros la transacción
            connection.autocommit = False
            cursor = connection.cursor()

            print("--- Iniciando operación transaccional ---")

            # 1. Insertar en 'forma_aprendizaje'
            # (id_forma_aprendizaje es PK, asegúrate de usar uno que no exista, ej: 100)
            query_forma = "INSERT INTO forma_aprendizaje (id_forma_aprendizaje, id_tipo_forma_aprendizaje) VALUES (%s, %s)"
            cursor.execute(query_forma, (100, 1))  # 1 es tipo 'MT'
            print("Paso 1: Forma de aprendizaje preparada...")

            # 2. Insertar en 'MT'
            # Forzamos un error: Supongamos que 'nombre' es un campo que no existe
            # o enviamos un valor nulo en una columna NOT NULL para disparar el EXCEPT
            query_mt = "INSERT INTO mt (id_forma_aprendizaje, MT) VALUES (%s, %s)"

            # Simulamos fallo: Si la columna 'MT' en tu SQL tiene una restricción
            # o simplemente escribimos mal la columna para que salte el error
            cursor.execute(query_mt, (100, None))  # Esto debería fallar si MT no admite nulos

            # 3. Si llega aquí, todo ha ido bien
            connection.commit()
            print("Transacción completada con éxito.")

    except mysql.connector.Error as error:
        # Si algo falla en el paso 1 o 2, venimos aquí
        print(f"Error detectado: {error}")
        if connection:
            connection.rollback()
            print("Refugio seguro: Se ha hecho ROLLBACK. La base de datos no ha cambiado.")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada.")


insertar_mt_con_transaccion()