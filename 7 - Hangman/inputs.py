def input_letras(letras):
    letra = input("¿Qué letra quieres intentar? ")
    while letra[0].upper() in letras:
        letra = input("Ya has puesto esa letra, intenta otra:  ")
    letra = letra[0].upper()
    letras = letras + letra + " "
    return letras, letra
