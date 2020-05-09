""" Write a method o_words that takes in a sentence string and returns an array of the words that contain an "o". Use select in your solution! """
# select() not available in python. So using traditional method instead 
def o_words(sentence):
    letter = "o"
    list1 = []
    split_word = sentence.split(" ")
    for i in range(len(split_word)):
        if letter in split_word[i]:
            list1.append(split_word[i])

    return list1


print(o_words("How did you do that?"))  # => ["How", "you", "do"]
