# This problem was asked by Google.

# An XOR linked list is a more memory efficient doubly linked list. Instead of 
# each node holding next and prev fields, it holds a field named both, which is 
# an XOR of the next node and the previous node. Implement an XOR linked list; it
# has an add(element) which adds the element to the end, and a get(index) which 
# returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you 
# have access to get_pointer and dereference_pointer functions that converts 
# between nodes and memory addresses.

# [In-progress]

class node:
    address = None
    value = None
    both = None
    def __init__(self, address, node):
        self.address = address
        self.node = node

def xor(a,b):
    return a^b

class XorList:
    head = None
    tail = None
    size = 0

    def __init__(self, head=None):
        self.head = head
        self.size = 0 if head == None else 1

    def add(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        elif self.size == 1:
            
            
        pass




def main():
    print('hello')
    print(xor(6,3))

if __name__=='__main__':
    main()