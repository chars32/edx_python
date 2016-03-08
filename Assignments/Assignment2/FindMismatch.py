#Write a function named find_mismatch that accepts two strings as input arguments and returns:

#0 if the two strings match exactly.
#1 if the two strings have the same length and mismatch in only one character.
#2 if the two strings do not have the same length or mismatch in two or more characters.

def find_mismatch(s1,s2):

	s1 = s1.lower()
	s2 = s2.lower()

	#-------------------------------------------
	# function that sum one to 'count' everytime
	# caracther of s1 and s2 are differents
	#-------------------------------------------

	def compare_character(s1, s2):
		count = 0
		for x in range(0, len(s1)):
			if s1[x] != s2[x]:
				count += 1
		return count 

	#---------------------------------------

	if len(s1) == len(s2):
		diferents = compare_character(s1, s2)
		if diferents > 1:
			return 2
		elif diferents == 1:
			return 1
		return 0
	else:
		return 2


k = find_mismatch("Venecia", "venecia")
print(k)

 