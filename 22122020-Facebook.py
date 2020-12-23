# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different 
# colors. He has a goal of minimizing cost while ensuring that no two neighboring
# houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to 
# build the nth house with kth color, return the minimum cost which achieves this
# goal.

min = None
# Back tracking + prunning
def min_cost(matrix, house=-1, color=0, sum=0):
    global min
    # stop condition house == len matrix
    if house == len(matrix)-1:
        if min == None:
            min = sum
        else:
            min = sum if sum <= min else min
    else:
        # prunning
        if (min != None and sum <= min) or (min == None):
            curr = 0
            if house >= 0:
                curr = matrix[house][color]
            for i in range(len(matrix[house])):
                if i != color:
                    min_cost(matrix, house + 1, i, sum + curr)
    

n = 5
k = 4
test = [
    [1,6,4,2],
    [5,3,4,15],
    [15,2,7,3],
    [4,8,5,12],
    [4,1,2,25],
]
min_cost(test)
print (min)
