def unique_common(a, b):

    lista = []
    lista_final = []

    #obtenemos los numeros repetidos en las dos listas,
    #sin importar que se repitan
    for i in a:
        if i in b:
            lista.append(i)

    #creamos una lista en la cual no habra numeros repetidos
    for i in lista:
        if i not in lista_final:
            lista_final.append(i)

    lista_final.sort() #ordenamos la lista
    return lista_final

    

print(unique_common([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7]))
#print(unique_common([1,2,3,5,4,6], [2, 4, 5, 5, 6]))
