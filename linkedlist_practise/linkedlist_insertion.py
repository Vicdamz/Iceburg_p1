class Node:
 def __init__(self, value):
    self.value = value
    self.next = None


# Create original nodes
a = Node(10)
b = Node(20)
c = Node(30)


# Connect original list
a.next = b
b.next = c

# 10 -> 20 -> 30 -> None


# Create new node
new_node = Node(25)


# Insert 25 after 20
new_node.next = b.next
b.next = new_node


# Traverse to check
current = a

while current != None:
 print(current.value)
 current = current.next