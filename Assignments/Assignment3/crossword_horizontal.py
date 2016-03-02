#Write a function named find_word_horizontal that accepts a 2-dimensional list of characters (like a crossword puzzle) 
#and a string (word) as input arguments. This function searches the rows of the 2d list to find a match for the word. 
#If a match is found, this functions returns a list containing row index and column index of the start of the match, 
#otherwise it returns the value None (no quotations).

crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','d','o','g']]
word='cat'

def find_word_horizontal(crosswords,word):
	matches = []

	for item_list in crosswords:
		if word in "".join(item_list):
			matches.append(item_list)

	if matches:
		final_list = [crosswords.index(matches[0]), matches[0].index(word[0])]
	else:
		return None

	return final_list

print(find_word_horizontal(crosswords, word))