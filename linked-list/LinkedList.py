from Node import Node

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.counter = 0

    # O(n)
    def traverseList():
        actualNode = self.head
        
        while is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode

    # start O(1)
    def insertStart(self, data):
        self.counter += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    # O(1) insted of O(n)
    def size(self):
        return self.counter
    
    # end O(n)
    def insertEnd(self, data):
        self.counter += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        
        actualNode.nextNode = newNode
    
    # O(n)
    def remove(self, data):
        if self.head:
            if data == self.head.data
                self.head = self.head.newNode
            else: 
                self.head.remove(data, self.head)
