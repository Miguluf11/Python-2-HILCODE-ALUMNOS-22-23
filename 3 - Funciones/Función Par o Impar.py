# Escribe tu código aquí :-)
def par_o_impar(numero):
    print("Tu número es", numero)
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")


numero = int(input("Escriba un número: "))
par_o_impar(numero)
