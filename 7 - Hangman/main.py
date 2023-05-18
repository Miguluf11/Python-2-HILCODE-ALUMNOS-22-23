import horca
from caja import crear_caja
import palabras
import inputs
import checks

palabra = palabras.palabra
guiones = "_" * len(palabra)
letras = ""
vidas = 6
crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = "¡Hola, Bienvenido al juego!")
print(horca.visual[vidas])
crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = guiones)

while True:
    letras, letra = inputs.input_letras(letras)
    guiones, vidas = checks.checks(palabra, guiones, letra, vidas)
    crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = letras)
    print(horca.visual[vidas])
    crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = guiones)


