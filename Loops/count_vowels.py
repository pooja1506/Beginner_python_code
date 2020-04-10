# Write a program that counts the number of "vowels(a,e,i,o,u)" in a string. 
def count_vowels(word):
    count = 0
    for character in word:
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            count = count + 1
    return count
print(count_vowels("bootcamp"))  # => 3 
print(count_vowels("apple"))     # => 2 
print(count_vowels("pizza"))     # => 2
