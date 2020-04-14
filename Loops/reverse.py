# Write a method reverse(word) that takes in a string word and returns the word with its letters in reverse order.
def reverse(word):
    value = ''
    for i in range(len(word)):
        value = word[i] + value
    return value


print(reverse("cat"))  # prints "tac" 
print(reverse("programming"))  # prints "gnimmargorp" 
print(reverse("bootcamp"))   # prints "pmactoob" 
print(reverse("noon"))  # print "noon"
