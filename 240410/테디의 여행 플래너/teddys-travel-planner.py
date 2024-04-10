import sys

class Node:
    def __init__(self,city):
        self.city = city
        self.left = None
        self.right = None

N,Q = map(int,sys.stdin.readline().split())
cities = sys.stdin.readline().strip().split()
pinned = Node(cities[0])
tail = pinned
for i in range(1,N):
    node = Node(cities[i])
    tail.right = node
    node.left = tail
    tail = node
tail.right = pinned
pinned.left = tail

for _ in range(Q):
    line = sys.stdin.readline().strip().split()
    if line[0] == '1':
        if pinned.right:
            pinned = pinned.right
    
    elif line[0] == '2':
        if pinned.left:
            pinned = pinned.left
    
    elif line[0] == '3':
        if pinned.right:
            if pinned.right.right == pinned:
                pinned.right = None
                pinned.left = None
            else:
                pinned.right.right.left = pinned
                pinned.right = pinned.right.right
    
    else:
        if pinned.right:
            node = Node(line[1])
            pinned.right.left = node
            node.right = pinned.right
            node.left = pinned
            pinned.right = node
        else:
            node = Node(line[1])
            pinned.right = node
            pinned.left = node
            node.right = pinned
            node.left = pinned
    
    if pinned.left == pinned.right: print(-1)
    else: print(pinned.left.city,pinned.right.city)