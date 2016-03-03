#Write a function that accepts a dictionary as input and returns a sorted list of all the keys in the dictionary.

dictionary = {"juan": 1, "pedro": 2, "carlos": 3}

def sorted_keys(dictionary):

	algo = list(dictionary.keys())

	algo.sort()

	return algo




print(sorted_keys(dictionary))