#Write a function named calculate_gcd that receives two positive integers a and b as parameter and returns 
#their greatest common divisor (GCD) using recursion.

def calculate_gcd(a, b):
    if b == 0:
    	return a
    else:
    	print("antes", a,b, a%b)
   g cd = calculate_gcd(b, a%b)
    	return gcd
    

print(calculate_gcd(5, 10))