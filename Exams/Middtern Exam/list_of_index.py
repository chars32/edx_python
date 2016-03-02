def list_of_primes(n):

    list_primes = []

    #Funcion que verifica que UN numero sea primo
    def is_prime(n):
        count = 0
        for x in range(2, n+1):
            if n%x == 0:
                count = count +1
        if count > 1:
            return False
        else:
            return True

    #en base al numero dado recorremos una lista desde 2 hasta al numero n
    #y le pasamos a la funcion is_prime el valor de x para saber si es primo
    
    for x in range(2,n):
        verif = is_prime(x)

        if verif:
            list_primes.append(x)
    

    return list_primes
            
        

print(list_of_primes(100))
