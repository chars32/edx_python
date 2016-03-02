def test_for_anagrams(my_string1, my_string2):
	lower_my_string1 = my_string1.lower()
	lower_my_string2 = my_string2.lower()

	sorted1 = "".join(sorted(lower_my_string1))
	sorted2 = "".join(sorted(lower_my_string2))

	if sorted1 == sorted2:
		return True 
	else:
		return False

k = test_for_anagrams("Orchestra", "Carthorese")
print(k)