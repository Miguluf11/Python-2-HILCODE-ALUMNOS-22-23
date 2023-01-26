'''
Semejante al proyecto anterior, vamos a hacer otro proyecto
para adivinar números, sin embargo, nosotros somos los que
decimos que número debe ser adivinado y el ordenador es el
responsáble por adivinarlo en el menor número de turnos posible.

Para ello necesitamos programar el ordenador de tal modo que pueda
convergir al número que indiquiemos nosotros al início del programa.
Hay várias maneras de hacerlo, cabe a vosotros pensar y desarrollar
una manera que el ordenador pueda encontrar el número secreto en el
menor número de turnos posible.
'''
import random
mínimo = 0
máximo = 100000
numero = int(input(f"Elige un número entre {mínimo} y {máximo}: "))
ordenador = random.randint(mínimo, máximo)
intentos = 0
def juego(numero,ordenador,intentos, máximo, mínimo):

    print (ordenador)
    while numero != ordenador:
        if numero > ordenador:
            intentos += 1
            print ("El número es mayor")
            mínimo = ordenador + 1
            ordenador = random.randint(mínimo, máximo)
            print(ordenador)
        if numero < ordenador:
            intentos += 1
            print ("El número es menor")
            máximo = ordenador - 1
            ordenador = random.randint(mínimo, máximo)
            print (ordenador)
        if numero == ordenador:
            intentos  += 1
            print("Es correcto")
            print ("Lo has hecho en", intentos, "intentos")


juego(numero,ordenador,intentos, máximo, mínimo)


