import sys
from collections import deque

cur = sys.stdin.readline().strip()
lq,rq = deque(),deque()

for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().strip().split()
    if line[0] == '1': lq.append(line[1])
    elif line[0] == '2': rq.appendleft(line[1])
    elif line[0] == '3':
        if lq:
            rq.appendleft(cur)
            cur = lq.pop()
    else:
        if rq:
            lq.append(cur)
            cur = rq.popleft()
    print(lq[-1] if lq else "(Null)", cur, rq[0] if rq else "(Null)")

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

S_init = sys.stdin.readline().strip()
cur = Node(S_init)
N = int(sys.stdin.readline())

for _ in range(N):
    line = sys.stdin.readline().strip().split()

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
'''