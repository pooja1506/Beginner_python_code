""" Write a method abbreviate_sentence that takes in a sentence string and returns a new sentence where every word longer than 4 characters has all of it's vowels removed. """


def abbreviate_sentence(sent):
    words = sent.split(" ")
    new_words = []
    for each_word in words:
        if len(each_word) > 4:
            word_without_vowels = sentence(each_word)
            new_words.append(word_without_vowels)
        else:
            new_words.append(each_word)
        new_sentence = " ".join(new_words)
    return new_sentence


def sentence(each_word):
    vowels = 'aeiou'
    no_vowels = ''
    for each_char in each_word:
        if not (each_char in vowels):
            no_vowels += each_char
    return no_vowels


print(abbreviate_sentence("follow the yellow brick road")) # => "fllw the yllw brck road"
print(abbreviate_sentence("what a wonderful life"))  # => "what a wndrfl life"

