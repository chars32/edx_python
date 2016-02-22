#Write a function that accepts a string of words separated by spaces consisting of alphabetic characters and returns a string such that each
#word in the input string is reversed while the order of the words in the input string is preserved. 

def preserve_and_reverse(line):

	line_split = line.split()

	final = ""

	count = 0

	for x in line_split:

		if line_split[count] != line_split[-1]:

			for i in range(len(x)-1, -1, -1):

				final += x[i]

			final += " "

			count += 1

		else:

			for i in range(len(x)-1, -1, -1):

				final += x[i]