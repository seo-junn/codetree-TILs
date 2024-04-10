import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

N = int(sys.stdin.readline())
nodes = [Node(i) for i in range(N+1)]

for _ in range(int(sys.stdin.readline())):
    line = list(map(int,sys.stdin.readline().split()))
    
    if line[0] == 1:
        cur = nodes[line[1]]
        if cur.prev: cur.prev.next = cur.next
        if cur.next: cur.next.prev = cur.prev
        cur.prev = None
        cur.next = None
    
    elif line[0] == 2:
        cur, node = nodes[line[1]],nodes[line[2]]
        if cur.prev:
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node
        else:
            cur.prev = node
            node.next = cur
    
    elif line[0] == 3:
        cur, node = nodes[line[1]],nodes[line[2]]
        if cur.next:
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node
        else:
            cur.next = node
            node.prev = cur
    
    else:
        cur = nodes[line[1]]
        print(cur.prev.data if cur.prev else 0, cur.next.data if cur.next else 0)

ans = []
for i in range(1,N+1):
    ans.append(nodes[i].next.data if nodes[i].next else 0)

print(*ans)