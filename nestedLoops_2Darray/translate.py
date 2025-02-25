"""Write a method two_d_translate that takes in a 2 dimensional array and translates it into a 1 dimensional array. You can assume that the inner arrays always have 2 elements. See the examples.
"""
def two_d_translate(arr):
    list1 = []
    for i in arr:
        for j in range(i[1]):
            list1.append(i[0])
    return list1

arr_1 = [['boot', 3],['camp', 2],['program', 0]]
print(two_d_translate(arr_1))  # => [ 'boot', 'boot', 'boot', 'camp', 'camp' ]
arr_2 = [['red', 1],['blue', 4]]
print(two_d_translate(arr_2))  # => [ 'red', 'blue', 'blue', 'blue', 'blue' ]
