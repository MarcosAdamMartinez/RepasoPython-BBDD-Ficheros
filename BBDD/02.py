# Reto: Crea una función en Python que reciba el nombre de un artista
# (ej. "AC/DC") y devuelva todos los títulos de sus álbumes consultando las tablas Artist y Album.
# Pista: Necesitarás un JOIN entre Artist.ArtistId y Album.ArtistId.
# Objetivo: Practicar JOINs y paso de parámetros seguros

import mysql.connector

def buscar_album(nombre):
    conexion = None

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="dam2",
            password="asdf.1234",
            database="chinook"
        )

        if conexion.is_connected():
            cursor = conexion.cursor()

            query = "SELECT Album.title FROM Album JOIN Artist ON Album.ArtistId = Artist.ArtistId WHERE Artist.name = %s"

            cursor.execute(query, (nombre,))

            resultados = cursor.fetchall()

            if (resultados):
                print(f"Albumes de {nombre}:")
                for fila in resultados:
                    print(f"- {fila[0]}")
            else:
                print(f"No hay albumes de {nombre}")


    except mysql.connector.Error as error:
        print(error)
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

buscar_album("AC/DC")