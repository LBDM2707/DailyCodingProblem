# This problem was asked by Palantir.

# Write an algorithm to justify text. Given a sequence of words and an integer 
# line length k, return a list of strings which represents each line, fully 
# justified.

# More specifically, you should have as many words as possible in each line. 
# There should be at least one space between each word. Pad extra spaces when 
# necessary so that each line has exactly length k. Spaces should be distributed 
# as equally as possible, with the extra spaces, if any, distributed starting 
# from the left.

# If you can only fit one word on a line, then you should pad the right-hand side 
# with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words 
# ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
# and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

def create_line(temp,count, k):
    
    return temp


def justify_texts(s, k):
    temp_line = []
    temp_sum = 0
    result = []
    for word in s:
        if temp_sum + len(word) + 1 <= k:
            temp_line.append(word)
            temp_sum += 1 + len(word)
        else:
            # Created new line from temp
            result.append(create_line(temp_line, temp_sum, k))
            # Append word to new temp
            temp_line = []
            temp_sum = 0
            temp_line.append(word)
            temp_sum += len(word)
    if temp_sum > 0:
        result.append(create_line(temp_line, temp_sum, k))
    return result

test = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
print(justify_texts(test,k))