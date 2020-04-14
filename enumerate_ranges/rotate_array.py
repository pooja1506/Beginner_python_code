'''Write a method rotate_array that takes in an array and a number. The method should return the array after rotating the elements the specified number of times. A single rotation takes the last element of the array and moves it to the front.'''
def rotate_array(arr, num):
    for i in range(len(arr)):
        new = arr[i]
        

print(rotate_array([ "Matt", "Danny", "Mashu", "Matthias" ], 1)) # => [ "Matthias", "Matt", "Danny", "Mashu" ]
#print(rotate_array([ "a", "b", "c", "d" ], 2)) # => [ "c", "d", "a", "b" ]
