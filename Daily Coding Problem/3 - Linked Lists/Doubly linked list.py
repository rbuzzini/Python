# Doubly linked lists have pointers to the previous and next nodes. They take up
# more space, but allow you to traverse backwards. Their implementations looks lie this:

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

