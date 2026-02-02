import re, random, pickle, os

# EXTRA


def grabarEmpleado(fichero, empleado):
    empleados = []

    # Si el fichero existe, leerlo
    if os.path.exists(fichero):
        try:
            with open(fichero, "rb") as f:
                empleados = pickle.load(f)
        except EOFError:
            empleados = []

    # Añadir el nuevo empleado
    empleados.append(empleado)

    # Guardar de nuevo
    with open(fichero, "wb") as f:
        pickle.dump(empleados, f)

    # Listar empleados
    print("Listado de empleados:")
    for e in empleados:
        print(f"{e.nombre} {e.apellidos} ({e.edad})")


# 1. Crea una función en python que se llame compararFicheros y que reciba como argumento el
# nombre de dos ficheros de texto. La función debería de devolver un valor booleano indicando
# si el contenido de ambos ficheros es exactamente el mismo o no.

def compararFicheros(nameFile1, nameFile2):
    file1 = open(nameFile1, 'r')
    file2 = open(nameFile2, 'r')

    if(file1.read() == file2.read()):
        return True
    else:
        return False

# 2. Tenemos un fichero llamado estadisticas.txt. El formato del fichero es el siguiente (pero el
# contenido puede variar, lógicamente):

file1 = open("./File/estadisticas.txt", "r")

countMujer = 0
countHombre = 0
media = list()

regex = r"^[1-9]+.[1-9]+"

for fileVar in file1.readlines():
    if "Mujer" in fileVar:
        countMujer += 1
    elif "Hombre" in fileVar:
        countHombre += 1
    elif re.match(regex, fileVar):
        media.append(float(fileVar))


print("Numero Hombres: ", countHombre)
print("Numero Mujeres: ", countMujer)
print("Media aritmetica: ", round(sum(media) / len(media), 2))

# 3. Un código bancario en formato IBAN en nuestro país está formado por 24 caracteres de los
# cuales los dos primeros son letras y los restantes 22 son dígitos númericos comprendidos entre el 0
# y el 9. Por ejemplo, el siguiente sería un IBAN válido

print("Ejercicio 3")

def validarIbanArchivo(nameFile="default"):
    file = open("./File/codigos.txt", 'r')
    correctos = 0
    incorrectos = 0
    regex = r"^[A-Z]{2}(?:\s?\d{2}){11}$"

    for i in file.readlines():
        if(re.match(regex, i)):
            correctos += 1
            print("País:", i[0:2])
            print("DC:", i[2:4])
            print("Entidad:", i[4:8])
            print("Sucursal:", i[8:12])
            print("DC cuenta:", i[12:14])
            print("Número de cuenta:", i[14:24])
        else:
            incorrectos += 1

    print(f"Hay {correctos} códigos correctos y {incorrectos} incorrectos")

validarIbanArchivo("./File/codigos.txt")

# 4. Escribe un programa usando POO que, tomando el mismo fichero codigos.txt del ejercicio 3,
# tenga una clase que se llame IBAN donde guarde la información de los códigos IBAN correctos que
# se hayan leído del fichero.

print("Ejercicio 4")
class IBAN:
    def __init__(self, codigo):
        self.codigo = codigo

        if not re.match(r"^[A-Z]{2}[0-9]{22}$", codigo):
            raise ValueError("IBAN inválido")

        self.pais = codigo[0:2]
        self.dc = codigo[2:4]
        self.entidad = codigo[4:8]
        self.sucursal = codigo[8:12]
        self.dc_cuenta = codigo[12:14]
        self.num_cuenta = codigo[14:24]

        def mostrar(self):
            print("País:", self.pais)
            print("DC:", self.dc)
            print("Entidad:", self.entidad)
            print("Sucursal:", self.sucursal)
            print("DC cuenta:", self.dc_cuenta)
            print("Número de cuenta:", self.num_cuenta)


def procesarIBAN_POO(fichero):

    correctos = 0
    incorrectos = 0

    print(f"Códigos correctos en el fichero {fichero}:")

    with open(fichero, "r") as f:
        for linea in f:
            try:
                iban = IBAN(linea.strip())
                iban.mostrar()
                correctos += 1
            except:
                incorrectos += 1

    print(f"Hay {correctos} códigos correctos y {incorrectos} incorrectos")

