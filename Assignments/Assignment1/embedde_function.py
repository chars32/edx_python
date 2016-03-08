def embedded_function(a, b):
    # first find the sum of the two numbers
    my_sum = a + b

    # write a function that accepts a number as parameter and
    # returns True or False
    def lets_test_for_even(n):
        if n % 2 == 0:
            return True
        else:
            return False

    # Now here is the important part!
    # you need to call your inner function from within the outer function
    my_result = lets_test_for_even(my_sum) 
    # Now return the result
    return my_result

print(embedded_function(3,4))

