#Write a function which returns the number of words in the input string which have more than 4 characters. 
#Assume that the input string consists of alphabetic characters separated by spaces and capitalization does 
#not matter i.e. an upper case character should be treated the same as a lower case character.

def number_words(line):

	line = line.split()

	count = 0

	for x in line:

		if len(x) > 4:

			count += 1

	return count 

k = number_words("hello my friend and hello to you")
print (k)