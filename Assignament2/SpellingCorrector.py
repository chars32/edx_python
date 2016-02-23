def spelling_corrector(s1,s2):

	s1 = s1.lower()
	s1 = s1.split()
	output_list=[]

#---------------------------------------------

	def compare(x,y):
		count = 0
		for i in range(0, len(x)):
			if x[i] != y[i]:
				count += 1
		return count

	def insertion(x,y):
		for i in range(97,123):
			copyx = x
			copyx = x+chr(i)
			if copyx == y:
				return True

	def delete(x,y):
		last = x[-1]
		copyx = x.replace(last, "")
		if copyx == y:
			return True

	def replacing(x,y):
		for i in x:
			for z in range(97,123):
				copyx = x.replace(i, chr(z))
				if copyx == y:
					return True

#---------------------------------------------

	for x in s1:
		for y in s2:
	 		if len(x) == len(y):
	 			compare_words = compare(x,y)
	 			if compare_words == 2 or compare_words == 0:
	 				output_list.append(x)
	 				s1.remove(x)

	print(s1, s2)




#----------------------------------------------

	return output_list

print(spelling_corrector("Thes is the Firs cas", ['that','first','case','car']))
#print(spelling_corrector("programing is fan and eesy", ['programming','this','fun','easy','book' ]))
#thes is the first case
