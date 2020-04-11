""" Write a method select_long_words(words) that takes in an array of words and returns a new array containing all of the words of the original array that are longer than 4 characters. """
def select_long_words(words):
    list1 = []
    for i in range(len(words)):
        #print(words[i])
        if len(words[i]) > 4:
            a = words[i]
            list1.append(a)

    return list1

print(select_long_words(["what", "are", "we", "eating", "for", "dinner"])) # => ["eating", "dinner"] 
print(select_long_words(["keep", "coding"]))  # => ["coding"]
