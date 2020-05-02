""" Write a method hand_score that takes in a string representing a hand of cards and returns it's total score. You can assume the letters in the string are only A, K, Q, J. A is worth 4 points, K is 3 points, Q is 2 points, and J is 1 point. The letters of the input string are not necessarily uppercase. """
def hand_score(hand):
    sum = 0
    dict1 = {"A":4 , "a":4 , "K": 3 , "k":3 , "Q":2 , "q":2 , "J":1 , "j":1}
    for i in range(len(hand)):
        
        sum = sum + dict1[hand[i]]
    return sum


print(hand_score("AQAJ"))  # => 11 
print(hand_score("jJka"))  # => 9
