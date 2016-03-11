#Write a function named my_final_grade_calculation that receives a file name and returns a dictionary 
#that tells whether a student in this course passed or failed based on the following criteria. 

def my_final_grade_calculation(filename):
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

	#--------------------------------------------
	dictionary = {}

	for element in list_of_lists: #start running elements of list of lists
		sort_quizes = []
		sort_assignments = []

		for quiz in range(1,7): #get the values of quizes sorted less to more
			sort_quizes.append(int(element[quiz]))
		sort_quizes.sort()

		for assignment in range(7,11): #get the values of assginments sorted less to more
			sort_assignments.append(int(element[assignment]))
		sort_assignments.sort()

		max_quizes = sort_quizes[2:] #split the sort_quizes from position 2 to end
		max_assignments = sort_assignments[1:] #split the sort_assignment from position 1 to end
		midterm = int(element[11])
		final = int(element[12])

		#get the average of each student
		average = ((sum(max_quizes)/4)*.25) + ((sum(max_assignments)/3)*.25) + (midterm*.25) + (final*.25)
		average = "{0:5.2f}".format(average)

		if float(average) >= 60:
			dictionary[element[0]] ="pass"
		else:
			dictionary[element[0]] ="fail"

	return dictionary


print(my_final_grade_calculation('archivodos.txt'))
