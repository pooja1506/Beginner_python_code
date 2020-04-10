# Write a program that counts the number of "A/a" in a string. 
def count_a(word): 
    count = 0
    for character in word :
        #print(character)
        if character == 'A' or character == 'a':
            count = count + 1
    return count

print(count_a("application"))  # => 2 
print(count_a("bike"))         # => 0 
print(count_a("Arthur"))       # => 1 
print(count_a("Aardvark"))     # => 3
