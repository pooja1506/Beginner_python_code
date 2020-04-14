""" Write a method to_initials that takes in a person's name string and returns a string representing their initials."""


def to_initials(name):
    value = []
    new_name = ""
    split_name = name.split(" ")
    i = 0

    while i < len(split_name):
        x = (split_name[i])[0]
        value.append(x)
        i = i+1
    new_name = "".join(map(str, value))
    return new_name

print(to_initials("Kelvin Bridges"))      # => "KB"
print(to_initials("Michaela Yamamoto"))   # => "MY"
print(to_initials("Mary La Grange"))      # => "MLG"
print(to_initials("pooja mehta"))

