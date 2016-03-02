def left_whitespaces(words):
    letter = ""
    for x in words:
        if x.isalpha():
            letter = x
    return words[0:words.index(letter)+1]

print(left_whitespaces("  Hello       "))
#print(left_whitespaces("Hello"))
