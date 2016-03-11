#Write a function named nested_list_sum that receives a nested list of integers as parameter and calculates 
#and returns the total sum of the integers in the list using recursion. Keep in mind that the inner elements 
#may be integers or other nested lists themselves. 

def nested_list_sum(list_nested):
	sum = 0
	for elements in list_nested:
		if type(elements) != type([]):
			sum += elements
		else:
			sum += nested_list_sum(elements)
	return sum

print(nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]]))