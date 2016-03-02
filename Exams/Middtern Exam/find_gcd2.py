def find_gcd(some_list):
  
  #se obtienen todos los divisores en una lista ordenada
  def divisors(some_list):
    divisores =[]
    for x in some_list:
      for y in range(1, x+1):
        if x%y == 0:
          divisores.append(x//y)
      divisores.sort()
    return divisores

  #se obtiene los divisores sin repetirse
  def search_destroy(divisores_ordenados):
    lista = []
    for x in divisores_ordenados:
      if x not in lista:
        lista.append(x)
    return lista

  #se obtiene una lista para saber cuantas veces se repiten los numeros
  def maximo(a,b):
    lista = []
    for x in a:
      count = 0
      for y in b:
        if x == y:
          count = count+1
      lista.append(count)
    return lista

  #se compara que los elementos de la lista maxi sean iguales al num_maximo
  #y de ser asi, se obtiene la posicion en la lista 'una_sola'
  def buscando(maxi):
    num_maximo = max(maxi)
    count = 0
    lista = []
    if num_maximo > 1:
      for x in maxi:
        if x == num_maximo:
          lista.append(una_sola[count])
        count = count+1
    else:
      return 1
    return max(lista)
        
     

  divisores_ordenados = divisors(some_list)
  una_sola = search_destroy(divisores_ordenados)
  maxi = maximo(una_sola, divisores_ordenados)
  final = buscando(maxi)
  return final
  


print(find_gcd([12,24,6,18]))
#print(find_gcd([3, 5, 9, 11, 13]))
