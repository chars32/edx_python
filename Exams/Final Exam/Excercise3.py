#Write a function named n_letter_dictionary that receives a string (words separated by spaces)
#as parameter and returns a dictionary whose keys are numbers and whose values are lists that 
#contain unique words that have the number of letters equal to the keys. 

def n_letter_dictionary(argument):
	argument = argument.lower()
	list_argument = argument.split()
	dictionary = {}

	no_repeat_list = [] #palabras sin repetirse
	len_element_list = [] #len de las palabras sin repetirse
	for element in list_argument:
		if element not in no_repeat_list:
			no_repeat_list.append(element)
			len_element_list.append(len(element))

	no_repeat_number_list = []
	for number in len_element_list:
		if number not in no_repeat_number_list:
			no_repeat_number_list.append(number)
	no_repeat_number_list.sort()

	for key_number in no_repeat_number_list:
		aux_list = []
		for word in no_repeat_list:
			if len(word) == key_number:
				aux_list.append(word)
			aux_list.sort()
		dictionary[key_number] = aux_list

	return dictionary



#print(n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become"))
print(n_letter_dictionary("I loved a girl once"))