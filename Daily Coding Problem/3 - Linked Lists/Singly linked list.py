# Singly linked list only contain a pointer to the next node, tipically called next,
# and are implemented like follows:

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Linked lists are a recursive data structure: the type of next is another linked list node.
# They have no fixed size like arrays do: a new node can be initialized and appended to a
# linked list on the fly