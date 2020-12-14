# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes 
# under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
class Node:
    left = None
    right = None
    value = None
    def __init__(self, value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(node):
    print(node.value)
    if node.left != None:
        dfs(node.left)
    if node.right != None:
        dfs(node.right)



def main():
    print('This is the 11/12/2020 problem by Google:')
    # Construct tree
    root = Node(0, left=Node(1), right=Node(0,left=Node(1,left=Node(1),right=Node(1)),right=Node(0)))

    # dfs to test tree
    dfs(root)



if __name__=='__main__':
    main()