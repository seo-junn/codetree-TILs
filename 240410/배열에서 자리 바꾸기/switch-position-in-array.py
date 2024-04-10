import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

N = int(sys.stdin.readline())
nodes = [Node(i) for i in range(N+1)]

nodes[1].next = nodes[2]
nodes[N].prev = nodes[N-1]

for i in range(2,N):
    nodes[i].prev = nodes[i-1]
    nodes[i].next = nodes[i+1]

head = nodes[1]
tail = nodes[N]

for _ in range(int(sys.stdin.readline())):
    a,b,c,d = map(int,sys.stdin.readline().split())
    if nodes[a].prev: nodes[a].prev.next = nodes[c]
    else: head = nodes[c]
    if nodes[c].prev: nodes[c].prev.next = nodes[a]
    else: head = nodes[a]
    nodes[a].prev, nodes[c].prev = nodes[c].prev, nodes[a].prev
    
    if nodes[b].next: nodes[b].next.prev = nodes[d]
    else: tail = nodes[d]
    if nodes[d].next: nodes[d].next.prev = nodes[b]
    else: tail = nodes[b]
    nodes[b].next, nodes[d].next = nodes[d].next, nodes[b].next

ans = []
cur = head
while cur:
    ans.append(cur.data)
    cur = cur.next

print(*ans)