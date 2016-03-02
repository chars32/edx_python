#Write a function which returns the total number of vowels in an input string
#which consists of alphabetic characters. Note that capitalization does not
#matter here i.e. a lower case character should be considered the same as an
#upper case character. For this problem, the vowels are considered
#to be A, E, I, O, U.

def count_vowels(line):

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for x in line.lower():
        if x in vowels:
            count += 1
    return count

print(count_vowels("MUrciElAgO"))

