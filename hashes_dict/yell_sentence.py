""" Write a method yell_sentence that takes in a sentence string and returns a new sentence where every word is yelled. See the examples. Use map to solve this. """
def yell_sentence(sent):
    final_string = " "
    word = sent.split(" ")
    for i in range(len(word)):
        a = word[i].upper() + "! " 
        final_string = final_string +  a

    return final_string


# => "I! HAVE! A! BAD! FEELING! ABOUT! THIS!" 
print(yell_sentence("I have a bad feeling about this"))
