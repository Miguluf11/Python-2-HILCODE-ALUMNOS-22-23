# Escribe tu código aquí :-)
# Escribe tu código aquí :-)

p1 = ["tijeras", "tijeras", "piedra"]
p2 = ["tijeras", "papel", "piedra"]

def piedra_papel_tijeras(p1, p2):
    piedra = "piedra"
    papel = "papel"
    tijeras = "tijeras"
    posicion = 0
    while posicion < 3:
        if p1[posicion] == p2[posicion]:
            print("Empate.")

        if p2[posicion] == papel and p1[posicion] == piedra:
            print("Gana jugador 2.")
        if p1[posicion] == piedra and p2[posicion] == tijeras:
            print("Gana jugador 1.")
        if p1[posicion] == tijeras and p2[posicion] == papel:
            print("Gana jugador 1.")

        if p1[posicion] == papel and p2[posicion] == piedra:
            print("Gana jugador 1.")
        if p2[posicion] == piedra and p1[posicion] == tijeras:
            print("Gana jugador 2.")
        if p2[posicion] == tijeras and p1[posicion] == papel:
            print("Gana jugador 2.")

        posicion = posicion + 1

jugadas = ["piedra", "papel", "tijeras"]



piedra_papel_tijeras(p1, p2)
