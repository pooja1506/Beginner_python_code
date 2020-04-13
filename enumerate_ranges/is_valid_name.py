""" Write a method is_valid_name that takes in a string and returns a boolean indicating whether or not it is a valid name. """
# A name is valid is if satisfies all of the following:
# - contains at least a first name and last name, separated by spaces
# - first alphabet of the name should be capitalized

"""
Step 1: Check if the input has atleast 2 values separated by Space. If it does not, return False.(case 2- Daniel)
Step 2: If there are atleast 2 values separated by Space, send the individual names to helper function(is_capital_name).
is_capital_name will take in the "string value" and compare it with original string.capitalize(). If only the first letter is capitalized and rest are small, it'll return true, or else false.
Step 3: back to main function - is_valid_name(), take in the returned string and evaluate using "if not in (is_capital_name): return False"
Step 4: finally return true in line of Step 1's if.
"""


def is_valid_name(string):
    split_string = string.split(" ")
    if len(split_string) < 2:
        return False
    else:
        for word in split_string:
            #print("Passing Word: ", word)
            if not(is_capital_name(word)):
                return False
    return True


def is_capital_name(word):
    if word == word.capitalize():
        #print("word: ", word)
        #print("word.capitalize: ", word.capitalize())
        #print("---------------------True---------------------")
        return True
    else:
        #print("---------------------False--------------------")
        return False




print(is_valid_name("Kush Patel"))       # => true
print(is_valid_name("Daniel"))           # => false
print(is_valid_name("Robert Downey Jr"))  # => true
print(is_valid_name("ROBERT DOWNEY JR"))  # => false
print(is_valid_name("PooJa Mehta")) #=> False
print(is_valid_name("Pooja Mehta student")) #=> False