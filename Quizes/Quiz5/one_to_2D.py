#Write a function named one_to_2D which receives an input list and two integers r and c as parameters and returns a 
#new two-dimensional list having r rows and c columns. 
#Note that if the number of elements in the input list is larger than r*c then ignore the extra elements. 
#If the number of elements in the input list is less than r*c then fill the two dimensional list with the keyword None.

def one_to_2D(some_list, r, c):
	mult_rc = r*c
	some_list_aux = []
	list_aux = []
	final_list = []

	#------------------------------------
	#first we compare is the leng of the list is greather or equal than the multiplication
	#of r*c if yes we split the list to fix it.
	if len(some_list) >= mult_rc:
		some_list_aux = some_list[:mult_rc]
	#if the len of the list is less thant the multiplication r*c then we fill the spaces
	#with None string
	else:
		some_list_aux = some_list
		for x in range(len(some_list_aux), mult_rc):
			some_list_aux.append(None)
	print(some_list_aux)
	#-------------------------------------

	for x in some_list_aux:
		list_aux.append(x)
		if len(list_aux) == c:
			final_list.append(list_aux)
			list_aux = []

	return final_list

print(one_to_2D([1, 2, 3, 4], 3, 4))