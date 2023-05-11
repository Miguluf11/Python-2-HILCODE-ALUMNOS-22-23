import horca
from caja import crear_caja
import palabras
import inputs

crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = "")
print(horca.visual[6])
crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = "")
palabra = palabras.palabra
guiones = "_" * len(palabra)
print(palabra)
print(guiones)

letras = ""
letras, letra = inputs.input_letras(letras)

crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = letras)
print(horca.visual[6])
crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = "")

letras, letra = inputs.input_letras(letras)

crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = letras)
print(horca.visual[6])
crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = "")
