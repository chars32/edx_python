def create_grades_dict(file_name):
	file_pointer = open(file_name, 'r')
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

	#----------------------------------------------
	tests_list=['Test_1', 'Test_2', 'Test_3', 'Test_4']
	dictionary = {}

	#making the structure of the dictionary
	for student_id in list_of_lists:
		dictionary[student_id[0]] = [student_id[1], 0, 0, 0, 0, 0]

	#average calculated and saved to dictionary position
	for lists in list_of_lists:
		average = 0
		for x in range(2, len(lists)):
			if lists[x] in tests_list:
				position_number = tests_list.index(lists[x])+1
				dictionary[lists[0]][position_number] = int(lists[x+1])
				average += int(lists[lists.index(lists[x])+1])
		dictionary[lists[0]][5] = average/4

	return dictionary

print(create_grades_dict('students_grade.txt'))
#{'1000123456': ['Rubble', 0, 0, 80, 80, 40.0], '1000123459': ['Chipmunk', 86, 0, 0, 96, 45.5]}