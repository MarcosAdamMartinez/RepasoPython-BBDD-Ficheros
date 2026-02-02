import pickle

try:
    archivo = open("archivos/residuales/log.dat","rb")
    print(pickle.load(archivo))
except Exception as e:
    print(e)