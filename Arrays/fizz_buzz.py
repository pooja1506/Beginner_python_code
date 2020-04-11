""" Write a method fizz_buzz(maximum) that takes in a number max and returns an array containing all numbers greater than 0 and less than max that are divisible by either 4 or 6, but not both. """
def fizz_buzz(maximum):
    list1 = []
    for i in range(1,maximum):
        if (i % 4 == 0 or i % 6 == 0) and i % 12 != 0 :
            a = i
            list1.append(a)

    return list1

print(fizz_buzz(20))  # => [4, 6, 8, 16, 18] 
print(fizz_buzz(15))  # => [4, 6, 8]
