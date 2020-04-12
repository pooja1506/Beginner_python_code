""" Write a method to_initials that takes in a person's name string and returns a string representing their initials."""
def to_initials(name):
    value = ""
    for index,items in enumerate(name):
        for character in items:
            if character == character.upper():
        
                value = value + character

    return value



        

print(to_initials("Kelvin Bridges"))      # => "KB" 
print(to_initials("Michaela Yamamoto"))   # => "MY" 
print(to_initials("Mary La Grange"))      # => "MLG"
