class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Initialize nodes
a = Node(10)
b = Node(20)
c = Node(30)
d = Node(31)
e = Node(10)
f = Node(20)
g = Node(30)
h = Node(20)

# Link nodes
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

target = 20
counter = 0
current = a

# Traverse the linked list
while current is not None:
    if current.value == target:
        counter += 1
    current = current.next

# Output result
if counter > 0:
    print(f"The value is in the list")
    print(f"Occurrences: {counter}")
else:
    print(f"The value is not in the list")