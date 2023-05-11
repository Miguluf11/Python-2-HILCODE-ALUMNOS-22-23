def leer_fichero(nombre_fichero):
    palabras = []
    with open(nombre_fichero, "r") as f:
        for palabra in f:
            palabra = palabra.replace("\n","")
            palabras.append(palabra)
    f.close()
    return palabras
