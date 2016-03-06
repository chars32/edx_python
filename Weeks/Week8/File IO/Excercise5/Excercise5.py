def lastname_name_values(file_name):

	file_pointer = open(file_name, 'r')
	data = file_pointer.readlines()

	no_return_list = []
	for item in data:
		no_return_list.append(item.strip('\n'))

	list_of_lists = []
	for x in no_return_list:
		list_of_lists.append(x.split(','))

	dictionary = {}

	list_lastnames = []
	for item in list_of_lists:
		if item[1] not in list_lastnames:
			list_lastnames.append(item[1])
			dictionary[item[1]] = {}

	for x in list_lastnames:
		dict_aux = {}
		for y in list_of_lists:
			if x in y[1]:
				dict_aux[y[0]] =int(y[2])

		dictionary[x] = dict_aux

	return dictionary

print(lastname_name_values('excercise.txt'))