""" Write a method get_double_age that takes in a dictionary and returns twice the "age" value of the dictionary. """ 
def get_double_age(hash_in):
    a = hash_in["age"]
    age_double = a * 2
    return age_double

print(get_double_age({"name": "App Academy", "age": 5}))  # => 10 
print(get_double_age({"name": "Ruby", "age": 23}))       # => 46
