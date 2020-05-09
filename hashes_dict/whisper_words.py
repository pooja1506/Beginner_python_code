""" Write a method whisper_words that takes in an array of words and returns a new array containing a whispered version of each word. See the examples. Solve this using map :-). """
def whisper_words(words):
    list1 = []
    for i in range(len(words)):
        final = words[i].lower() + "..."
        list1.append(final)

    return list1

# => ["keep...", "the...", "noise...", "down..."] 
print(whisper_words(["KEEP", "The", "NOISE", "down"]))
