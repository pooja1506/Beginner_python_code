""" Write a method hash_to_pairs that takes in a dictionary and returns a 2D array representing each key-value pair of the dictionary. """
def hash_to_pairs(hash_in):
    list1 = []
    for keys,values in hash_in.items():
        list1.append([keys,values])

    return list1

# => [["name", "skateboard"], ["wheels", 4], ["weight", "7.5 lbs"]] 
print(hash_to_pairs({"name": "skateboard", "wheels": 4, "weight": "7.5 lbs"})) 

# => [["kingdom", "animalia"], ["genus", "canis"], ["breed", "German Shepherd"]] print(hash_to_pairs({"kingdom": "animalia", "genus": "canis", "breed": "German Shepherd"}))

