#Write a function named calculate_fibonacci that receives a positive integer 'n' as parameter 
#and calculates and returns the nth fibonacci number using recursion. 
#Notes
#Fibonacci numbers are the numbers in the sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
#The 0th Fibonacci number is 0, the 1st Fibonacci number is 1.
#All other numbers are sum of the previous two numbers.

def calculate_fibonacci(number):
	if number == 0:
		return 0
	elif number == 1:
		return 1
	else:
		return calculate_fibonacci(number-1) + calculate_fibonacci(number-2)

print(calculate_fibonacci(10))