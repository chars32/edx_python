
vector = [2,3,-4]

def magnitud(vector):
    paso_uno = 0
    for x in vector:
       paso_uno = paso_uno + x**2
    return paso_uno**(1/2)
magna = magnitud(vector)
def magna_cada_uno(vector):
    resultante = []
    for x in vector:
        resultante.append(x/magna)
    return resultante

print(magna_cada_uno(vector))
       
