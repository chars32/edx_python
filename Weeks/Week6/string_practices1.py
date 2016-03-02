#Write a function that takes a string consisting of alphabetic characters as
#input argument and returns True if the string is a palindrome. A palindrome
#is a string which is the same backward or forward.
#Note that capitalization does not matter here i.e. a lower case character
#can be considered the same as an upper case character.

def palindromes(line):
    reverse = ""
    line = line.lower()
    for x in range(len(line)-1,-1,-1):
        reverse += line[x]

    return line == reverse


k = palindromes("Ana")
print (k)
