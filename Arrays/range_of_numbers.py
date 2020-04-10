""" Write a method range(min, max) that takes in two numbers min and max. The method should return an array containing all numbers from min to max inclusive. """
def range_of_num(minimum, maximum):
    list1 = []
    for i in range(minimum, maximum+1):
        num = i
        list1.append(num)

    return list1

print(range_of_num(2, 7))   # => [2, 3, 4, 5, 6, 7] 
print(range_of_num(13, 20))  # => [13, 14, 15, 16, 17, 18, 19, 20]
