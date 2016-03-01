#Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product. 
#Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is the 
#same as the number of rows of the second matrix(b). Do NOT use numpy module for this exercise. The input for this 
#function will be two 2 Dimensional lists.

def mult_matrix_without_numpy(a,b):

	print(a)
	print(b)

a = [[2, 3, 4],
     [3, 4, 5]]

b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(mult_matrix_without_numpy(a,b))