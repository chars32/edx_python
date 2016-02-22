#Write a function that takes a string consisting of alphabetic characters as input argument and returns the most common character. 
#Ignore white spaces i.e. Do not count any white space as a character. Note that capitalization does not matter here.
#In case of a tie between certain characters return the last character that has the most count

def _most_common_character_(sample_string):
    stripped_string = sample_string.replace(" ", "")   
    lowercase_stripped_string = stripped_string.lower()
    sample_character = None
    sample_maximum_count = 0

    for character in lowercase_stripped_string:
        each_character_count = lowercase_stripped_string.count(character)

        if each_character_count >= sample_maximum_count:
            sample_maximum_count = each_character_count
            sample_character = character
    return sample_character

k =_most_common_character_("Hello")
print(k)