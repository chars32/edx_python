#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list 
#which includes the maximum value of each column. Assume that the length of columns is consistent in each row.

def maximun_value_columns(list2d):
	len_lists = len(list2d[0])
	final_list = []

	for number in range(len_lists):
		aux_list = []
		for list_number in list2d:
			aux_list.append(list_number[number])
		final_list.append(max(aux_list))

	return final_list


print(maximun_value_columns([[1,2],[3,4]]))