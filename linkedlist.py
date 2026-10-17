class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(56)

# Link the nodes
first.next = second
second.next = third
third.next = fourth

# Traverse the linked list
current = first

while current is not None:
    print(current.data)
    current = current.next

    