procesarIBAN_POO("./File/codigos.txt")


#5. En los centros de datos es normal anonimizar de alguna forma los ficheros de clientes para poder
# hacer pruebas con ellos sin vulnerar las leyes de protección de datos. Una de las formas mas
# utilizadas es “barajar” los datos de los clientes originales. Imagina que el fichero de clientes de tu
# empresa es el siguiente:

def validarDatos(nameFile="default"):
    file = open(nameFile, "r")

    nombres = []
    apellidos = []
    dnis = []
    for i in file.readlines():
        nombre, apellido, dni = i.strip().split(" ")
        nombres.append(nombre)
        apellidos.append(apellido)
        dnis.append(dni)

    random.shuffle(nombres)
    random.shuffle(apellidos)
    random.shuffle(dnis)

    file1 = open(nameFile, 'w')

    for i in range(len(nombres)):
        file1.write(f"{nombres[i]} {apellidos[i]} {dnis[i]}\n")


validarDatos("./File/clientes.txt")


# 6. Escribe un programa usando POO que, tomando el mismo fichero clientes.txt del ejercicio
# anterior, tenga una clase que se llame cliente donde guarde la información de los clientes que se
# hayan leído del fichero.

class Cliente:
    def __init__(self,linea):
        partes = linea.strip().split(" ")
        self.nombre = partes[0]
        self.apellido = partes[1]
        self.dni = partes[2]

    def mostrar(self):
        print(f"{self.dni} – {self.apellido}, {self.nombre}")

def mostrarClientes():
    file1 = open("./File/clientes.txt", "r")
    clientes = []

    for i in file1.readlines():
        cliente = Cliente(i)
        clientes.append(cliente)

    for i in clientes:
        i.mostrar()


# 7. Te ha contratado la policía nacional para que hagas un programa que permita ver si un ciudadano
# tiene ficha por delitos previos y mostrar los resultados. El archivo de la policía se llama
# delincuentes.txt y tiene este formato:

def mostrarDelincuentes():
    file1 = open("./File/delincuentes.txt", "r")
    for i in file1.readlines():
        delincuentes = i.strip().split(" ")

        print(delincuentes[0])


mostrarDelincuentes()


# 10. Sabrás, por el módulo de Redes, que las redes de Clase A tienen máscara /8, las clase B
# máscara /16 y las clase C /24. Tenemos un fichero llamado redes.txt con el siguiente formato:

print("Ejercicio 10")
def validarRedes():
    file = open("./File/redes.txt", "r")
    for i in file.readlines():
        mascara = int(i.split("/")[1].strip())
        if(mascara == 8):
            print("Clase A: ", i)
        elif(mascara == 16):
            print("Clase B: ", i)
        elif (mascara == 24):
            print("Clase C: ", i)

validarRedes()


# 11. Tenemos un fichero cuyo formato es el siguiente (pero el contenido puede variar, lógicamente):
# 1234.5
# 725.3
# pepe
# 4.37
# 12
# ani33kk
# 1285.3
# Realiza una función que reciba como argumento el nombre del fichero. Tu función debe de leer el
# contenido y mostrarnos una salida como esta (para el anterior fichero):

print("Ejercicio 11")

def validarSalida(nameFile="default"):
    file = open(nameFile, "r")

    correctos = 0
    incorectos = 0
    regex = r"[0-9]+.[0-9]+"
    regex1 = r"[0-9]+"

    numeros = []
    for i in file.readlines():


        if re.match(regex, i) or re.match(regex, regex1):
            correctos += 1
            numeros.append(float(i))
        else:
            incorectos += 1

    print("Correctos: ", correctos)
    print("Incorrectos: ", incorectos)
    print("Minimo: ", min(numeros))
    print("Maximo: ", max(numeros))
    print("Media aritmetica: ", sum(numeros) / len(numeros))
validarSalida("./File/Numeros.txt")


# 12. Queremos hacer un programa en python que sirva para evaluar los resultados de un test. El
# fichero manejará dos ficheros: uno llamado soluciones.txt y otro llamado respuestas.txt
# El fichero llamado soluciones.txt tiene esta estructura:
# A, C, C, D, B, A, D, A, B, A

