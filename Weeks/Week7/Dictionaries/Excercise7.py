#Write a function that takes a string of words as input argument and returns a dictionary of word counts. 
#The keys of this dictionary should be the unique words and the values should be the total count of those words. 
#Assume that characters are not case sensitive.

#argument = "I am tall when I am young and I am short when I am old" 
argument = 'I love that fact that I am in love with python'

def dictionary_word_count(argument):

	argument = argument.lower()
	argument = argument.split()
	
	dictionary = {}
	keys_list = []

	for x in argument:
		if x not in keys_list:
			keys_list.append(x)

	for x in keys_list:
		if x in argument:
			dictionary[x] = argument.count(x)

	return dictionary

print(dictionary_word_count(argument))