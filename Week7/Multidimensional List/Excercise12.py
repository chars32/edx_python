#Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product. 
#Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is the 
#same as the number of rows of the second matrix(b). Do NOT use numpy module for this exercise. The input for this 
#function will be two 2 Dimensional lists.

def mult_matrix_without_numphy(a, b):
    if len(a[0]) != len(b):
        return None
    # Creamos la matriz como debe quedar pero rellena de 0
    # esto lo hacemos para poder utilizar los indexes mas adelante
    output_list=[]
    temp_row=len(b[0])*[0]
    
    for r in range(len(a)):
        output_list.append(temp_row[:])

    #----------------------------------------------------------------
    
    for row_index in range(len(a)): #Recorremos el len(a)

        for col_index in range(len(b[0])): #Recorremos en len(b), pero solo en el primer elemento
            sum=0

            for k in range(len(a[0])): #Recorremos el len(a), pero solo en el primer elemento

            	sum=sum+a[row_index][k]*b[k][col_index]

            output_list[row_index][col_index]=sum #aqui es donde usamos los indices de la matriz que 
            									  #hicimos mas arriba
    return output_list

a = [[2, 3, 4],
     [3, 4, 5]]

b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(mult_matrix_without_numphy(a,b))