print("Ejercicio 12 DIFICIL")

def validarNotas():
    respuestas = open("./File/respuestas.txt", "r")
    soluciones = open("./File/solutions.txt", "r")

    aciertos = 0

    while True:
        # Leer una línea de cada archivo
        linea_sol = soluciones.readline()
        linea_resp = respuestas.readline()

        # Salir si llegamos al final de alguno de los archivos
        if not linea_sol or not linea_resp:
            break

        # Limpiar espacios y separar por palabras
        solucion = linea_sol.strip().split(" ")
        respuesta = linea_resp.strip().split(" ")

        # Comparar listas completas
        if respuesta == solucion:
            aciertos += 1

    # Cerrar los archivos
    respuestas.close()
    soluciones.close()

    print("Correctos:", aciertos)

validarNotas()


# 13. Escribe un programa en python para desarrollar una función de login con las siguientes
# características:
# - Los usuarios y contraseñas válidos estarán almacenados en un fichero con la sintaxis
# usuario:contraseña. Suponemos que el fichero es correcto y no habrá errores en su formato.
# Tampoco puede haber usuarios repetidos. Un ejemplo de fichero podría ser este:

print("Ejercicio 13")

def contrasenas(fichero="default"):
    try:
        contra = open(fichero, "r")
    except:
        print("Fichero inexistente o imposible de acceder")
        return

    lineas = contra.readlines()
    contra.close()

    if not lineas:
        print("Fichero vacío")
        return

    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contrasena: ")

    encontrado = False
    for i in lineas:
        login = i.strip().split(":")
        if usuario == login[0]:
            encontrado = True
            if contrasena == login[1]:
                print("Contrasena correcta")
            else:
                print("Contrasena incorrecta")
            break
    if not encontrado:
        print("Usuario no encontrado")


contrasenas("./File/login.txt")


print("Ejercicio 14")

def contrasenaGuardar(file="default"):
    try:
        archivo = open(file, "a")
    except:
        print("Fichero inexistente o imposible de acceder")
        return


    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contrasena: ")
    contrasena2 = input("Ingrese su contrasena2: ")

    if contrasena == contrasena2:
        archivo.write(usuario + ":" + contrasena + "\n")
        print("Cuenta de usuario grabada correctamente")
    else:
        print("Las contraseñas no son iguales. No se puede grabar la nueva cuenta")

contrasenaGuardar("./File/login.txt")


#15. Haz un programa en Python que convierta las parejas usuario:password en objetos de una
#clase Consideraciones a tener en cuenta:

print("Ejercicio 15")

class User:
    def __init__(self, linea):
        self.usuario, self.contrasena = linea.strip().split(":")




    def fortaleza(self):
        puntuacion = 0
        pwd = self.contrasena

        if len(pwd) > 8:
                puntuacion += 1

        if any(c.isalpha() for c in pwd):
            puntuacion += 1

        if any(c.islower() for c in pwd) and any(c.isupper() for c in pwd):
            puntuacion += 1

        if any(c.isdigit() for c in pwd):
            puntuacion += 1

        if any(not c.isalnum() for c in pwd):
            puntuacion += 1

        return puntuacion

    def mostrar(self):
        print(f"Usuario: {self.usuario}")
        print(f"Contraseña: {self.contrasena}")
        print(f"Fortaleza de la contra: {self.fortaleza()}")


def validarUsuario():
    usuario1 = User("josemaria:abc")

    usuario1.mostrar()

validarUsuario()

print("Ejercicio 16")

# 16. Haz un programa en Python que haga lo siguiente:
# - Lea del fichero del ejercicio 11 y convierta las parejas usuario:contraseña en objetos de una
# clase
# - Grabe los objetos en un fichero binario que se llame login.bin
# - Lea del fichero binario que has escrito y muestre el contenido de los objetos por consola
# Tú programa debería de funcionar independientemente del número de elementos que haya en
# el fichero, tanto a la hora de grabarlo en disco como de leerlo posteriormente.

# ----- LEER TEXTO -----
def leer_fichero_texto(ruta):
    usuarios = []
    with open(ruta, "r") as f:
        for linea in f:
            if linea.strip():
                usuarios.append(User(linea))
    return usuarios


