#Write a function named multiplication_table that receives a positive integer 'n' as parameter 
#and returns a n by n multiplication table as a two-dimensional list.

def multiplication_table(n):
	final_list = []

	for x in range(1,n+1):
		list_aux = []
		
		for z in range(1, n+1):
			list_aux.append(x*z)
			
			if len(list_aux) == n:
				final_list.append(list_aux)
	return final_list


print(multiplication_table(4))