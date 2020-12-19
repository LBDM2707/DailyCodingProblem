# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be 
# smaller than or equal to N.

# You should be as efficient with time and space as possible.

# Link list



class logger:
    class LogNode:
        order_id = 0
        next = None
        def __init__(self, order_id, next = None):
            self.order_id = order_id
            self.next = next

    last_log = 0
    size = 0
    def __init__(self, node = None):
        self.last_log = node
    
    def record(self, order_id):
        new_node = self.LogNode(order_id, self.last_log)
        self.last_log = new_node   
        self.size += 1     
        return self.size

    def get_last(self,i):
        if i >= self.size:
            return False        
        curr = self.last_log
        for j in range(1, i):
            curr = curr.next
        return curr.order_id


def main():
    print("hello")

if __name__=='__main__':
    main()
