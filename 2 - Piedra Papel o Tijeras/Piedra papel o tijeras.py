# Escribe tu código aquí :-)

p1 = ["tijeras", "tijeras", "piedra"]
p2 = ["tijeras", "papel", "piedra"]

def piedra_papel_tijeras(p1, p2):
    piedra = "piedra"
    papel = "papel"
    tijeras = "tijeras"
    if p1[0] == p2[0]:
        print("Empate.")

    if p2[0] == papel and p1[0] == piedra:
        print("Gana jugador 2.")
    if p1[0] == piedra and p2[0] == tijeras:
        print("Gana jugador 1.")
    if p1[0] == tijeras and p2[0] == papel:
        print("Gana jugador 1.")

    if p1[0] == papel and p2[0] == piedra:
        print("Gana jugador 1.")
    if p2[0] == piedra and p1[0] == tijeras:
        print("Gana jugador 2.")
    if p2[0] == tijeras and p1[0] == papel:
        print("Gana jugador 2.")

    # SEGUNDA RONDA

    if p1[1] == p2[1]:
        print("Empate.")

    if p2[1] == papel and p1[1] == piedra:
        print("Gana jugador 2.")
    if p1[1] == piedra and p2[1] == tijeras:
        print("Gana jugador 1.")
    if p1[1] == tijeras and p2[1] == papel:
        print("Gana jugador 1.")

    if p1[1] == papel and p2[1] == piedra:
        print("Gana jugador 1.")
    if p2[1] == piedra and p1[1] == tijeras:
        print("Gana jugador 2.")
    if p2[1] == tijeras and p1[1] == papel:
        print("Gana jugador 2.")

    # TERCERA RONDA

    if p1[2] == p2[2]:
        print("Empate.")

    if p2[2] == papel and p1[2] == piedra:
        print("Gana jugador 2.")
    if p1[2] == piedra and p2[2] == tijeras:
        print("Gana jugador 1.")
    if p1[2] == tijeras and p2[2] == papel:
        print("Gana jugador 1.")

    if p1[2] == papel and p2[2] == piedra:
        print("Gana jugador 1.")
    if p2[2] == piedra and p1[2] == tijeras:
        print("Gana jugador 2.")
    if p2[2] == tijeras and p1[2] == papel:
        print("Gana jugador 2.")

jugadas = ["piedra", "papel", "tijeras"]

piedra_papel_tijeras(p1, p2)


'''
p1 = input("Elija piedra, papel, o tijeras. ")
while p1 not in jugadas:
    print("INVALIDO!!")
    p1 = input("Elija piedra, papel, o tijeras. ")

p2 = input("Elija piedra, papel, o tijeras. ")
while p2 not in jugadas:
    print("INVALIDO!!")
    p2 = input("Elija piedra, papel, o tijeras. ")
'''
