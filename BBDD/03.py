import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="dam2",
        passwd="asdf.1234",
        database="pokemondb"
    )

    if conexion.is_connected():
        cursor = conexion.cursor(dictionary=True)  # Usamos diccionario para mayor claridad

        # 1. Pedir datos al usuario
        nuevo_id = int(input("Introduce el ID de la nueva piedra: "))
        nuevo_nombre = input("Introduce el nombre de la piedra: ")

        # 2. COMPROBACIÓN: ¿Existe ya ese ID?
        check_query = "SELECT id_tipo_piedra FROM tipo_piedra WHERE id_tipo_piedra = %s"
        cursor.execute(check_query, (nuevo_id,))

        if cursor.fetchone():
            print(f"Error: El ID {nuevo_id} ya existe en la base de datos.")
        else:
            # 3. INSERCIÓN: Si no existe, insertamos
            insert_query = "INSERT INTO tipo_piedra (id_tipo_piedra, nombre_piedra) VALUES (%s, %s)"
            datos = (nuevo_id, nuevo_nombre)

            cursor.execute(insert_query, datos)

            # ¡IMPORTANTE! Sin esto, los cambios no se guardan permanentemente
            conexion.commit()

            print(f"✅ {nuevo_nombre} añadida correctamente. Filas afectadas: {cursor.rowcount}")

except mysql.connector.Error as error:
    print(f"Error en la base de datos: {error}")
    # Si hay un error crítico, podemos deshacer cambios pendientes
    if conexion:
        conexion.rollback()

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()