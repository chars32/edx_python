#Write a function that accepts a filename as input argument, the file contains the information about a persons 
#expenses on milk and bread and returns a dictionary that contains exactly the strings 'milk' and 'bread' as 
#the keys and their floating point values in a list as values. Each line of the file may start with a 'm' or a 'b' 
#denoting milk or bread respectively.

def milk_and_break(file_name):
	file_pointer = open(file_name, 'r')
	data = file_pointer.readlines()

	no_return_list = []
	for item in data:
		no_return_list.append(item.strip('\n'))

	list_of_lists = []
	for x in no_return_list:
		list_of_lists.append(x.split(' '))

	#------------------------------------------
	out_dict={}
	out_dict["milk"] =[]
	out_dict["bread"] =[]

	milk_list = []
	bread_list = []
	for item in list_of_lists:
		aux_m = []
		aux_b = []

		if item[0] == 'm':
			for x in range(1, len(item)):
				aux_m.append(float(item[x]))
			milk_list.append(aux_m)

		elif item[0] == 'b':
			for x in range(1, len(item)):
				aux_b.append(float(item[x]))
			bread_list.append(aux_b)

	out_dict['milk'] = milk_list
	out_dict['bread'] = bread_list

	return out_dict

print(milk_and_break('excercise.txt'))