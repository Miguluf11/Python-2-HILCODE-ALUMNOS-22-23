# Escribe tu código aquí :-)
import random
nombre_fichero = "Todas_Palabras.txt"

numeros = []
for i in range(0,1000):
    numeros.append(random.randint(0,100))
print(numeros)

f = open(nombre_fichero,'w')
for i in range(len(numeros)):
    f.write(str(numeros[i])+"\n")
f.close()


