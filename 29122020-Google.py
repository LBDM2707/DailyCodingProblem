# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from 
# the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

class LinkedList:
    class Node:
        def __init__(self, value = None):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.size = 0
        self.head = None

    def append(self, value):
        node = self.Node(value)
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = node
        self.size += 1
        
    def print_list(self):
        result = []
        tmp = self.head
        while tmp != None:
            result.append(tmp.value)
            tmp = tmp.next
        print(result)

    def delete(self, k):
        if k == 0:
            self.head = self.head.next
        else:
            i = 1
            tmp1 = self.head
            tmp2 = self.head.next
            while i < k:
                i += 1
                tmp1 = tmp1.next
                tmp2 = tmp2.next
            tmp1.next = tmp2.next
        self.print_list()


l = [1,2,3,4,5,6,7]
llist = LinkedList()
for i in l:
    llist.append(i)

llist.print_list()
llist.delete(2)
llist.delete(4)