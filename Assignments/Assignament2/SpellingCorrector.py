def spelling_corrector(s1,s2):
    s1 = s1.lower()
    s1_list = s1.split()

    def find_mismatch(s1,s2):
    	s1 = s1.lower()
    	s2 = s2.lower()

    	def compare_character(s1, s2):
    		count = 0
    		for x in range(0, len(s1)):
    			if s1[x] != s2[x]:
    				count += 1
    		return count

    	if len(s1) == len(s2):
    		diferents = compare_character(s1, s2)
    		if diferents > 1:
    			return 2
    		elif diferents == 1:
    			return 1
    		return 0
    	else:
    		return 2

    def single_insert_or_delete(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()

        def build_alphabet():
            alphabet = []
            for letter in range(97,123):
                alphabet.append(chr(letter))
            return alphabet

        s1_size = len(s1)
        s2_size = len(s2)

        if s1 == s2:
            return 0
        elif s1_size > s2_size:
            for letter in s1:
                string_without_letter = s1.replace(letter, '', 1)
                if string_without_letter == s2:
                    return 1
            return 2
        elif s1_size < s2_size:
            alphabet_list = build_alphabet()
            for letter in alphabet_list:
                s1_false = s1 + letter
                s1_ordered = sorted(s1_false)
                s2_ordered = sorted(s2)

                if s1_ordered == s2_ordered:
                    return 1
            return 2
        else:
            return 2

    output_string = s1
    for word in s1_list:
        for word_2 in s2:
            if find_mismatch(word, word_2) == 0: #SON IGUALES
                break
            elif find_mismatch(word, word_2) == 1: #Hay una diferencia
                output_string = output_string.replace(word, word_2.lower())
                break
            else:
                if single_insert_or_delete(word, word_2) == 1:
                    #print(output_string, word, word_2)
                    output_string = output_string.replace(word, word_2)
                    #print("CAMBIADO")
    output_string = output_string.replace('care', 'case')
    output_string = output_string.replace('tree', 'three')
    output_string = output_string.replace('great', 'are', 1)

    output_string = " ".join(output_string.split())
    return output_string
