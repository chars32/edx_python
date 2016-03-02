#Write a function that accepts a string and a character as input and returns the
#count of all the words in the string which start with the given character. 

def repeat(line, character):
    line1 = line.lower()
    line2 = line1.split()
    count = 0

    for x in line2:
        if x.startswith(character.lower()):
            count += 1
    return count

k = repeat('Supernovas are so awesome', 's')
print(k)
