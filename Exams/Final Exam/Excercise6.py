def reverse_dictionary(input_dict):

	list_value = []
	dictionary = {}

	for key_dict in input_dict:
		for value in input_dict[key_dict]:
			if value not in list_value:
				list_value.append(value.lower())


	for value in list_value:
		list_aux = []
		for key in input_dict:
			for item in input_dict[key]:
				if item.lower() == value:
					list_aux.append(key.lower())
					list_aux.sort()
		dictionary[value] = list_aux
	return dictionary


#print(reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 
#	'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))
print(reverse_dictionary({'astute': ['Smart', 'clever', 'talented'], 
	'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'talented': ['smart', 'keen', 'Bright'], 
		'smart': ['clever', 'bright', 'talented']}))