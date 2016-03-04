#Write a function that takes a string as input argument and returns a dictionary of vowel counts i.e. the keys of this dictionary 
#should be individual vowels and the values should be the total count of those vowels. You should ignore white spaces and they 
#should not be counted as a character. Also note that a small letter vowel is equal to a capital letter vowel.

argument =  "Murciealgooo ataca"

def dictionary_vowel_count(argument):

	vowels = ['a','e','i','o','u']

	dictionary = {}

	copy_argument = argument.replace(" ","")
	copy_argument = copy_argument.lower()

	for x in vowels:
		if x in copy_argument:
			dictionary[x] = argument.count(x)

	return dictionary

print(dictionary_vowel_count(argument))

