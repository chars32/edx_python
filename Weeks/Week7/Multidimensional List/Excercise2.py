#Write a function that accepts a 2 Dimensional list of integers and returns the average. 
#Remember that average = (sum_of_all_items) / (total_number_of_items).

def average_two_list(list_dimensional):
	total_sum = 0
	total_numbers = 0

	for each_list in list_dimensional:
		for number in each_list:
			total_sum += number
			total_numbers += 1

	average = total_sum/total_numbers
	return average

result = average_two_list([[1,2],[3,4]])
print (result)
