#Write a function that accepts a dictionary as input which contains the names and grades of students (The keys are student names 
#and the values are lists of grades for 3 exams (1 Dimensional list)) and returns the list of names for those students whose 
#grade on all three exams is greater than or equal to 78.

dictionary = {'Hectar': [80, 50, 0], 'John': [70, 80, 85], 'Undertaker': [90, 92, 93], 'Priest': [75, 78, 83], 'Henry': [80, 85.2, 88]}

def list_as_values(dictionary):

	good_grades = []

	for x in dictionary:

		count = 0

		for z in dictionary[x]:

			if z >= 78:
				
				count += 1

		if count == 3:

			good_grades.append(x)

	return good_grades


print(list_as_values(dictionary))