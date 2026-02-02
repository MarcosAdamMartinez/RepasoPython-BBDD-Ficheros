# Gestión de Inventario:
# Imagina que tienes un archivo productos.txt donde cada línea es nombre,precio,cantidad. Haz un script que:
# Lea el archivo.
# Calcule el valor total del inventario (precio * cantidad).
# Añada una nueva línea al final con el producto "Teclado" a 25.99€ y 10 unidades.

ARCHIVO = "archivos/productos.txt"

try:
    total = 0
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            valores = linea.strip().split(",")
            total += float(valores[1]) * float(valores[2])

    print(f"El total de los productos del archivo es: {total}")

    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write("Teclado,25.99,10\n")

except FileNotFoundError:
    print("Archivo no existe")
except Exception as e:
    print(e)

