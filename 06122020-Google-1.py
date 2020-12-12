# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes
# the tree into a string, and deserialize(s), which deserializes the string 
# back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    result = [root]        
    i = 0
    while i< len(result):
        if result[i] != None:
            result.append(result[i].left)
            result.append(result[i].right)
            result[i] = result[i].val
        else:
            result[i] = None
        i += 1
    return result

def deserialize(s):
    # temp = [Node(x) for x in s]    
    # for i in range(len(temp)):
    #     temp[i].left = temp[2*i+1] if (2*i +1 < len(temp)) and temp[2*i+1] != None else None
    #     temp[i].right = temp[2*i+2] if (2*i +2 < len(temp)) and temp[2*i+2] != None else None
    # return temp[0]
    s[0] = Node(s[0])
    for i in range(len(s)):
        if 2*i+1<len(s) and s[2*i + 1] != None:
            s[2*i+1] = Node(s[2*i+1])
        s[i].left=s[2*i+1]
        if 2*i+2<len(s) and s[2*i + 2] != None:
            s[2*i+2] = Node(s[2*i+2])
        s[i].right=s[2*i+2]
    return s[0]

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    print(deserialize(serialize(node)).left.left.val == 'left.left')
    assert deserialize(serialize(node)).left.left.val == 'left.left'

if __name__ == '__main__':
    main()