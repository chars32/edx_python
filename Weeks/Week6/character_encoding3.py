def sum_characters(word):

    total = 0

    for x in word:

        total += ord(x)

    print(total)

sum_characters("hello")
