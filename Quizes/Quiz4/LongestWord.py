#Write a function named find_longest_word that receives a string as parameter and returns the longest word in the string. 
#Assume that the input to this function is a string of words consisting of alphabetic characters that are separated by space(s). 
#In case of a tie between some words return the last one that occurs.

def find_longest_word(some_string):

	out_spaces = some_string.split()
	current_valor = 0
	final_word = ""



	for x in out_spaces:

		if len(x) >= current_valor:

			final_word = x

			current_valor = len(x)

	return final_word



k = find_longest_word("hola bebe como haaaaaaaaaaaas estado")

print(k)