#Write a function that accepts a filename as input argument and reads the file and saves each line of the file as an element 
#in a list (without the new line ("\n")character) and returns the list. Each line of the file has comma separated values

# Type your code here
def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    final_list = []

    for x in data:
    	final_list.append(x.strip('\n'))
    return final_list

    file_pointer.close()


print(list_from_file('file_name.txt'))