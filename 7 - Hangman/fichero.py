nombre_fichero = "fichero_palabras.txt"

def leer_fichero(nombre_fichero):
    palabras = []
    with open(nombre_fichero, "r") as f:
        for palabra in f:
            palabra = palabra.replace("\n","")
            palabras.append(palabra)
    f.close()
    return palabras

palabras = leer_fichero(nombre_fichero)
print(palabras)


