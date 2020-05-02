""" Write a method frequent_letters that takes in a string and returns an array containing the characters that appeared more than twice in the string. """
def frequent_letters(string):
    dict1 = {}
    list1 = []
    for i in string:
        dict1[i] = string.count(i)
    #print(dict1)
    for keys,values in dict1.items():
        if values > 2:
            list1.append(keys)
    return list1

print(frequent_letters('mississippi'))  # => ["i", "s"] 
print(frequent_letters('bootcamp'))  # => []
