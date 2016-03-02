def divisors(number):
    lista = []
    if number%2 == 0:
        for n in range(1,number+1):
            if number%n == 0:
                lista.append(n)
    else:
        for n in range(1, number+1):
            if number%n == 0:
                lista.append(n)
    return lista

y = divisors(4)
print(y)
