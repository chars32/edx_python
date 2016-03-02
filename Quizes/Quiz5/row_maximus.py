def row_maximums(some_multi_dimensional_list):
	dictionary = {}
	count = 0

	for row in some_multi_dimensional_list:
		max_value = 0
		for col in row:
			if col > max_value:
				max_value = col
		dictionary ["row "+str(count)+" max"] = max_value
		count += 1
	return dictionary