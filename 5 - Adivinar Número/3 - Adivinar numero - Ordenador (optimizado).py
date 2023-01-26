import random

def input_numero(MAX):
    numero = int(input(f"Escriba un numero entre 0 y {MAX} "))
    while numero > MAX or numero < 0:
        print("Este número no es válido")
        numero = int(input(f"Escriba un numero entre 0 y {MAX} "))
    return numero

def adivinar(MAX, numero, intentos):
    minimo = 0
    maximo = MAX
    bot = MAX//2
    while bot != numero:
        print("El numero ", bot," no es correcto.")
        if bot > numero:
            maximo = bot
            bot = (maximo+minimo)//2

        elif bot < numero:
            minimo = bot
            bot = (maximo+minimo)//2

        intentos = intentos + 1
    return bot, intentos


MAX = 10000
numero = input_numero(MAX)
intentos = 0
bot, intentos = adivinar(MAX, numero,intentos)
print("El numero ", bot," es correcto.")
print("Repeticiones: ", intentos)
