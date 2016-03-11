#Write a function named my_final_grade_calculation that receives a file name and returns a dictionary 
#that tells whether a student in this course passed or failed based on the following criteria. 

def my_final_grade_calculation(filename):
	file_pointer = open(filename, 'r')
	data = file_pointer.readlines()
	
	no_return_list = []
	for item in data:
		no_return_list.append(item.strip('\n'))

	list_of_lists = []
	for x in no_return_list:
		list_of_lists.append(x.split(','))

	#--------------------------------------------
	dictionary = {}
	for element in list_of_lists:
		name = element[0]
		avg_quizes = 0
		avg_assignment = 0

		for quiz in range(1, 7):
			avg_quizes += int(element[quiz])

		for assignment in range(7, 11):
			avg_assignment += int(element[assignment])

		average_final = (avg_quizes*.25 + avg_assignment*.25 + int(element[11]) + int(element[12]))/4

		if int(average_final) >= 60:
			dictionary[name] = 'pass'
		else:
			dictionary[name] = 'fail'

	return dictionary




print(my_final_grade_calculation('archivo.txt'))
