""" Write a method first_half(array) that takes in an array and returns a new array containing the first half of the elements in the array. If there is an odd number of elements, return the first half including the middle element. """
def first_half(an_array):
    list1 = []
    a = int(len(an_array))
    #print(a)
    
    for i in range(0,a):
        b=a/2
        #print(b)
        c = b+1
        #print(c)
        if i % 2 == 0:
            ans = an_array[ 0: int(c)]
            list1.append(ans)
        elif i%2 != 0:
            ans = an_array[0:int(b)]
            list1.append(ans)
    return ans

print(first_half(["Brian", "Abby", "David", "Ommi"]))  # => ["Brian", "Abby"] 
print(first_half(["a", "b", "c", "d", "e"]))          # => ["a", "b", "c"]
print(first_half(["P", "M", "15", "0", "6", "9", "7", "y"]))  # => ["P", "M", "15", "0"] 
print(first_half(["P", "M", "15", "0", "6", "9", "7"]))  # => ["P", "M", "15", "0"]

