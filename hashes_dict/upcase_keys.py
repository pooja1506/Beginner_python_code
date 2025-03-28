""" Write a method select_upcase_keys that takes in a dictionary and returns a new dictionary containing key-value pairs of the original dictionary that had uppercase keys. You can assume that the keys will always be strings. """
def select_upcase_keys(hash_in):
    final_dict = {}
    for a in hash_in.keys():
        if a == a.upper():
            final_dict[a] = hash_in[a]

    return final_dict


# => {"MODEL": "S", "SEATS": 4} 
print(select_upcase_keys( {"make": "Tesla", "MODEL": "S", "Year": 2018, "SEATS": 4}))

 # => {"DATE": "July 4th"} 
print(select_upcase_keys( {"DATE": "July 4th", "holiday": "Independence Day", "type": "Federal"}))
