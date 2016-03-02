def crazy_list(some_list):
    large = len(some_list)
    for x in some_list:
        if x == some_list[large-1]:
            return True
        else:
            return False
        
        large = large-1
            

print(crazy_list([5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]))
