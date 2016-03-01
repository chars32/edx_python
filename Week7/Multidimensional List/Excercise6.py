#Write a function that will receive a 2D list of integers. 
#The function should return the count of how many rows of the list have even sums and the count of how many rows have odd sums. 
#For example if the even count was 2, and odd count was 4 your function should return them in a list like this: [2, 4].

def list_even_odds(list2d):

	even_count = 0
	odd_count = 0

	for list_number in list2d:
		list_number_sum = sum(list_number)
		
		if list_number_sum % 2 == 0:
			odd_count += 1
		else:
			even_count += 1

	return [odd_count, even_count]



print (list_even_odds([[1, 2, 3, 5], [5, -6, -9, 9], [2, 2, 2, 2], [1, 1, 1, 0]]))