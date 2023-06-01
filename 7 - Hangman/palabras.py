from fichero import leer_fichero
import random

def sortear_palabra(todasPalabras):
    indice = random.randint(0,len(todasPalabras)-1)
    palabra = todasPalabras[indice]
    return palabra

nombre_fichero = "fichero_palabras.txt"
todasPalabras = leer_fichero(nombre_fichero)
palabra = sortear_palabra(todasPalabras)
