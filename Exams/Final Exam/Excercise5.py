def MY_2D_LIST(number):

	#first fill the 2d list without final values
	fill_list=[]	
	if number >= 1:
		for x in range(1, number+1):
			aux_list = []
			if x == 1:
				aux_list.append(1)
			else:
				for y in range(0, x):
					aux_list.append(1)
			fill_list.append(aux_list)

	#second make the logic to fill the 2d list with 
	#the desire values
	final_list =[]	
	for n in fill_list:
		if len(n) == 1 or len(n) == 2:
			final_list.append(n)
		else:
			for z in range(1, len(n)-1):
				change = final_list[-1][z] + final_list[-1][z-1]
				n[z] = change
			final_list.append(n)


	return final_list

print(MY_2D_LIST(9))