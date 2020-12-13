# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of 
# non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

# Version 1, O(N), linear space with dynamic programing
def max_na_sum(s):
    if len(s) <= 2:
        return max(s)
    result = [0] * len(s)
    result[0] = s[0]
    if s[1] > s[0]:
        result[1] = s[1]
        last = True
    else:
        result[1] = s[0]
        last = False # check to see the last 
    for i in range(2, len(s)):
        temp = 0
        if last:
            temp = result[i-1] 
            last = False
        else:
            temp = result[i-1] + s[i]
            last = True
        if (result[i-2] + s[i]) > temp:
            temp = result[i -2] + s[i]
            last = True        
        result[i] = temp
    return result[i]


def main():
    print('This is a problem form Airbnb on 12/12/2020')
    print("f([2, 4, 6, 2, 5]) = {}".format(max_na_sum([2, 4, 6, 2, 5])))
    print("f([5, 1, 1, 5]) = {}".format(max_na_sum([5, 1, 1, 5])))


if __name__ == "__main__":
    main()