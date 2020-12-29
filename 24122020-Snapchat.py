# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly 
# overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def min_room(slots):
    # result = 0
    temp = {}
    max = 0
    for s in slots:
        for i in range(s[0],s[1]):
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
            max = temp[i] if temp[i] > max else max
    return max


test = [(30, 75), (0, 50), (60, 150)]
print(min_room(test))