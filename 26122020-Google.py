# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. 
# Each True boolean represents a wall. Each False boolean represents a tile you 
# can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the 
# minimum number of steps required to reach the end coordinate from the start. 
# If there is no possible path, then return null. You can move up, left, down, 
# and right. You cannot move through walls. You cannot wrap around the edges of 
# the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum 
# number of steps required to reach the end is 7, since we would need to go 
# through (1, 2) because there is a wall everywhere else on the second row.
maze = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]
min = None

def valid_move(maze, point):
    x = point[0]
    y = point[1]
    m = len(maze)
    n = len(maze[0])
    return 0<= x and x<m and 0<=y and y<n and maze[x][y] == 0

def finding_path(maze, step, current, stop):   
    global min
    maze[current[0]][current[1]] = 1
    if current == stop:
        if min == None:
            min = step
        else:
            min = step if min > step else min
    else:
        if (min is None) or (min is not None and step < min):
            x = current[0]
            y = current[1]
            if valid_move(maze, (x+1, y)):
                finding_path(maze, step+1, (x+1, y),stop)
            if valid_move(maze, (x-1, y)):
                finding_path(maze, step+1, (x-1, y),stop)
            if valid_move(maze, (x, y+1)):
                finding_path(maze, step+1, (x, y+1),stop)
            if valid_move(maze, (x, y-1)):
                finding_path(maze, step+1, (x, y-1),stop)

start = (3,0)
stop = (0,0)

finding_path(maze, 0, start,stop)

print(min)