# ----- GUARDAR BINARIO -----
def guardar_binario(usuarios, fichero):
    with open(fichero, "wb") as f:
        pickle.dump(usuarios, f)


# ----- LEER BINARIO -----
def leer_binario(fichero):
    with open(fichero, "rb") as f:
        return pickle.load(f)


# ----- PROGRAMA PRINCIPAL -----
def main():
    fichero_origen = "/home/josemaria/login.txt"
    fichero_destino = "login.bin"

    print(f"Fichero origen: {fichero_origen}")
    print(f"Fichero destino: {fichero_destino}")

    usuarios = leer_fichero_texto(fichero_origen)

    print(f"Número de cuentas encontradas: {len(usuarios)}")
    print("Listado de cuentas:")

    guardar_binario(usuarios, fichero_destino)

    usuarios_bin = leer_binario(fichero_destino)

    for u in usuarios_bin:
        u.mostrar()
        print()


main()

#

print("Ejercicio 17")

# 17. Queremos hacer un programa en Python que revise que la sintaxis de un archivo es
# correcta. El fichero debería de tener una estructura como la que sigue:
# Imedio, Demetrio;Programador Categoría 2;1599.56
# Borriquero, Luis Ricardo;Analista;1341.60
# Lorin, Francisco;Administrativo;1095
# Cortada del Rosal, Rosa;Administrador de bases de datos;2256.99


# POR REVISAR JODIDO

origen = "/home/josemaria/origen.txt"
destino = "/home/josemaria/salida.txt"

with open(origen, "r", encoding="utf-8") as f_origen, open(destino, "w", encoding="utf-8") as f_destino:
    for num, linea in enumerate(f_origen, 1):
        linea = linea.strip()
        partes = linea.split(";")
        if len(partes) != 3 or ", " not in partes[0]:
            print(f"Línea errónea {num}: {linea}")
            continue

        apellidos, nombre = partes[0].split(", ")
        puesto, salario = partes[1], partes[2]

        valido = True
        for palabra in apellidos.split() + nombre.split():
            if not palabra.isalpha():
                valido = False
                break
        for c in puesto:
            if not (c.isalnum() or c == " "):
                valido = False
                break
        try:
            float(salario)
        except:
            valido = False

        if valido:
            f_destino.write(linea + "\n")
        else:
            print(f"Línea errónea {num}: {linea}")

print("Ejercicio 18")

# 18. Queremos añadir al fichero del ejercicio anterior un cuarto campo que sea la edad del
# trabajador. Tu programa deberá de mostrar el nombre de cada persona del fichero pero no
# como aparece en él, sino poniendo antes el nombre y a continuación los apellidos) y
# preguntarnos la edad que introduciremos por teclado. Un ejemplo de ejecución partiendo del
# fichero anterior sería como sigue:


# 19. Vamos a hacer ahora a crear un programa con una clase que se llame Empleado y que
# contenga los siguientes atributos:
# - nombre
# - apellidos
# - cargo
# - salario
# - edad
# Tú clase recibirá en el constructor una línea como la escrita en el fichero anterior. Así, por
# ejemplo:
# Empleado(“Imedio, Demetrio;Programador Categoría 2;1599.56;34”)
# Deberás, además, crear una función llamada mostrar que muestre la siguiente salida:
# Empleado: Demetrio Imedio
# Cargo: Programador Categoría 2
# Años hasta su jubilación ordinaria: 33
# Salario neto anual: 22393.84
# Sabiendo que la jubilación ordinaria se produce a los 67 años y que el salario neto anual se
# calcula multiplicando el salario mensual por 14 pagas que recibe el empleado al año

print("Ejercicio 19")

class Empleado:
    def __init__(self, linea):
        partes = linea.strip().split(";")
        nombre_apellido = partes[0].split(",")
        self.apellido = nombre_apellido[0].strip()
        self.nombre = nombre_apellido[1].strip()
        self.cargo = partes[1]
        self.salario = partes[2]
        self.edad = partes[3]

    def mostrar(self):
        return (
            f"Empleado: {self.nombre}\n"
            f"Cargo: {self.cargo}\n"
            f"Años hasta su jubilación ordinaria: {self.edad}\n"
            f"Salario neto anual: {self.salario}\n"
        )


