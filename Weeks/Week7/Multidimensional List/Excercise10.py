#Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns True 
#if they can be multiplied together False otherwise. Hint: Two matrices a and b can be multiplied together 
#only if the number of columns of the first matrix(a) is the same as the number of rows of the second matrix(b). 
#The input for this function will be two 2 Dimensional lists.


def mult_matrix (list_one_2d, list_two_2d):

	if len(list_one_2d[0]) == len(list_two_2d):

		return True

	else: 

		return False



a = [[2, 3, 4],
     [3, 4, 5]]

b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(mult_matrix(a,b))