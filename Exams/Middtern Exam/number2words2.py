n = int(input('please enter an integer between 1 and 9999: '))

tostring = str(n)

one_number = ["one", "two", "three", "four", "five", "six", "seven", "eight",
              "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
two_numbers = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
               "eighty", "ninety"]

lista_numeros = []

lista_final = []


for x in tostring:
    lista_numeros.append(x)

#----------------------------------------------------

def pintar_numero(numero, one_number):
    numero = int(numero)
    if numero > 0:
        return one_number[numero-1]

def pintar_dos(num1, two_numbers):
    decen = two_numbers[num1-2]
    return decen

#--------------------------------------------------
    
while lista_numeros:
              
    if len(lista_numeros)==4:
        numero = lista_numeros[0]
        n = pintar_numero(numero, one_number)
        if n:
            lista_final.append(n)
            lista_final.append("thousand")
            #print (n, "thousand", end="")
              
    elif len(lista_numeros)==3:
        numero = lista_numeros[0]
        n = pintar_numero(numero, one_number)
        if n:
            lista_final.append(n)
            lista_final.append("hundred")
            #print (n, "hundred", end="")
        
    elif len(lista_numeros)==2:
        numero = int(lista_numeros[0]+ lista_numeros[1])
        if numero <= 19 and numero > 0:
            n = pintar_numero(numero, one_number)
            if n:
                lista_final.append(n)
                #print (n, end="")
            break

        elif numero > 19:
            num1 = int(lista_numeros[0])
            num2 = int(lista_numeros[1])
            n = pintar_dos(num1, two_numbers)
            n1 = pintar_numero(num2, one_number)
            if n:
                lista_final.append(n)
                #print (n, n1)

            if n1:
                lista_final.append(n1)
            break
                
        
    elif len(lista_numeros)==1:
        numero = lista_numeros[0]
        n = pintar_numero(numero, one_number)
        if n:
            lista_final.append(n)
            #print (n)
   
    lista_numeros.pop(0)

#---------------------------------------------------------

while lista_final:
    if len(lista_final)>1:
        print(lista_final[0], end=" ")
    else:
        print(lista_final[0])
    lista_final.pop(0)





        
