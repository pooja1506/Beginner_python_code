""" Write a method opposite_count that takes in an array of unique numbers. The method should return the number of pairs of elements that sum to 0. """
from itertools import combinations
def opposite_count(nums):
    count = 0
    list2 = []
    x = list(combinations(nums,2))

    for i in range(len(x)):
        list2.append(list(x[i]))
    
    for j in range(len(list2)):
        a = list2[j][0]
        b = list2[j][1]
        sum = a + b
        
        if sum == 0:
            count = count + 1

    return count



print(opposite_count([2, 5, 11, -5, -2, 7]))  # => 2 
print(opposite_count([21, -23, 24 - 12, 23]))  # => 1
