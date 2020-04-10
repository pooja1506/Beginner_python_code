# Write a program that counts the number of "E/e" in a string. 

def count_e(word):
    count = 0
    for character in word:
        if character == 'e' or character=='E':
            count = count + 1
    return count


print("Count for 'Excellent': ", count_e("excellent")) # => 3
print("Count for 'Entrepreneurialism': ", count_e("Entrepreneurialism")) # => 4