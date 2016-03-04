#Write a function that takes an integer as input argument and returns the integer using words. 
#For example if the input is 4721 then the function should return the string "four seven two one". 
#Note that there should be only one space between the words and they should be all lowercased in the string that you return.

number = 4722

def number_to_words(number):
	
	word_numbers = ["zero","one", "two", "three", "four", "five", "six", "seve", "eight", "nine"]

	number = str(number)

	list_words = []

	final_list = ""

	count = 0

	for x in number:
		list_words.append(word_numbers[int(x)])

	for y in list_words:

		if count == len(list_words)-1:
			final_list += y
		else:
			final_list += y + " "
		count += 1

	return final_list

print(number_to_words(number))