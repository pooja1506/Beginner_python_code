""" Write a method pig_latin_word that takes in a word string and translates the word into pig latin. """ 
# Pig latin translation uses the following rules:
 # - for words that start with a vowel, add 'yay' to the end 
# - for words that start with a nonvowel, move all letters before the first vowel to the end of the word and add 'ay
def pig_latin_word(word):
    vowels = "aeiou"
    for character in word:
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            vowel1 = word + "yay"
            return vowel1

        else:
            for index,items in enumerate(word):
                if items in vowels:
                    val1 = word[0:index]
                    val2 = word[index: ]
                    total = val2 + val1 + "ay"
                    return total       




print(pig_latin_word("apple"))   # => "appleyay" 
print(pig_latin_word("eat"))     # => "eatyay" 
print(pig_latin_word("banana"))  # => "ananabay" 
print(pig_latin_word("trash"))   # => "ashtray"
