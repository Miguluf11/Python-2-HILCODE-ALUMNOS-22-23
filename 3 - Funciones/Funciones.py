'''
Explicación con más detalles sobre las funciones 
disponible en https://drive.google.com/file/d/1SB7ff6AB1jaTidw4kcyQAo0D3b21PbbJ/view
'''

num_1 = 2
num_2 = 3
suma = num_1 + num_2
print("La suma es", suma)



#############################

def sumador():
    num_1 = 2
    num_2 = 3
    suma = num_1 + num_2
    print("La suma es", suma)

sumador()
###################################

def sumador(num_1, num_2):
    suma = num_1 + num_2
    print("La suma es", suma)

num_1 = 2
num_2 = 3
sumador(num_1,num_2)



#############################
suma = 0
def sumador():
    num_1 = 2
    num_2 = 3
    suma = num_1 + num_2

sumador()
print(suma)
##############################
suma = 0
def sumador():
    num_1 = 2
    num_2 = 3
    suma = num_1 + num_2
    return suma

suma = sumador()
print(suma)
##############################


def sumador(num_1, num_2):
    suma = num_1 + num_2
    return suma

num_1 = 2
num_2 = 3
suma = 0
suma = sumador(num_1, num_2)
print("La suma es", suma)



################################

num_1 = 10
num_2 = 5

suma = num_1 + num_2
resta = num_1 - num_2
multipicacion = num_1 * num_2
division = num_1 - num_2

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La división es: ", division)
##################################

def calculadora():
    num_1 = 10
    num_2 = 5

    suma = num_1 + num_2
    resta = num_1 - num_2
    multipicacion = num_1 * num_2
    division = num_1 - num_2

    print("La suma es: ", suma)
    print("La resta es: ", resta)
    print("La multiplicación es: ", multiplicacion)
    print("La división es: ", division)

##################################

def calculadora():
    num_1 = 10
    num_2 = 5

    suma = num_1 + num_2
    resta = num_1 - num_2
    multipicacion = num_1 * num_2
    division = num_1 - num_2
    return suma, resta, multiplicacion, division

suma = 0
resta = 0
multiplicacion = 0
division = 0
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La división es: ", division)
'''
