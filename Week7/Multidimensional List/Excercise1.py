#Write a function which accepts a 2D list of numbers and returns the sum of all the number in the list 
#You can assume that the number of columns in each row is the same. 
#(Do not use python's built-in sum() function).

def two_list_numbers(list2d):
	total_sum = 0
	for list_number in list2d:
		for number in list_number:
			total_sum += number
	return total_sum

print(two_list_numbers([[1,2,3],[4,5,6]]))