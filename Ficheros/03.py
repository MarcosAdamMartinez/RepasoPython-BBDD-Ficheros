# Persistencia de Objetos:
# Crea una clase Alumno con atributos nombre, nota y modulo.
# Crea una lista con 3 objetos de tipo Alumno.
# Guarda esa lista completa en un archivo binario llamado alumnos.dat.
# Crea otra función que lea ese archivo, cargue la lista y muestre solo los alumnos que han aprobado (nota >= 5)

import pickle
from typing import override

ARCHIVO = "archivos/residuales/alumnos.dat"

class Alumno:
    def __init__(self, nombre, nota, modulo):
        self.__nombre = nombre
        self.__nota = nota
        self.__modulo = modulo

    @property
    def nota(self):
        return self.__nota

    def __str__(self):
        return f"Nombre: {self.__nombre}, nota: {self.__nota}, modulo: {self.__modulo}"


alumno1 = Alumno("Alumno1", 10.0, "Modulo1")
alumno2 = Alumno("Alumno2", 2.0, "Modulo1")
alumno3 = Alumno("Alumno3", 5.5, "Modulo1")

lista = [alumno1, alumno2, alumno3]
def dumpear(lista):
    try:
        with open(ARCHIVO, "wb") as archivo:
            pickle.dump(lista, archivo)
    except FileNotFoundError:
        print("Archivo no existe")
    except Exception as e:
        print(e)

def loadear(fichero):
    try:
        with open(fichero, "rb") as archivo:
            lista = pickle.load(archivo)

            for alumno in lista:
                if alumno.nota >= 5.0:
                    print(alumno)
    except FileNotFoundError:
        print("Archivo no existe")
    except Exception as e:
        print(e)

dumpear(lista)
loadear(ARCHIVO)