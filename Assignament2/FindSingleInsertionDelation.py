def single_insert_or_delete(s1,s2):

	s1 = s1.lower()
	s2 = s2.lower()

	count = 0
	#si son de igual tamaño y son iguales
	if len(s1) == len(s2) and s1 == s2:

		return 0

	else:
		#si s1 es mayor que s2
		if len(s1) > len(s2):			

			for x in s1:

				delete_char = s1.replace(x, "") #remplazamos el valor de x por ""

				if delete_char == s2: #si son iguales retorna 1

					return 1

			return 2 #si no se cumple el for entonces retorna 2

		else:

			for x in range(97,123): #empezamos recorriendo x en los valores de la tabla de valores

				copy_s1 = s1 

				copy_s1 = copy_s1+chr(x) #agregamos el valor de chr(x) al final de copy_s1

				copy_s1 = "".join(sorted(copy_s1)) #ordenamos los caracteres en la copy_s1

				copy_s2 = "".join(sorted(s2)) #ordenamos los caracteres de s2 en la copy_s2

				if copy_s1 == copy_s2:

					return 1

			return 2




print(single_insert_or_delete('programing', 'programming'))