# Write a method is_palindrome(word) that takes in a string word and returns the true if the word is a palindrome, false otherwise. A palindrome is a word that is spelled the same forwards and backwards. '''
def is_palindrome(word):
    value = ''
    for i in range(len(word)):
        value = word[i] + value

    if word == value:
        return True

    else:
        return False

print(is_palindrome("racecar"))  # prints true 
print(is_palindrome("kayak"))  # prints true 
print(is_palindrome("bootcamp"))  # prints false
