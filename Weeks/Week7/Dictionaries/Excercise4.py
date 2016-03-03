#Write a function which accepts a dictionary and an integer as input and returns an ascending sorted list 
#of all the keys whose values contain the input value. Note that the keys of this dictionary are strings 
#while the values of this dictionary are 1 Dimensional lists of integers

dictionary = {"rabbit" : [1, 2, 3],
          	  "kitten" : [2, 2, 6],
          	  "lioness": [6, 8, 9]}

#dictionary = {'Hyena': [12, 3, 0], 
#			 'lioness': [6, 8, 9], 
#			  'rabbit': [1, 2, 3], 
#			  'kitten': [2, 2, 6]}

number = 2

def value_containing_key(dictionary, number):

	final_list = []

	list_keys = list(dictionary.keys())  # 4
	len_values = 0

	for name in list_keys:

		len_values = len(dictionary[name]) #3

	for x in range(len_values):
		for y in list_keys:

			if dictionary[y][x] == number:
				if y not in final_list:
					final_list.append(y)

	return final_list


#print(value_containing_key(dictionary, number))

print(value_containing_key(dictionary, number))