'''Write a method is_valid_email that takes in a string and returns a boolean indicating whether or not it is a valid email address.'''
# For simplicity, we'll consider an email valid when it satisfies all of the following:
# - contains exactly one @ symbol
# - contains only lowercase alphabetic letters before the @
# - contains exactly one . after the @


def is_valid_email(str):
    split_at_rate = str.split("@")
    #print(split_at_rate)

    if len(split_at_rate)!=2:
        return False

    a = split_at_rate[0]
    b = split_at_rate[1]
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for character in a:
        if character not in alphabets:
            return False

    split_b = b.split(".")
    if len(split_b) !=2:
        return False

    else:
        return True

    
    
print(is_valid_email("abc@xy.z"))         # => true
print(is_valid_email("jdoe@gmail.com"))   # => true
print(is_valid_email("jdoe@g@mail.com"))  # => false
print(is_valid_email("jdoe42@gmail.com"))  # => false
print(is_valid_email("jdoegmail.com"))    # => false 
print(is_valid_email("az@email"))         # => false
