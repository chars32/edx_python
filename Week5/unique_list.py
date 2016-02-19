#Write a function that accepts an input list and returns a new list which contains only 
#the unique elements(Elements should only appear one time in the list and the order of 
#the elements must be preserved as the original list. ).

def unique_list(lista):

	lista_final = []

	for x in lista:
		if x not in lista_final:
			lista_final.append(x)

	return lista_final


print(unique_list([1,5,2,2,3,1,4,5,3,5,7]))