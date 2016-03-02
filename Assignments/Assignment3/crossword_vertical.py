#Write a function named find_word_vertical that accepts a 2-dimensional list of characters (like a crossword puzzle) 
#and a string (word) as input arguments. This function searches the columns of the 2d list to find a match for the word. 
#If a match is found, this functions returns a list containing row index and column index of the start of the match, 
#otherwise it returns the value None (no quotations).

crosswords=[['s','d','o','g'],
	    ['c','u','c','m'],
	    ['a','c','a','t'],
	    ['t','e','t','k']]
word='cat'

def find_word_vertical(crosswords,word):
	column_list = []
	column_number = []
	matches = []
	count = 0

	for x in range(len(crosswords)):
		aux_list = []
		for y in range(len(crosswords[x])):
			aux_list.append(crosswords[y][x])
		column_list.append(aux_list)


	for item_list in column_list:
		if word in "".join(item_list):
			matches.append(item_list)
			column_number.append(count)
		count += 1

	if matches:
		final_list = [matches[0].index(word[0]), column_number[0]]
	else:
		return None

	return final_list



print(find_word_vertical(crosswords,word))
