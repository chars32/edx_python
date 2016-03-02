def find_integer_with_most_divisors(input_list):
    list_temp =[]
    #primero encontramos el numero de divisores de los elementos de la lista
    for number in input_list:
        count = 0
        for x in range(1, number+1):
            if number%x == 0:
                count = count+1
        list_temp.append(count)
        
    num_repeat = max(list_temp)
    #segundo buscamos el valor mas alto, no importa que este duplicado
    posicion = 0
    list_final = []

    for x in list_temp:
        if x == num_repeat:
            list_final.append(input_list[posicion])
        posicion = posicion+1
    return (list_final[0])


    

print(find_integer_with_most_divisors([8,12,18,6]))
print(find_integer_with_most_divisors([10,30,20]))

            
