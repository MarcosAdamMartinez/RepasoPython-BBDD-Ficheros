import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="dam2",
        password="asdf.1234",
        database="pokemondb"
    )

    if connection.is_connected():
        cursor = connection.cursor()

        id_borrar = input("Introduce el ID de la piedra que quieres eliminar: ")

        # 1. Ejecutamos el DELETE
        # Usamos %s para evitar SQL Injection incluso en borrados
        query = "DELETE FROM tipo_piedra WHERE id_tipo_piedra = %s"
        cursor.execute(query, (id_borrar,))

        # 2. IMPORTANTE: Guardar cambios
        connection.commit()

        # 3. COMPROBACIÓN: ¿Se ha borrado algo?
        # cursor.rowcount devuelve el número de filas afectadas por la última sentencia
        if cursor.rowcount > 0:
            print(f"✅ Éxito: Se han eliminado {cursor.rowcount} registro(s).")
        else:
            print(f"⚠️ No se encontró ninguna piedra con el ID {id_borrar}.")

except mysql.connector.Error as error:
    print(f"Error: {error}")
    connection.rollback() # Si falla el borrado por una FK, deshacemos
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()