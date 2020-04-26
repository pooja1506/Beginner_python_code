""" Write a method ae_count that takes in a string and returns a dictionary containing the number of a's and e's in the string. Assume the string contains only lowercase characters. """
def ae_count(string):
    count = 0
    count1 = 0
    final_dict = {}
    for character in string :
        
        if character == 'a':
            count = count + 1
            final_dict["a"] = count
        elif character == 'e':
            count1 = count1 + 1
            final_dict["e"] = count1


    return final_dict

print(ae_count("everyone can program"))  # => {"a": 2, "e": 3} 
print(ae_count("keyboard"))  # => {"a": 1, "e": 1}
