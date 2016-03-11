#Write a function named calculate_exponent that receives two positive integers a and b as parameter 
#and calculates and returns a to the power of b using recursion.

def calculate_exponent(a, b):
	if b == 0:
		return 1
	exp = calculate_exponent(a, b-1)*a
	return exp

print(calculate_exponent(5, 3))