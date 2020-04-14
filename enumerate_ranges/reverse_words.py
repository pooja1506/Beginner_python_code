'''Write a method reverse_words that takes in a sentence string and returns the sentence with the order of the characters in each word reversed. Note that we need to reverse the order of characters in the words, do not reverse the order of words in the sentence.'''


def reverse_words(sent):
    split_sent = sent.split(" ")
    list1 = []
    new_string = " "
    i = 0
    while i < len(split_sent):
        new = split_sent[i]
        new2 = to_reverse(new)
        list1.append(new2)
        i += 1
    new_string = " ".join(list1)
    return new_string


def to_reverse(new):
    value = " "
    value_out = ""
    for word in range(len(new)):
        value = new[word]
        value_out = value + value_out
    return value_out


print(reverse_words('keep coding'))  # => 'peek gnidoc'
# => 'yticilpmis si etisiuqererp rof ytilibailer'
print(reverse_words('simplicity is prerequisite for reliability'))