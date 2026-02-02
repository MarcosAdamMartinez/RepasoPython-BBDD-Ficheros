import mysql.connector

def menu():
    print("\n--- CRUD POKEMON DB (Tipo Piedra) ---")
    print("1. Ver todas las piedras")
    print("2. Añadir nueva piedra")
    print("3. Actualizar nombre de piedra")
    print("4. Eliminar piedra")
    print("5. Salir")
    return input("Elige una opción: ")

def ejecutar_crud():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="dam2",
            password="asdf.1234",
            database="pokemondb"
        )
        cursor = conexion.cursor(dictionary=True)

        while True:
            opcion = menu()

            if opcion == '1': # READ
                cursor.execute("SELECT * FROM tipo_piedra")
                piedras = cursor.fetchall()
                print("\nLISTADO DE PIEDRAS:")
                for p in piedras:
                    print(f"ID: {p['id_tipo_piedra']} | Nombre: {p['nombre_piedra']}")

            elif opcion == '2': # CREATE
                id_p = input("ID de la piedra: ")
                nom = input("Nombre de la piedra: ")
                query = "INSERT INTO tipo_piedra (id_tipo_piedra, nombre_piedra) VALUES (%s, %s)"
                cursor.execute(query, (id_p, nom))
                conexion.commit()
                print("✅ Piedra añadida.")

            elif opcion == '3': # UPDATE
                id_p = input("ID de la piedra a modificar: ")
                nuevo_nom = input("Nuevo nombre: ")
                query = "UPDATE tipo_piedra SET nombre_piedra = %s WHERE id_tipo_piedra = %s"
                cursor.execute(query, (nuevo_nom, id_p))
                conexion.commit()
                if cursor.rowcount > 0:
                    print("✅ Nombre actualizado.")
                else:
                    print("⚠️ No se encontró ese ID.")

            elif opcion == '4': # DELETE
                id_p = input("ID de la piedra a eliminar: ")
                query = "DELETE FROM tipo_piedra WHERE id_tipo_piedra = %s"
                cursor.execute(query, (id_p,))
                conexion.commit()
                if cursor.rowcount > 0:
                    print("✅ Piedra eliminada.")
                else:
                    print("⚠️ No existe ese ID.")

            elif opcion == '5':
                break
            else:
                print("Opción no válida.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada. ¡Suerte en el examen!")

if __name__ == "__main__":
    ejecutar_crud()