#Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product. 
#Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is the same 
#as the number of rows of the second matrix(b). Hint: You may import and use the numpy module but your return must be a 
#python list not a numpy array. The input for this function will be two 2 Dimensional lists.

# I couldnt install numpy, so I use the answer in the excercise.

def mult_matrix (list_one_2d, list_two_2d):
	import numpy
	product = (numpy.mat(a) * numpy.mat(b))
	product_to_list = product.tolist()
	return product_to_list

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(mult_matrix(a,b))