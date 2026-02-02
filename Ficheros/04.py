# El Log de Errores:
# Escribe un programa que intente leer una lista de archivos de una carpeta
# (puedes usar la librería os). Si un archivo no existe, debe capturar
# la excepción y escribir en un fichero binario de "log" el nombre del archivo
# fallido y la hora exacta del error. Si existe, debe copiar su
# contenido a un archivo maestro de texto
import datetime
import pickle

listaArch = ["archivos/datos.txt", "archivos/config.txt", "notas.dat"]

ARCHIVO_MAESTRO = "archivos/maestro.txt"

for fichero in listaArch:
    try:
        if fichero.endswith(".txt"):
            with open(fichero,"r", encoding="utf-8") as archivo:
                with open(ARCHIVO_MAESTRO,"a",encoding="utf-8") as archivo_maestro:
                    for linea in archivo:
                        archivo_maestro.write(linea)
        else:
            with open(fichero,"rb") as archivo:
                with open(ARCHIVO_MAESTRO,"a", encoding="utf-8") as archivo_maestro:
                    for linea in archivo:
                        archivo_maestro.write(linea)
    except FileNotFoundError as e:
        dumpear = str(e) + " - Fecha del error: " + str(datetime.datetime.now())
        with open("archivos/residuales/log.dat", "ab") as archivo:
            pickle.dump(dumpear, archivo)
    except Exception as e:
        print(e)