# Write a method doubler(numbers) that takes an array of numbers and returns a new array where every element of the original array is multiplied by 2.
def doubler(numbers):
    list1 = []
    for i in range(0,len(numbers)):
        #print(numbers[i])
        double = 2 * numbers[i]
        #print(double)
        list1.append(double)

    return list1

print(doubler([1, 2, 3, 4]))  # prints [2,4,6,8] 
print(doubler([2, 4, 6]))  # prints [4, 8, 12]


