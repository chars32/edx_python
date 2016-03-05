#Write a function that accepts a filename(string) of a CSV file which contains the information about student's names 
#and their grades for four courses and returns a dictionary of the information. The keys of the dictionary should be 
#the name of the students and the values should be a list of floating point numbers of their grades.

def file_to_dictionary(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()

    #---------------------------------------
    #first takeout the '\n' string and save in a list
    no_return_list = []

    for x in data:
    	no_return_list.append(x.strip('\n'))
    #---------------------------------------
    #second made a list with four lists inside
    #each of the four lists with their elements
    list_of_list = []

    for element in no_return_list:
    	list_of_list.append(element.split(','))

    #---------------------------------------
    #finally save it on a dictionary
    dictionary = {}

    for lists in list_of_list:
    	name = ""
    	grades_list = []

    	for item in lists:
    		if lists.index(item) == 0:
    			name = item
    		else:
    			grades_list.append(float(item))
    	
    	dictionary[name] = grades_list

    return dictionary

print(file_to_dictionary('excercise2.txt'))