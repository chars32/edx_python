#Write a function named list_to_tuples that receives a two dimensional list of strings as parameter 
#and returns a tuple of tuples where the content of each inner list is reversed

MY_LIST = [['mean', 'really', 'is', 'jean'], ['world', 'my', 'rocks', 'python']]

def list_to_tuples(MY_LIST):
	final_tuple=[]
	for lists in MY_LIST:
		lists.reverse()
		final_tuple.append(tuple(lists))
	
	return tuple(final_tuple)

print(list_to_tuples(MY_LIST))
