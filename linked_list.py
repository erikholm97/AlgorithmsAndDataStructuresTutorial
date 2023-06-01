class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data
    

n1 = Node(10)

print(n1)

class LinkedList:
    """
    Singly linked list
    """
    head = None
    next_node = None

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes 0(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def is_empty(self):
        return self.head == None
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        

        
l = LinkedList()

N1 = Node(10)
l.head = N1
print(l.size())