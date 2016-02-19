#Write a function that accepts a list and returns a new list such 
#that the new list contains all the items of the old list in reverse order.

def list_reverse(lista):

	largo = len(lista)

	lista_final = []

	while largo >= 1:

		lista_final.append(lista[largo-1])

		largo = largo - 1

	return lista_final


input_list = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']

list_reverse(input_list)