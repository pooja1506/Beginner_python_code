# Write a method sum_nums(max) that takes in a number max and returns the sum of all numbers from 1 up to and including max.
def sum_nums(max_val):
    sum = 0
    for i in range(1,max_val+1):
        sum = sum + i
    return sum


print(sum_nums(4))  # prints 10 
print(sum_nums(5))  # prints 15 
print(sum_nums(100))  # prints 5050
