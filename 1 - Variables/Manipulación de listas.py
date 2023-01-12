#####################################################################
####################### Declarando variables ########################
nombre = 'Clóvis Magno'
edad = 24

#####################################################################
################## Entrada de valores por teclado ###################
nombre = input("Escriba tu nombre: ")

print(nombre)
print("Tu nombre es: ", nombre)

edad = int(input("¿Cuántos años tienes? "))
print("Tu edad es: ", edad)


compras = ["Manzana", "Plátano", "Sandía", "Uva"]

print(compras)
print(compras[0])
print(compras[2])

#####################################################################
################### Añadiendo elementos una lista ###################
item = input("¿Qué deseas añadir a la lista de compras? ")
compras.append(item)
print(compras)

nombres = []

nombre = input("Como te llamas?")
nombres.append(nombre)

madre = input("Como se llama tu madre?")
nombres.append(madre)
print(nombres)

#####################################################################
################## Excluyendo elementos una lista ###################
compras.pop()
print(compras)

compras.pop()
print(compras)

compras.remove("Manzana")
print(compras)

#####################################################################
################# Enseñando elementos deuna lista ###################
edades = [10, 15, 16, 17, 12, 13, 14, 15, 20, 25, 19, 18, 26]
print(edades[11]) # muestra el elemento en la posición de indice 11

print(edades[-1]) # -1 muuestra el ultimo elemento, -2 el penultimo, -3 el antipenultimo...

print("Tamaño:", len(edades))

#####################################################################
################### Ejemplo de uso de las listas ####################
nombres = []
edades = []

nombre = input("Como te llamas?")
nombres.append(nombre)
edad = int(input("Cuántos años tienes?"))
edades.append(edad)

madre = input("Como se llama tu madre?")
nombres.append(madre)
edad = int(input("Cuántos años tiene tu madre?"))
edades.append(edad)
print(nombres)
print(edades)

edades[0] = edades[0] + 10
print(edades)


print("La lista tiene tamaño", len(nombres))
print("La última persona es: ", nombres[-1])
