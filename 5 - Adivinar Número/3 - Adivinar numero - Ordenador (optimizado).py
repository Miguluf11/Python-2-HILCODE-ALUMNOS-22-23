import random

def input_numero(lim):
    numero = int(input(f"Escriba un numero entre 0 y {lim} "))
    while numero > lim or numero < 0:
        print("Este número no es válido")
        numero = int(input(f"Escriba un numero entre 0 y {lim} "))
    return numero

def adivinar(lim, numero):
    lim_inferior = 0
    lim_superior = lim
    ordenador = lim//2
    repeticiones = 0
    while ordenador != numero:
        print("El numero ", ordenador," no es correcto.")
        if ordenador > numero:
            lim_superior = ordenador
            ordenador = (lim_superior+lim_inferior)//2

        elif ordenador < numero:
            lim_inferior = ordenador
            ordenador = (lim_superior+lim_inferior)//2

        repeticiones = repeticiones + 1
    return ordenador, repeticiones


lim = 1000
numero = input_numero(lim)
ordenador, repeticiones = adivinar(lim, numero)
print("El numero ", ordenador," es correcto.")
print("Repeticiones: ", repeticiones)
