#Write a function that accepts two lists both of which consists of integers
#and returns the total sum of all the odd integers 


def odd_lists(a,b):
	a.extend(b)
	lista = 0
	
	for x in a:
		if x%2 != 0:
			lista += x

	return (lista)



list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

odd_lists(list1, list2)