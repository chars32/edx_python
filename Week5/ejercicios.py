a = [10,5,2,8,1]

def _custom_bubble_sort_sample_(original_list):
    
    my_list = original_list[:]  
    length = 0
    
    for element in my_list:
        length = length + 1
    unsorted = True
    
    while unsorted:
        unsorted = False
        for index in range(0, length-1):
            if my_list[index] > my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable
                unsorted = True
    return my_list

y = _custom_bubble_sort_sample_(a)
print(y)
