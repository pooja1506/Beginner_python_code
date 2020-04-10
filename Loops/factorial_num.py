# Write a method factorial(num) that takes in a number num and returns the product of all numbers from 1 up to and including num.
def factorial(num):
    factorial = 1
    for value in range(1,num+1):
        factorial = factorial * value
    return factorial

print(factorial(3))  # prints 6 
print(factorial(5))  # prints 120