def escribirDatos():
    with open("./Ejercicio19.txt", "w") as file:
        empleado1 = Empleado("Imedio, Demetrio;Programador Categoría 2;1599.56;34")
        file.write(empleado1.mostrar())

escribirDatos()


# 20. Crea una función que reciba un empleado (de la clase que has creado en el ejercicio
# anterior) y el nombre de un fichero y te añada el empleado al fichero. La llamada a esta
# función debería de ser así:
# grabarEmpleado(“/home/josemaria/empleados.bin”, empleado1)

def grabarEmpleado (ruta, empleado):

    #Validar existe el fichero
    try:
        file = open(ruta, "bw+")
    except:
        raise Exception("El archivo no existe")

    if file.read() == null:
        raise Exception("El archivo esta vacio")




grabarEmpleado("./empleado.bin", empleado1 = Empleado())

# Ejercicio 21
# 1. Tenemos un fichero con un formato como el que sigue:
# 1 Bulbasaur; 2 Ivysaur; 3 Venasaur
# 25 Pikachu; 26 Raichu
# 122 Mr. Mime
# 227 Skarmory
# Dónde cada línea del fichero se corresponde con una línea evolutiva de un
# Pokemon de la primera generación. Tu fichero deberá de comprobar lo siguiente:
# - En cada línea aparece al menos un pokemon y como máximo tres
# - Por cada pokemon aparece su número de la pokedex y su nombre. El separador
# entre pokemons es siempre el símbolo ; y un espacio en blanco
# - El número de la pokedex es un número positivo mayor o igual a 1 e inferior o
# igual a 151
# - El nombre del pokemon puede contener espacios y el punto (.) pero nunca
# números u otros símbolos no alfabéticos
# - Tu programa debe de tener dos variables claramente definidas con los nombres
# de los ficheros de entrada y de salida. Así por ejemplo:

print("Ejercicio 21")

def leerPokemons():
    entrada = "./pokemon_in.txt"
    salida = "./pokemon_out.txt"

    codigo = r"^[1-151]"
    try:
        nameFileR = open(entrada, "w")
        nameFileW = open(salida, "r")
    except:
        raise Exception("El archivo no existe")

    for linea in nameFileR.readlines():
        linea = linea.strip(";") # hdasjasdh ; hsdajhsdks ; sdajksdsd 3

        if not len(linea) <= 3:
            raise Exception("Tiene que haber al menos 3 campos")
            return

        if not regex.match(linea, regex):
            raise Exception("Línea erronea detectada:", linea)
            return

leerPokemons()

import re

entrada = "./pokemon_in.txt"
salida = "./pokemon_out.txt"

# Regex
regex_numero = r"^(?:[1-9]|[1-9][0-9]|1[0-4][0-9]|151)$"
regex_nombre = r"^[A-Za-z .]+$"

def leerPokemons():
    total_pokemons_correctos = 0

    try:
        f_in = open(entrada, "r")
        f_out = open(salida, "w")
    except:
        raise Exception("No se pudo abrir alguno de los archivos")

    for linea in f_in:
        linea = linea.strip()
        linea_correcta = True
        pokemons = linea.split("; ")

        if not (1 <= len(pokemons) <= 3):
            print(f"Línea errónea detectada: {linea}")
            print("La línea no tiene entre 1 y 3 pokemons")
            linea_correcta = False

        for pokemon in pokemons:
            partes = pokemon.split(" ", 1)

            if len(partes) != 2:
                print(f"Línea errónea detectada: {linea}")
                print("Formato incorrecto: falta número o nombre")
                linea_correcta = False
                break

            numero, nombre = partes

            if not re.match(regex_numero, numero):
                print(f"Línea errónea detectada: {linea}")
                print("El número de la pokedex no es de la primera generación")
                linea_correcta = False
                break

            if not re.match(regex_nombre, nombre):
                print(f"Línea errónea detectada: {linea}")
                print("El nombre del pokemon contiene caracteres no válidos")
                linea_correcta = False
                break

        if linea_correcta:
            f_out.write(linea + "\n")
            total_pokemons_correctos += len(pokemons)

    f_in.close()
    f_out.close()

    print(f"Se han grabado {total_pokemons_correctos} pokemons correctos en el fichero de salida")

