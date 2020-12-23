# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the 
# intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the
# node with value 8.

# In this example, assume nodes with the same value are the exact same node 
# objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and 
# constant space.

class LinkedList:
    class Node:
        value = None
        next_node = None
        def __init__(self, value=None, next=None):
            self.value = value
            self.next_node = next

    head = None
    size = None
    def __init__(self, head=None):
        self.head = head
        self.size = 1 if head != None else 0

    def append(self, value):
        self.size += 1
        if self.head == None:
            self.head = self.Node(value=value) 
        else:
            temp = self.head
            while temp.next_node != None:
                temp = temp.next_node
            temp.next_node = self.Node(value=value) 
    def __str__(self):
        if self.head == None:
            return "[ ]"
        result = "["
        temp = self.head
        while temp != None:
            if temp == self.head:
                result += temp.value.__str__()
            else:
                result += ", " + temp.value.__str__()
            temp= temp.next_node
        return result + "]"

def find_intersect(linklist1, linklist2):
    temp1 = linklist1.head
    temp2 = linklist2.head
    terminal = linklist1.size * linklist2.size
    count = 0
    while temp1.value != temp2.value and count <= terminal:
        temp1 = temp1.next_node if temp1.next_node != None else linklist1.head    
        temp2 = temp2.next_node if temp2.next_node != None else linklist2.head
        count += 1
    return temp1.value if temp1 == temp2 else None


# init problem
list1 = [3,7,8,10]
list2 = [99,1,8,10]
linklist1 = LinkedList()
linklist2 = LinkedList()
for item in list1:
    linklist1.append(item)

for item in list2:
    linklist2.append(item)

print("link list 1 = {}".format(linklist1))
print("link list 2 = {}".format(linklist2))

print(find_intersect(linklist1,linklist2))

    