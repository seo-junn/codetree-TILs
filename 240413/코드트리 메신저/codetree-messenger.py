import sys

class Node:
    def __init__(self,id,parent=None):
        self.id = id
        self.parent = parent
        self.left = None
        self.right = None
        self.alarm_option = True
        self.power = 0

def alarm_count(node,depth):
    if depth and not node.alarm_option: return 0
    if depth == 0: ans = 0
    else: ans = 1 if depth <= node.power else 0
    if node.left:
        ans += alarm_count(node.left,depth+1)
    if node.right:
        ans += alarm_count(node.right,depth+1)
    return ans

# initialize
N, Q = map(int,sys.stdin.readline().split())
tree = {}

for i in range(N+1):
    tree[i] = Node(i)

command,*data = map(int,sys.stdin.readline().split())
for i in range(N):
    parent = tree[data[i]]
    child = tree[i+1]
    child.parent = parent
    child.power = data[N+i]

    if parent.left == None:
        parent.left = child
    else:
        parent.right = child

# simulate
for _ in range(Q-1):
    command = list(map(int,sys.stdin.readline().split()))

    # alarm on/off
    if command[0] == 200:
        tree[command[1]].alarm_option = False if tree[command[1]].alarm_option else True

    # change power
    elif command[0] == 300:
        tree[command[1]].power = command[2]

    # change parent
    elif command[0] == 400:
        node1,node2 = tree[command[1]],tree[command[2]]
        parent1 = node1.parent
        parent2 = node2.parent

        node1.parent = parent2
        node2.parent = parent1
        if parent1.left == node1: parent1.left = node2
        else: parent1.right = node2
        if parent2.left == node2: parent2.left = node1
        else: parent2.right = node1

    # count alarming chat room
    else:
        print(alarm_count(tree[command[1]],0))