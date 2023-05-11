import palabras
import inputs

dict_especiales = {"A":"Á", "E":"É", "I":"Í", "O":"Ó", "U":"Ú", "N":"Ñ"}



def checks(palabra, guiones, letra, dict_especiales):
    lista_guiones = []
    tam = len(palabra)

    # pasa de string a lista
    for i in range(tam):
        lista_guiones.append(guiones[i])

    for i in range(0,tam):
        if palabra[i] == letra:
            lista_guiones[i] = letra

        elif letra in dict_especiales.keys() and palabra[i] == dict_especiales[letra]:
            lista_guiones[i] = dict_especiales[letra]

    # une los elementos de la lista de vuelta a strings
    guiones = ""
    for i in range(len(lista_guiones)):
        guiones = guiones + lista_guiones[i]

    return guiones

guiones = checks(palabra, guiones, letra, dict_especiales)


