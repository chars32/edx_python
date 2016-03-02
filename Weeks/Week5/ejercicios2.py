def add_odd(lis):
    new_lis=[]
    for x in lis:
        if x%2 != 0:
            x = x+1
            new_lis.append(x)
        else:
            new_lis.append(x)
    return new_lis
    

lista=[12, 3, 4, 5, 6]

y = add_odd(lista)
print (y)
