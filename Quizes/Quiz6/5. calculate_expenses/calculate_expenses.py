def calculate_expenses(filename):
	file_pointer = open(filename, 'r')
	data = file_pointer.readlines()

	no_return_list = []
	for item in data:
		no_return_list.append(item.strip('\n'))

	no_spaces_list =[]
	for item in no_return_list:
		no_spaces_list.append(item.replace(' ',''))

	list_of_lists = []
	for x in no_spaces_list:
		list_of_lists.append(x.split(','))
	#-----------------------------------------------
	products_names_list = []
	for product in list_of_lists:
		if product[0] not in products_names_list:
			products_names_list.append(product[0])
	products_names_list.sort()

	expenses_list = []
	for name in products_names_list:
		sum_prices = 0
		aux_list = []
		for item in list_of_lists:
			if item[0] == name:
				sum_prices += float(item[1])
		aux_list.append(name)
		aux_list.append("${:.2f}".format(sum_prices))
		expenses_list.append(tuple(aux_list))

	return expenses_list

print(calculate_expenses('archive.txt'))