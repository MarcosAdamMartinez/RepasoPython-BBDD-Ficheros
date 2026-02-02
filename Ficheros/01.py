# El Contador de Palabras:
# Crea un programa que lea un archivo llamado quijote.txt,
# cuente cuántas veces aparece la palabra "Sancho" y escriba el resultado en
# un nuevo archivo llamado resultado.txt

try:
    contador = 0
    with open("archivos/quijote.txt","r") as fichero:
        for linea in fichero:
            linea = linea.replace("\n","")
            if "Sancho" in linea:
                palabras = linea.split(" ")
                for palabra in palabras:
                    palabra = palabra.strip(",.;:¡!¿?")
                    if palabra == "Sancho":
                        contador += 1
    print(f"La palabra Sancho aparece: {contador} veces")

    with open("archivos/residuales/resultado.txt", "w") as ficheroEscritura:
        ficheroEscritura.write(f"La palabra Sancho aparece: {contador} veces")

except:
    print("No existe el fichero.")

