def pattern_sum(a, b):
    convert = str(a)
    suma = 0
    for x in range(1, b+1):
        suma = suma + int(convert*x)
    return suma
        

print(pattern_sum(5,3))
