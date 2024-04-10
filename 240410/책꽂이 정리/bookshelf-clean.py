import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

N, K = map(int,sys.stdin.readline().split())

# initialize
bookshelves = [[None,None] for _ in range(K+1)]
node = Node(1)
bookshelves[1][0] = node
tail = node
for i in range(2,N+1):
    node = Node(i)
    tail.next = node
    node.prev = tail
    tail = node
bookshelves[1][1] = tail

# simulate
for _ in range(int(sys.stdin.readline())):
    c,i,j = map(int,sys.stdin.readline().split())
    
    if c == 1:
        taken_head = bookshelves[i][0]
        if taken_head == None: continue

        node = taken_head
        
        if taken_head.next:
            taken_head = taken_head.next
            taken_head.prev = None
            bookshelves[i][0] = taken_head
        else:
            bookshelves[i][0] = None
            bookshelves[i][1] = None

        put_tail = bookshelves[j][1]        
        node.next = None
        if put_tail:
            put_tail.next = node
            node.prev = put_tail
            bookshelves[j][1] = node
        else:
            bookshelves[j][0] = node
            bookshelves[j][1] = node
    
    if c == 2:
        taken_tail = bookshelves[i][1]
        if taken_tail == None: continue

        node = taken_tail

        if taken_tail.prev:
            taken_tail = taken_tail.prev
            taken_tail.next = None
            bookshelves[i][1] = taken_tail
        else:
            bookshelves[i][0] = None
            bookshelves[i][1] = None

        put_head = bookshelves[j][0]        
        node.prev = None
        if put_head:
            put_head.prev = node
            node.next = put_head
            bookshelves[j][0] = node
        else:
            bookshelves[j][0] = node
            bookshelves[j][1] = node
    
    if c == 3:
        taken_head, taken_tail = bookshelves[i]
        if taken_head == None: continue
        bookshelves[i][0] = None
        bookshelves[i][1] = None

        put_head = bookshelves[j][0]
        if put_head:
            put_head.prev = taken_tail
            taken_tail.next = put_head
            bookshelves[j][0] = taken_head
        else:
            bookshelves[j][0] = taken_head
            bookshelves[j][1] = taken_tail
    
    if c == 4:
        taken_head, taken_tail = bookshelves[i]
        if taken_head == None: continue
        bookshelves[i][0] = None
        bookshelves[i][1] = None

        put_tail = bookshelves[j][1]
        if put_tail:
            put_tail.next = taken_head
            taken_head.prev = put_tail
            bookshelves[j][1] = taken_tail
        else:
            bookshelves[j][0] = taken_head
            bookshelves[j][1] = taken_tail

for i in range(1,K+1):
    head,tail = bookshelves[i]
    if head == None: print(0)
    else:
        books = []
        count = 0
        cur = head
        while cur:
            books.append(cur.data)
            count += 1
            cur = cur.next
        print(count,*books)