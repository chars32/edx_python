#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list 
#which includes the sum of each column. Assume that the number of columns in each row is the same.

def sum_of_two_lists_col(list2d):
	final_list = []

	#we know that every row have the same number of column
	#we get the len of a list in list2d
	lists_len_list2d = len(list2d[0])

	for x in range(0, lists_len_list2d): #we start a for with the range of the len of the element
		sum_cols = 0

		for lists_numbers in list2d: #we search in the items of list2d with the index of x
			sum_cols += lists_numbers[x]

		final_list.append(sum_cols)

	return final_list

print(sum_of_two_lists_col([[1,2,3,4], [2,4,6,8]]))
