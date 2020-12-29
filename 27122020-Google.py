# This problem was asked by Google.

# Implement locking in a binary tree. A binary tree node can be locked or 
# unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# + is_locked, which returns whether the node is locked

# + lock, which attempts to lock the node. If it cannot be locked, then it should 
# return false. Otherwise, it should lock it and return true.

# + unlock, which unlocks the node. If it cannot be unlocked, then it should 
# return false. Otherwise, it should unlock it and return true.

# You may augment the node to add parent pointers or any other property you would 
# like. You may assume the class is used in a single-threaded program, so there is 
# no need for actual locks or mutexes. Each method should run in O(h), where h is 
# the height of the tree.

class LockingBinaryTree:
    class Node:
        def __init__(self, value=None):
            self.parent = None
            self.value = value
            self.left = left
            self.right = right
            self.is_locked = False

        def is_locked(self):
            return self.is_locked

        def check_condition(self):
            condition = True
            # Check parrent
            temp = self.parent
            while temp != None:
                if temp.is_locked():
                    return False
                temp = temp.parent

            # Check child            
            queue = [self]
            while len(queue) > 0:
                temp = queue.pop(0)
                if temp.is_locked():
                    return False
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            return True

        def lock(self):
            if self.check_condition:
                self.is_locked = True
                return True
            return False

        def unlock(self):
            if self.check_condition:
                self.is_locked = False
                return True
            return False
    
    root = None
    def __init__(self, root=None):
        self.root = root

    