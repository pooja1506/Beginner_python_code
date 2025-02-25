""" Write a method map_by_name that takes in an array of dictionary and returns a new array containing the names of each dictionary key. """
def map_by_name(arr):
    list1 = []
    for i in range(len(arr)):
        for key,values in arr[i].items():
            if key == "name":
                list1.append(values)
    return list1



pets = [ {"type": "dog", "name": "Rolo"}, 
{"type": "cat", "name": "Sunny"}, 
{"type": "rat", "name": "Saki"}, 
{"type": "dog", "name": "Finn"}, 
{"type": "cat", "name": "Buffy"} ] 
print(map_by_name(pets))  # => ["Rolo", "Sunny", "Saki", "Finn", "Buffy"]

countries = [ {"name": "Japan", "continent": "Asia"}, 
{"name": "Hungary", "continent": "Europe"}, 
{"name": "Kenya", "continent": "Africa"}, ] 
print(map_by_name(countries))  # => ["Japan", "Hungary", "Kenya"]
