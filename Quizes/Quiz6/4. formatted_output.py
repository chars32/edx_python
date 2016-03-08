def formatted_print(arguments):

	values_list= list(arguments.values())
	values_list.sort()
	values_list.reverse()

	for value in values_list:
		for argument in arguments:
			if arguments[argument] == value:
				print("{0:10s}{1:6.2f}".format(argument, value))

#argument = {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900} 
argument = {'vader': 40, 'troy': 84.5, 'puma': 98.5, 'darth': 78.9, 'kevin': 88.454}
print(formatted_print(argument))



