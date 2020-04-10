""" Write a method element_times_index(nums) that takes in an array of numbers and returns a new array containing every number of the original array multiplied with its index. """
def elements_times_index(numbers):
    list1 = []
    for i in range(0,len(numbers)):
        
        calc = numbers[i] * i 
        list1.append(calc)

    return list1


print(elements_times_index([4, 7, 6, 5]))      # => [0, 7, 12, 15] 
print(elements_times_index([1, 1, 1, 1, 1, 1]))  # => [0, 1, 2, 3, 4, 5]
