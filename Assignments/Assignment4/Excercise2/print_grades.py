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


# Your main program starts below this line
def print_grades(file_name):
    # Call your create_grades_dict() function to create the dictionary
    grades_dict=create_grades_dict(file_name)
    
    #formatting and printing header 
    header_list = ["ID", "Name", "Test_1", "Test_2", "Test_3", "Test_4", "Avg."]
    print("{0: ^10} | {1: ^16} | {2: ^6} | {3: ^6} | {4: ^6} | {5: ^6} | {6: ^6} |".format(header_list[0], header_list[1], header_list[2],
    																header_list[3], header_list[4], header_list[5], header_list[6]))
    #converting tuple in list
    keys_order_list = list(grades_dict.keys())
    keys_order_list.sort()

    ordered_list = []
    for key in keys_order_list:
    	aux_list = [key]
    	for item in grades_dict[key]:
    		aux_list.append(item)
    	ordered_list.append(aux_list)

    #formatting and printing body
    for listed in ordered_list:
    	print("{0:10s} | {1:16s} | {2:6d} | {3:6d} | {4:6d} | {5:6d} | {6:6.2f} |".format(listed[0], listed[1], listed[2], 
    																	listed[3], listed[4], listed[5], listed[6]))
print(print_grades('archivo.txt'))