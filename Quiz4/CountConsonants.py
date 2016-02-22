#Write a function named count_consonants that receives a string as parameter and returns the total count of the consonants in the string. 
#Consonants are all the characters in the english alphabet except for 'a', 'e', 'i', 'o', 'u'. If the same consonant repeats multiple 
#times you should count all of them.

def count_consonants(some_string):

	vowels = ['a', 'e', 'i', 'o', 'u']
	lower_case = some_string.lower()
	espaces_out = lower_case.replace(" ", "")
	count = 0

	for x in espaces_out:

		if x not in vowels:

			count += 1

	return count

k = count_consonants("This Quiz Is So Easy Ha Ha Ha")
print(k)