leerPokemons()

# 22. Partimos ahora de un fichero como el del ejercicio anterior pero ya
# validado y correcto donde no tienes que comprobar que haya líneas erróneas
# porque es seguro que no las hay. Puedes hacer las pruebas con el siguiente:
# 1 Bulbasaur; 2 Ivysaur; 3 Venasaur
# 25 Pikachu; 26 Raichu
#122 Mr. Mime

print("Ejercicio 22")
entrada = "./pokemon_in.txt"

def pokedex():
    while True:
        dato = input("Introduce otro pokemon o escribe Exit para salir: ").strip()

        if dato.lower() == "exit":
            print("Gracias por consultar la pokedex")
            break

        encontrado = False

        # Comprobación básica
        if not dato.replace(" ", "").replace(".", "").isdigit() and not dato.replace(".", "").replace(" ", "").isalpha():
            print("Eso no parece corresponder a un nombre de pokemon o código de la pokedex")
            continue

        with open(entrada, "r") as f:
            for linea in f:
                cadena = linea.strip().split("; ")

                for i, p in enumerate(cadena):
                    num, nombre = p.split(" ", 1)

                    if dato.lower() == nombre.lower() or dato == num:
                        encontrado = True
                        print(f"{nombre}. Su número de la Pokedex es el {num}")

                        if i > 0:
                            n_ant, nom_ant = cadena[i - 1].split(" ", 1)
                            print(f"Evoluciona de {nom_ant}({n_ant}).", end=" ")
                        else:
                            print("No evoluciona de ningún otro.", end=" ")

                        if i < len(cadena) - 1:
                            n_sig, nom_sig = cadena[i + 1].split(" ", 1)
                            print(f"Evoluciona en {nom_sig} ({n_sig})")
                        else:
                            print("No evoluciona a ningún otro")

        if not encontrado:
            print("Ese Pokemon no está registrado en la pokedex")

pokedex()

# 23. Tenemos necesidad de mejorar nuestra pokedex y vamos a utilizar para ello
# programación orientada a objetos. Además de los datos que ya manejamos (número
# de la pokedex, nombre del pokemon, pokemon del que evoluciona y pokemon a que
# evoluciona) queremos guardar el tipo o tipos del Pokemon. Un ejemplo de como
# debería de funcionar nuestro programa es este:

print("Ejercicio 23")

class Pokemon:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None
        self.tipos = []

    def evoluciona(self, pokemon):
        self.siguiente = pokemon
        pokemon.anterior = self

    def tipo(self, tipo):
        if tipo not in self.tipos:
            self.tipos.append(tipo)

    def mostrar(self):
        print(f"{self.codigo}. {self.nombre}")

        if self.anterior:
            print(f"- Evoluciona de {self.anterior.nombre}")
        else:
            print("- No se conoce de donde evoluciona")

        if self.siguiente:
            print(f"- Evoluciona en {self.siguiente.nombre}")
        else:
            print("- No se conoce a donde evoluciona")

        print("- Tipos: " + ", ".join(self.tipos))

pokemon1 = Pokemon(10, "Caterpie")
pokemon2 = Pokemon(11, "Metapod")
pokemon3 = Pokemon(12, "Butterfree")

pokemon1.evoluciona(pokemon2)
pokemon2.evoluciona(pokemon3)

pokemon1.tipo("Bicho")
pokemon2.tipo("Bicho")
pokemon3.tipo("Bicho")
pokemon3.tipo("Volador")

pokemon1.mostrar()
pokemon2.mostrar()
pokemon3.mostrar()


# 4. Queremos implementar un método que nos permita jugar eligiendo tres
# pokemons de forma aleatoria de entre los guardados en un fichero.
# NOTA IMPORTANTE: Puedes partir de la clase que has creado en el ejercicio
# anterior o si quieres, para simplificar o porque no lo has hecho, puedes usar
# una mas simple sólo con el constructor. No te va a hacer falta nada mas
# Lo primero que tiene que hacer tu programa es crear los pokemons y guardarlos
# en un fichero binario

print("Ejercicio 24")

# ME DA PEREZAS
