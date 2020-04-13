'''Write a method is_valid_email that takes in a string and returns a boolean indicating whether or not it is a valid email address.'''
# For simplicity, we'll consider an email valid when it satisfies all of the following:
# - contains exactly one @ symbol
# - contains only lowercase alphabetic letters before the @
# - contains exactly one . after the @
def is_valid_email(str):
    for i in range(len(str)):
        #print(i)
        if str[i] == str[i].lower():
            return True


print(is_valid_email("abc@xy.z"))         # => true
#print(is_valid_email("jdoe@gmail.com"))   # => true
#print(is_valid_email("jdoe@g@mail.com"))  # => false
#print(is_valid_email("jdoe42@gmail.com")) # => false
#print(is_valid_email("jdoegmail.com"))    # => false
#print(is_valid_email("az@email"))         # => false
