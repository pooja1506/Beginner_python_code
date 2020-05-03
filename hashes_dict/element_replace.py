""" Write a method element_replace that takes in an array and a dictionary. The method should return a new array where elements of the original array are replaced with their corresponding values in the dictionary. """
def element_replace(arr, hash_in):
    list1 = []
    for i in range(len(arr)):
        if arr[i] in hash_in:
            list1.append(hash_in[arr[i]])

        elif arr[i] not in hash_in:
            list1.append(arr[i])

    return list1

arr1 = ["LeBron James", "Lionel Messi", "Serena Williams"] 
hash1 = {"Serena Williams": "tennis", "LeBron James": "basketball"} 
# => ["basketball", "Lionel Messi", "tennis"] .
print(element_replace(arr1, hash1)) 

arr2 = ["dog", "cat", "mouse"] 
hash2 = {"dog": "bork", "cat": "meow", "duck": "quack"} 
print(element_replace(arr2, hash2))  # => ["bork", "meow", "mouse"]
