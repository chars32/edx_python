def chicken_dogs(heads, legs):
    dogs_legs = 4
    chicken_legs = 2
    menos_pollos = heads
    lista_final = []

    for x in range(0, heads+1):
        total_perros = dogs_legs*x
        total_chicken = chicken_legs*menos_pollos
        total = total_perros + total_chicken

        if total == legs:
            lista_final.append(menos_pollos)
            lista_final.append(x)
            return lista_final

        menos_pollos = menos_pollos-1

    
                

print(chicken_dogs(5,12)) #4,1
#print(chicken_dogs(2,6))  #1,1
#print(chicken_dogs(12,8)) #None
#print(chicken_dogs(9,23)) #None

