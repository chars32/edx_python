#Write a function which accepts an input string consisting of alphabetic
#characters and returns the string with all the spaces removed.
#Do NOT use any string methods for this problem.

def remove_spaces(line):
    final_line = ""
    for x in line:
        if x != " ":
            final_line += x

    return final_line

print(remove_spaces("The Hobbit es una muy buena pelicula"))
