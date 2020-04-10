""" Write a method odd_range(min, max) that takes in two numbers min and max. The method should return an array containing all odd numbers from min to max (inclusive). """
def odd_range(minimum, maximum):
    list1 = []
    for i in range(minimum,maximum+1):
        if i % 2 != 0:
            num = i
            list1.append(num)

    return list1

print(odd_range(11, 18))  # => [11, 13, 15, 17] 
print(odd_range(3, 7))   # => [3, 5, 7]
