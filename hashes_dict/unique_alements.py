""" Write a method unique_elements that takes in an array and returns a new array where all duplicate elements are removed. Solve this using a dictionary. """ 
# Hint: all keys of a dictionary are automatically unique
def unique_elements(arr):
    final_dict = {}
    list1 = []
    for elements in arr:
        final_dict[elements] = arr.count(elements)
    for keys , values in final_dict.items():
        list1.append(keys)

    return list1

print(unique_elements(['a', 'b', 'a', 'a', 'b', 'c']))  # => ["a", "b", "c"]
