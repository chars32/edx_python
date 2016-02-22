#Write a function that takes a list of words as an input argument and returns
#True if the list is sorted and returns False otherwise.

def sorted(line):
    lista1 = []
    lista2 = []
    for x in line:
        lista1 += (x[0])
        lista2 += (x[0])

    lista2.sort()
    return lista1 == lista2

k = sorted(['c', 'java', 'matlab', 'python'])
print(k)
