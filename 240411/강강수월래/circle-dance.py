import sys

class Node:
    def __init__(self,id):
        self.id = id
        self.left = None
        self.right = None

N,M,Q = map(int,sys.stdin.readline().split())

# initialize
students = {}
for _ in range(M):
    length, *nums = map(int,sys.stdin.readline().split())
    head = Node(nums[0])
    students[nums[0]] = head
    tail = head
    for i in range(1,length):
        node = Node(nums[i])
        students[nums[i]] = node
        tail.left = node
        node.right = tail
        tail = node
    tail.left = head
    head.right = tail

# simulate
for _ in range(Q-1):
    command,num_A,num_B = map(int,sys.stdin.readline().split())
    A = students[num_A]
    B = students[num_B]
    if command == 1:
        A.left.right = B.right
        B.right.left = A.left
        A.left = B
        B.right = A
    else:
        A.right.left = B
        B.right.left = A
        A.right,B.right = B.right,A.right

command, num_A = map(int,sys.stdin.readline().split())
A = students[num_A]
target = A
target_id = A.id
cur = A.right

while cur != A:
    if cur.id < target_id:
        target_id = cur.id
        target = cur
    cur = cur.right

res = [target.id]
cur = target.right
while cur != target:
    res.append(cur.id)
    cur = cur.right

print(*res)