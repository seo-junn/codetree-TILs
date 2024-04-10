import sys

class Node:
    def __init__(self,id,line):
        self.id = id
        self.line = line
        self.prev = None
        self.next = None

N, M, Q = map(int,sys.stdin.readline().split())

# initialize
people = {}
lines = [[None,None] for _ in range(M)]

for line_num in range(M):
    line = list(map(int,sys.stdin.readline().split()))
    if line[0] == -1: continue

    length = line[0]
    head = Node(line[1],line_num)
    people[line[1]] = head
    tail = head

    for i in range(2,length+1):
        node = Node(line[i],line_num)
        people[line[i]] = node
        tail.next = node
        node.prev = tail
        tail = node

    lines[line_num][0] = head
    lines[line_num][1] = tail

# simulate
for _ in range(Q):
    command, *nums = map(int,sys.stdin.readline().split())
    if command == 1:
        # pick up a
        a = people[nums[0]]
        line_num_a = a.line
        if a.prev: a.prev.next = a.next
        else: lines[line_num_a][0] = a.next
        if a.next: a.next.prev = a.prev
        else: lines[line_num_a][1] = a.prev
        a.prev,a.next = None, None

        # put a
        b = people[nums[1]]
        line_num_b = b.line
        if b.prev: b.prev.next = a
        else: lines[line_num_b][0] = a
        a.prev, a.next, b.prev = b.prev, b, a
        a.line = line_num_b

    elif command == 2:
        # pick up a
        a = people[nums[0]]
        line_num_a = a.line
        if a.prev: a.prev.next = a.next
        else: lines[line_num_a][0] = a.next
        if a.next: a.next.prev = a.prev
        else: lines[line_num_a][1] = a.prev
        people.pop(nums[0])

    else:
        # pick up people between a and b
        a = people[nums[0]]
        b = people[nums[1]]
        prev_line_num = a.line

        if a.prev: a.prev.next = b.next
        else: lines[prev_line_num][0] = b.next
        if b.next: b.next.prev = a.prev
        else: lines[prev_line_num][0] = a.prev
        a.prev, b.next = None, None

        # put people
        c = people[nums[2]]
        next_line_num = c.line
        if c.prev: c.prev.next = a
        else: lines[next_line_num][0] = a
        a.prev, b.next, c.prev = c.prev, c, b
        cur = c
        while cur:
            cur.line = next_line_num
            cur = cur.prev

# print result
for i in range(M):
    head,tail = lines[i]
    if head == None: print(-1)
    else:
        res = []
        cur = head
        while cur:
            res.append(cur.id)
            cur = cur.next
        print(*res)