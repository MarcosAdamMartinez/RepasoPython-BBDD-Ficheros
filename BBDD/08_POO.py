import mysql.connector


# 1. LA MAQUETA (Clase de objeto puro)
class Piedra:
    def __init__(self, id_piedra, nombre):
        self.id = id_piedra
        self.nombre = nombre

    def __str__(self):
        return f"OBJETO PIEDRA -> ID: {self.id}, Nombre: {self.nombre}"


# 2. EL REPOSITORY / DAO (La persistencia)
class PiedraRepository:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'dam2',
            'password': 'asdf.1234',
            'database': 'pokemondb'
        }

    def obtener_todas(self):
        """Mapea las filas de la BD a una lista de objetos Piedra"""
        objetos_piedra = []
        conn = mysql.connector.connect(**self.config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT id_tipo_piedra, nombre_piedra FROM tipo_piedra")

        for fila in cursor.fetchall():
            # Creamos el objeto con los datos de la fila
            nuevo_obj = Piedra(fila['id_tipo_piedra'], fila['nombre_piedra'])
            objetos_piedra.append(nuevo_obj)

        cursor.close()
        conn.close()
        return objetos_piedra

    def guardar(self, piedra_obj):
        """Recibe un objeto y lo guarda en la base de datos"""
        conn = mysql.connector.connect(**self.config)
        cursor = conn.cursor()

        query = "INSERT INTO tipo_piedra (id_tipo_piedra, nombre_piedra) VALUES (%s, %s)"
        cursor.execute(query, (piedra_obj.id, piedra_obj.nombre))

        conn.commit()
        cursor.close()
        conn.close()


# 3. PRUEBA DE FUNCIONAMIENTO (Ctrl+C y Ctrl+V)
if __name__ == "__main__":
    repo = PiedraRepository()

    # EJEMPLO: Crear un objeto y persistirlo (Como en Java)
    nueva_piedra = Piedra(10, "Piedra DAM")
    try:
        repo.guardar(nueva_piedra)
        print(f"✅ Se ha guardado el objeto: {nueva_piedra.nombre}")
    except Exception as e:
        print(f"❌ No se pudo guardar (quizás el ID ya existe): {e}")

    # EJEMPLO: Traer todo de la BD y manejarlo como objetos
    print("\n--- LISTA DE OBJETOS RECUPERADOS ---")
    mis_piedras = repo.obtener_todas()

    for p in mis_piedras:
        # Aquí 'p' no es una tupla, es un objeto de la clase Piedra
        print(p)
        print(f"Accediendo al atributo nombre directamente: {p.nombre}")