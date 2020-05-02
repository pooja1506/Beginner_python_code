""" Write a method element_count that takes in an array and returns a dictionary representing the count of each element in the array. """
def element_count(arr):
    count = 0
    final_dict = {}
    for element in arr:
        final_dict[element] = arr.count(element)

    return final_dict
        
print(element_count(["a", "b", "a", "a", "b"]))  # => {"a":3, "b":2} 

# => {"red": 2, "blue": 1, "green": 1} 
print(element_count(["red", "red", "blue", "green"]))
