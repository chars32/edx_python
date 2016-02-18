import math
from math import *

a = [2, 3, -5] 
b = [4, -3, 12]

def funciona(a, b):
    y = ((b[0]-a[0])**2)+((b[1]-a[1])**2)+((b[2]-a[2])**2)
    return (sqrt(y))
algo = funciona(a,b)
print(algo)
