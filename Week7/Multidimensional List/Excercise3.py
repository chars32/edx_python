#Write a function that accepts a 2D list of integers and returns the maximum EVEN value for the entire list. 
#You can assume that the number of columns in each row is the same. 
#Your function should return None if the list is empty or all the numbers in the 2D list are odd. 
#Do NOT use python's built in max() function.

def even_empty_odd(list2d):
	len_list = 0
	even_numbers = []
	odd_numbers = []
	count = 0

	#if the list is empty
	for list_number in list2d:
		len_list += len(list_number)

	if len_list == 0:
		return None

	#if the list is gretaer than zero
	else:
		for list_number in list2d:
			for number in list_number:
				#find the even numbers
				if number % 2 == 0:
					even_numbers.append(number) #append all the even numbers in the even_numbers list
				else:
					#find the odd numbers
					odd_numbers.append(number) #append all the odd numbers in the odd_numbers list
				count += 1

	#Compare if the len of the odd_numbers list is equal to count
	#if True that means that all the numbers are odds
	if len(odd_numbers) == count:
		return "All the numbers in the list are odds"
	
	#if not it means that at least there is onw even number
	else:
		even_numbers.sort()
		return even_numbers[len(even_numbers)-1]

print(even_empty_odd([[1,8],[3,2]]))