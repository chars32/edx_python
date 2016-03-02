def my_encryption(some_string):

	character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
	secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
	encription = ""

	for x in some_string:
		count = 0
		for i in character_set:
			if i == x:
				encription += secret_key[count]
			count += 1

	return encription


k = my_encryption("Lets meet at the usual place at 9 am")
print(k)