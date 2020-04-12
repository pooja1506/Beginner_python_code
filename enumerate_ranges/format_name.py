""" Write a method format_name that takes in a name string and returns the name properly capitalized. """
def format_name(string):
    i = 0
    split_name = string.split(" ")
    new_string = ""
    value = []

    while i < len(split_name):
        capital = split_name[i].capitalize()
        value.append(capital)
        
        i=i+1

    new_string = " ".join(value)
    return(new_string)




print(format_name("chase WILSON"))  # => "Chase Wilson" 
print(format_name("brian CrAwFoRd scoTT"))  # => "Brian Crawford Scott"
