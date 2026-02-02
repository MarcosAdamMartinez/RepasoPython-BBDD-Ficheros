# Reto: Conéctate a la base de datos pokemondb y muestra por consola el nombre de todos
# los efectos secundarios que existen en la tabla efecto_secundario.
# Objetivo: Probar la conexión y el uso de cursor.fetchall()
import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="dam2",
        passwd="asdf.1234",
        database="pokemondb")

    if conexion.is_connected():
        cursor = conexion.cursor()

        query = "SELECT efecto_secundario FROM efecto_secundario"

        cursor.execute(query)

        for row in cursor:
            print(row[0])


except mysql.connector.Error as error:
    print(error)