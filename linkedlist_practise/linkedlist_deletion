class Node:
 def __init__(self, value):
    self.value = value
    self.next = None


a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

# Before:
# 10 -> 20 -> 30 -> None


# Delete first node
a = a.next


# Check
current = a

while current != None:
 print(current.value)
 current = current.next