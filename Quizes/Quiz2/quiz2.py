numero = int(input("Number: "))

dias = int(numero/86400)
dias_sobra = int(numero%86400)
horas = int(dias_sobra/3600)
horas_sobra = int(dias_sobra%3600)
minutos = int(horas_sobra/60)
segundos = int(horas_sobra%60)
print (dias, "days", horas, "hours", minutos, "minutes", segundos, "seconds")


    
