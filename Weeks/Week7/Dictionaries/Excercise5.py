#Write a function that takes a string as input argument and returns a dictionary of letter counts 
#i.e. the keys of this dictionary should be individual letters and the values should be the total count of those letters. 
#You should ignore white spaces and they should not be counted as a character. 
#Also note that a small letter character is equal to a capital letter character.

argument = "This is my house"

def dictionary_of_letters_count(argument):

	dictionary = {}

	copy_argumnent = argument.replace(" ","")

	copy_argumnent = copy_argumnent.lower()

	keys_list = []

	for letter in copy_argumnent:

		if letter not in keys_list:

			keys_list.append(letter)

	for key in keys_list:

		dictionary[key] = copy_argumnent.count(key)

	return dictionary


print(dictionary_of_letters_count(argument))