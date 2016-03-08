def calculate_grades(filename):
	file_pointer = open(filename, 'r')
	data = file_pointer.readlines()

	no_return_list = []
	for item in data:
		no_return_list.append(item.strip('\n'))

	list_of_lists = []
	for x in no_return_list:
		list_of_lists.append(x.split(','))
	#-----------------------------------------
	final_tuple = []
	for z in list_of_lists:
		aux_list = []
		sum_index = 0
		aux_list.append(z[0])
		for x in z[1:]:
			sum_index += int(x)
		aux_list.append(sum_index/4)
		final_tuple.append(tuple(aux_list))

	final_tuple.sort()
	return tuple(final_tuple)

print(calculate_grades('archive.txt'))