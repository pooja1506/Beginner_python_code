""" Write a method word_lengths that takes in a sentence string and returns a dictionary where every key is a word of the sentence, and its corresponding value is the length of that word. """


def word_lengths(sentence):
    new_sent = sentence.split(" ")
    final_dict = {}
    for word in new_sent:
        final_dict[word] = len(word)
    return final_dict


print(word_lengths("this is fun"))  # => {"this": 4, "is": 2, "fun": 3}

# => {"When": 4, "in": 2, "doubt,": 6, "leave": 5, "it": 2, "out": 3}
print(word_lengths("When in doubt, leave it out"))
