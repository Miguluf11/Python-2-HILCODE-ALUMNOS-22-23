'''
En este proyecto vamos a desarrollar un juego donde el ordenador genera
un número aleatorio y nosotros necesitamos adivinarlo. Para ello, en cada
intento que hagamos, el programa nos avisará si el número correcto es mayor
o menor que el número que hemos introducido por teclado.

A priori, el ordenador debe sortear números entre 0 y 10 para que sea más fácil
el testeo y corrección de eventuales errores.
'''
import random
import time

numero = random.randint(0,10)
mi_numero = int(input("¿Qué número quieres probar? "))

while mi_numero != numero:
    if mi_numero < numero:
        print("El número secreto es mayor.")
        mi_numero = int(input("¿Qué número quieres probar? "))
    elif mi_numero > numero:
        print("El número secreto es menor.")
        mi_numero = int(input("¿Qué número quieres probar? "))

print("Ea, has acertado el número!")

