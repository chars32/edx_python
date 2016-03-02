#Write a function which accepts an input string and returns a string where every individual word in the input string is reversed and the case 
#for every single character is reversed. The input string for this function would be a sentence (words separated by spaces) consisting of 
#alphabetic characters.

def reverse_and_case(line):

	final = ""

	invert_case = line.swapcase()

	for x in invert_case:

		final = x + final

	return final


k = reverse_and_case("Hello World")
print(k)