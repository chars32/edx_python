#Write a program using while loops that asks the user for a positive integer 'n' and prints 
#a triangle using numbers from 1 to 'n'.

number = int(input("Give me a number: "))

count = 0

for x in range(1, number+1):
	count += 1
	dibujar = str(x)
	print (dibujar*count)

