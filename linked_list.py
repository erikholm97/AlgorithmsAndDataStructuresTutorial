class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    
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
        """
        Adds new node containing data at head of the list
        Takes 0(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found

        Takes 0(n) time.
        """    
        current = self.head

        while current:
            if current.data == key:
                return current
        else:
            current = current.next_node
        return None

    def __repr__(self):
        """
        Returns a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)
        

        
# l = LinkedList()

# N1 = Node(10)
# l.head = N1
# print(l.size())

# l = LinkedList()

# l.add(1)
# print(l.size())
# l.add(2)
# l.add(60)
# print(l.size())