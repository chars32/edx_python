#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns 
#a list which includes the maximum value of each row.

def maximun_value(list2d):
	final_list = []

	for list_number in list2d:
		final_list.append(max(list_number))

	return final_list


print(maximun_value([[1,2,4,5],[9,3,5,6]]))