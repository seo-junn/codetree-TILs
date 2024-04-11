import sys

class Node:
    def __init__(self,name,line_num):
        self.name = name
        self.line_num = line_num
        self.prev = None
        self.next = None

# initialize
N,M,Q = map(int,sys.stdin.readline().split())
X = N//M
people = {}
Lines = [[None,None] for _ in range(M)]
names = sys.stdin.readline().strip().split()

for line_offset in range(M):
    head = Node(names[line_offset*X],line_offset)
    people[names[line_offset*X]] = head
    tail = head
    for i in range(1,X):
        node = Node(names[line_offset*X+i],line_offset)
        people[names[line_offset*X+i]] = node
        tail.next = node
        node.prev = tail
        tail = node
    Lines[line_offset][0] = head
    Lines[line_offset][1] = tail

# simulate
for _ in range(Q):
    command, *in_names = sys.stdin.readline().strip().split()
    if command == '1':
        A = people[in_names[0]]
        B = people[in_names[1]]

        # pick up A
        line_of_A = A.line_num
        if A.prev: A.prev.next = A.next
        else: Lines[line_of_A][0] = A.next
        if A.next: A.next.prev = A.prev
        else: Lines[line_of_A][1] = A.prev
        A.next, A.prev = None, None

        # put A
        line_of_B = B.line_num
        if B.prev: B.prev.next = A
        else: Lines[line_of_B][0] = A
        A.prev, A.next, B.prev = B.prev, B, A

    elif command == '2':
        A = people[in_names[0]]

        line_of_A = A.line_num
        if A.prev: A.prev.next = A.next
        else: Lines[line_of_A][0] = A.next
        if A.next: A.next.prev = A.prev
        else: Lines[line_of_A][1] = A.prev
        people.pop(in_names[0])

    else:
        A = people[in_names[0]]
        B = people[in_names[1]]
        C = people[in_names[2]]

        # pick line A~B
        prev_line = A.line_num
        if A.prev: A.prev.next = B.next
        else: Lines[prev_line][0] = B.next
        if B.next: B.next.prev = A.prev
        else: Lines[prev_line][1] = A.prev
        A.prev, B.next = None, None

        # put line
        next_line = C.line_num
        if C.prev: C.prev.next = A
        else: Lines[next_line][0] = A
        A.prev, B.next, C.prev = C.prev, C, B

# print result
for i in range(M):
    head, tail = Lines[i]
    if head == None: print(-1)
    else:
        cur = head
        res = []
        while cur:
            res.append(cur.name)
            cur = cur.next
        print(*res)