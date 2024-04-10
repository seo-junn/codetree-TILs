class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

S_init = input()
cur = Node(S_init)
N = int(input())

for _ in range(N):
    line = input().split()

    if line[0] == '1':
        node = Node(line[1])
        if cur.prev:
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node
        else:
            cur.prev = node
            node.next = cur
    
    elif line[0] == '2':
        node = Node(line[1])
        if cur.next:
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node
        else:
            cur.next = node
            node.prev = cur
    
    elif line[0] == '3':
        if cur.prev:
            cur = cur.prev
    
    else:
        if cur.next:
            cur = cur.next
    
    print(cur.prev.data if cur.prev else '(Null)',cur.data,cur.next.data if cur.next else '(Null)')