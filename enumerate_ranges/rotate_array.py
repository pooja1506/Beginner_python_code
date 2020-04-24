'''Write a method rotate_array that takes in an array and a number. The method should return the array after rotating the elements the specified number of times. A single rotation takes the last element of the array and moves it to the front.'''
from collections import deque


def rotate_array(arr, num):
    i = 0
    while i < num:
        ele = arr.pop()
        print("pop: ", ele)
        arr = deque(arr)
        print("arr_deque: ", arr)
        arr.appendleft(ele)
        print("arr_append_left: ", arr)
        arr = list(arr)
        print("arr_list: ", arr)
        print("-------------------**************---------------------")
        i += 1
    return arr

# => [ "Matthias", "Matt", "Danny", "Mashu" ]
print(rotate_array(["Matt", "Danny", "Mashu", "Matthias"], 1))

print(rotate_array(["a", "b", "c", "d"], 2))  # => [ "c", "d", "a", "b" ]

print(rotate_array(["10", "20", "30", "40", "50", "60"], 4))
