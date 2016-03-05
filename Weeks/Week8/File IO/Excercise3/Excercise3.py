#Write a function that takes a file name (string) of a CSV file which contains the information about student's names 
#and their grades for four courses and returns a dictionary that contains information about the students whose grades 
#in both Math and Chemistry is above 70. Note that if the file has any comments (lines starting with #) then you 
#should ignore such a line. 

def math_and_chemistry(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()

    no_return_list = []
    for item in data:
    	no_return_list.append(item.strip('\n'))

    list_of_lists = []
    for x in no_return_list:
    	list_of_lists.append(x.split(','))

    dictionary = {}
    for items in list_of_lists:
    	if int(items[1]) > 70 and int(items[3]) > 70:
    		list_aux = []
    		for x in range(1, len(items)):
    			list_aux.append(float(items[x]))
    		dictionary[items[0]] = list_aux

    return dictionary


print(math_and_chemistry('list_grades.txt'))