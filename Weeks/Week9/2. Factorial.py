#Write a function named calculate_factorial that receives a positive integer 'n' as parameter 
#and calculates and returns the factorial of n using recursion. 
#Notes
#Factorial is the product of an integer with all the integers below it. 
#For example, the factorial of 5 is 5*4*3*2*1 = 120. Note that the factorial of both 0 and 1 is 1.

def calculate_factorial(n):
	if n == 0 or n == 1:
		return 1
	return calculate_factorial(n-1)*n

print(calculate_factorial(5))