import mysql.connector

class PokemonManager:
    def __init__(self, host, user, password, database):
        """Constructor: Establece la configuración de conexión"""
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

    def _conectar(self):
        """Método privado para abrir conexión"""
        return mysql.connector.connect(**self.config)

    def obtener_todos(self):
        """READ: Devuelve lista de pokémon"""
        conexion = self._conectar()
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute("SELECT numero_pokedex, nombre FROM pokemon LIMIT 10")
            return cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()

    def insertar_pokemon(self, numero, nombre, peso, altura):
        """CREATE: Inserta un nuevo registro"""
        conexion = self._conectar()
        cursor = conexion.cursor()
        try:
            query = "INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (numero, nombre, peso, altura))
            conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            print(f"Error al insertar: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    def borrar_pokemon(self, numero):
        """DELETE: Borra por número de pokedex"""
        conexion = self._conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM pokemon WHERE numero_pokedex = %s", (numero,))
            conexion.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conexion.close()

# --- PROGRAMA PRINCIPAL (Main) ---
if __name__ == "__main__":
    # Instanciamos la clase
    db = PokemonManager("localhost", "dam2", "asdf.1234", "pokemondb")

    # 1. Probar inserción
    if db.insertar_pokemon(999, "GeminiMon", 10.5, 1.2):
        print("Pokémon insertado con éxito.")

    # 2. Probar lectura
    print("\nLista de Pokémon:")
    for p in db.obtener_todos():
        print(f"#{p['numero_pokedex']} - {p['nombre']}")

    # 3. Probar borrado
    if db.borrar_pokemon(999):
        print("\nPokémon borrado.")