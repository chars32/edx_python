#Write a function which accepts an input string and returns a string where
#the case of the characters are changed, i.e. all the uppercase characters are
#changed to lower case and all the lower case characters are changed to upper
#case. The non-alphabetic characters should not be changed.
#Do NOT use the string methods upper(), lower(), or swap().

def change_case(line):
    change = ""
    for x in line:
        if ord(x) in range(65, 91):
            mayus_num  = ord(x)
            change += chr(mayus_num+32)
        elif ord(x) in range(97, 123):
            minus_num = ord(x)
            change += chr(minus_num-32)
        else:
            change += x
    return change

print(change_case("The Happy Gilmore 124 % &"))
