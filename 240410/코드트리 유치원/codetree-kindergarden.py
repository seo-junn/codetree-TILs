import sys

class Node:
    def __init__(self,id):
        self.id = id
        self.prev = None
        self.next = None

students = {}
node = Node(1)
students[1] = node

def print_line(cur):
    while cur.prev:
        cur = cur.prev
    res = []
    while cur:
        res.append(cur.id)
        cur = cur.next
    print(*res)

cur_student = 1
for _ in range(int(sys.stdin.readline())):
    line = list(map(int,sys.stdin.readline().split()))
    if line[0] < 3:
        # create new students
        cur_student += 1
        head = Node(cur_student)
        students[cur_student] = head
        tail = head
        for i in range(line[2]-1):
            cur_student += 1
            node = Node(cur_student)
            students[cur_student] = node
            tail.next = node
            node.prev = tail
            tail = node

        if line[0] == 1:
            target = students[line[1]]
            if target.next:
                target.next.prev = tail
                tail.next = target.next
                target.next = head
                head.prev = target
            else:
                target.next = head
                head.prev = target
        else:
            target = students[line[1]]
            if target.prev:
                head.prev = target.prev
                target.prev.next = head
                tail.next = target
                target.prev = tail
            else:
                tail.next = target
                target.prev = tail
    else:
        target = students[line[1]]
        if target.prev and target.next: print(target.prev.id,target.next.id)
        else: print(-1)