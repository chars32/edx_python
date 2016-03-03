#Write a function that accepts a dictionary as input and returns a sorted list of all the values in the dictionary. 
#Assume that the values of this dictionary are just integers.

dictionary = {"juan": 3, "pedro": 1, "carlos": 2}

def sorted_values(dictionary):

	algo = list(dictionary.values())

	algo.sort()

	return algo

print(sorted_values(dictionary))