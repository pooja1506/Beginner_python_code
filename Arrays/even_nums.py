""" Write a method even_nums(max) that takes in a number max and returns an array containing all even numbers from 0 to max """
def even_nums(maximum):
    list1 = []
    for i in range(0,maximum+1,2):
        even = i
        list1.append(even)

    return list1

print(even_nums(10))  # => [0, 2, 4, 6, 8, 10] 
print(even_nums(5))  # => [0, 2, 4]
