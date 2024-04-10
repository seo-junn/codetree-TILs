import sys

class Knight:
    def __init__(self,id):
        self.id = id
        self.left = None
        self.right = None

N, M = map(int,sys.stdin.readline().split())

knights = {}
nums = list(map(int,sys.stdin.readline().split()))
head = Knight(nums[0])
knights[nums[0]] = head
tail = head

for i in range(1,N):
    node = Knight(nums[i])
    knights[nums[i]] = node
    tail.left = node
    node.right = tail
    tail = node

tail.left = head
head.right = tail

for _ in range(M):
    num = int(sys.stdin.readline())
    cur = knights[num]
    print(cur.left.id,cur.right.id)
    cur.left.right = cur.right
    cur.right.left = cur.left
    knights.pop(num)