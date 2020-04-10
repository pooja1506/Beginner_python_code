# Write a method yell(words) that takes in an array of words and returns a new array where every word from the original array has an exclamation point after it.
def yell(words):
    list1 = []
    for i in range(0,len(words)):
        print(i)
        print(words[i])

        new_array = words[i] + '!'
        print(new_array)
        list1.append(new_array)

    return list1


print(yell(["hello", "world"]))  # => ["hello!", "world!"] 
print(yell(["code", "is", "cool"]))  # => ["code!", "is!", "cool!"]
