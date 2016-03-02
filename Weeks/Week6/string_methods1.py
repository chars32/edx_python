def right_whitespaces(words):

    for x in words:
        if x.isalpha():
            count =  words[words.index(x)]
            place = words.index(count)
            return words[place:len(words)]

print(right_whitespaces("    Hello  "))
