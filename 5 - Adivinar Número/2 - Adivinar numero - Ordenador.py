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

def adivinar(jugador, bot, intentos, MAX):
    maximo = MAX
    minimo = 0
    while bot != jugador:
        if bot < jugador:
            print(f"El número {bot} es menor que el número secreto.")
            minimo = bot + 1
            bot = random.randint(minimo,maximo)
        elif bot > jugador:
            print(f"El número {bot} es mayor que el número secreto.")
            maximo = bot - 1
            bot = random.randint(minimo,maximo)
        intentos += 1

    return intentos

MAX = 10000000000000000000000000000000
jugador = int(input(f"Elija un numero entre 0 y {MAX} "))
bot = random.randint(0,MAX)
intentos = 0
intentos = adivinar(jugador, bot, intentos, MAX)

print(f"El ordenador ha acertado el número con {intentos} intentos")
1865471546154415456
