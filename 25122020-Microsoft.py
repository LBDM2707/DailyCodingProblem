# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces), 
# return the original sentence in a list. If there is more than one possible 
# reconstruction, return any of them. If there is no possible reconstruction, 
# then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
# string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond'] 
# or ['bedbath', 'and', 'beyond'].

from unittest import TestCase

def break_sentence(sentence, words_dict):
    return []

#Test 1
print("Case 1======================")
words_dict = ['bed', 'bath', 'bedbath', 'and', 'beyond']
sentence = "bedbathandbeyond"
result = ['the', 'quick', 'brown', 'fox']
print("Expected = {}".format(result))
print("Actual   = {}".format(break_sentence(sentence,words_dict)))

#Test 2
print("\nCase 2======================")
words_dict = ['quick', 'brown', 'the', 'fox']
sentence = "thequickbrownfox"
result = ['bed', 'bath', 'and', 'beyond']
print("Expected = {}".format(result))
print("Actual   = {}".format(break_sentence(sentence,words_dict)))
