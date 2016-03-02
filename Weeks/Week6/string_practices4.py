#Write a function that accepts a string and a character as input and returns the
#number of times the character is repeated in the string. Note that
#capitalization does not matter here i.e. a lower case character should be
#treated the same as an upper case character.

def count_character(line, character):
    count = 0
    for x in line.lower():
        if x == character.lower():
            count += 1

    return count

print(count_character('supernovas are so awesome', 's'))
