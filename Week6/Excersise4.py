#Write a program that asks the user for an input 'n' and prints a square of n by n asterisks "*". 

number = int(input("Give me a number: "))

line = '*'*number

for x in range(0, number):
	print (line)