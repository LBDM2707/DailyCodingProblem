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

<<<<<<< Updated upstream
def count_universal(node):
    if node.left == None and node.right == None:
        return 1
    else:
        count = 0
        if node.left != None and node.right != None and node.left.value == node.right.value:
            count =1
        
        return count + count_universal(node.left) + count_universal(node.right)

=======
def count_univ_value(node):
    if node.left == None and node.right == None:
        return 1
    else:
        tmp = 0
        if (node.left is not None) and (node.right is not None) and  node.left.value == node.right.value:
            tmp = 1
        return tmp + (count_univ_value(node.left) if node.left is not None else 0) +  (count_univ_value(node.right) if node.right is not None else 0)
>>>>>>> Stashed changes


def main():
    print('This is the 11/12/2020 problem by Google:')
    # Construct tree
    root = Node(0, left=Node(1), right=Node(0,left=Node(1,left=Node(1),right=Node(1)),right=Node(0)))

    # dfs to test tree
    # dfs(root)

    # test func:
    print(count_univ_value(root))

    # test run:
    print("Result = {}".format(count_universal(root)))



if __name__=='__main__':
    main()