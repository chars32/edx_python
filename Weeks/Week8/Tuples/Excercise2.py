def keys_tuples(dictionary):
    keys = tuple(dictionary.keys())
    values = tuple(dictionary.values())
    return keys, values

print(keys_tuples(dictionary = {1:"a", 2:"b", 3:"c", 4:"d"}))