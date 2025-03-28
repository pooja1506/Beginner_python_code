""" Write a method last_index that takes in a string and a character. The method should return the last index where the character can be found in the string. """
def last_index(string, character):
    for i in range(len(string)-1,0,-1):
        if character in (string[i]):
            return i

print(last_index("abca", "a"))  # => 3 
print(last_index("mississipi", "i"))  # => 9 
print(last_index("octagon", "o"))  # => 5 
print(last_index("programming", "m"))  # => 7
