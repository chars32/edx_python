#Write a function that accepts a 2-dimensional list of integers, and returns a sorted (ascending order) 
#1-Dimensional list containing all the integers from the original 2-dimensional list.

def one_list_descending(list2d):

	final_list = []

	for list_number in list2d:

		for number in list_number:

			final_list.append(number)

	final_list.sort()

	return final_list

print(one_list_descending([[1,2],[3,4]]))