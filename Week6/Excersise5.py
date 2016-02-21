#Write a program that asks the user for an input 'n' (assume that the user enters a positive integer)
#and prints only the boundaries of the triangle using asterisks "*" of height 'n'.

n = int(input("Give me a number: "))

if n > 1:

    #imprimimos la linea de arriba, la que esta completa
    print('*'*n)

    #empezamos a imprimir las lineas siguientes
    for x in range(n-1, 1, -1):
        print ('*'+(x-2)*' '+'*')

    #por ulitmo imprimos la ulitma linea
    print('*')

else:
    print('*')
