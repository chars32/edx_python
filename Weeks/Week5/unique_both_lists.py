#Write a function that accepts two input lists and returns a new list 
#which contains only the unique elements from both lists.

def unique_both_lists(list1, list2):

	list1.extend(list2)

	listaFinal = []

	for x in list1:
		if x not in listaFinal:
			listaFinal.append(x)

	return listaFinal
