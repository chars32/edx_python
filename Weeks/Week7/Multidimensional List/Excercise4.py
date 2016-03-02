#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list 
#which includes the sum of each row. You can assume that the number of columns in each row is the same.

def sum_of_two_lists_row(list2d):
	final_list = []

	for list_numbers in list2d:
		sum_list = 0
		for number in list_numbers:
			sum_list += number
		final_list.append(sum_list)

	return final_list

print(sum_of_two_lists([[1,2],[3,4]]))