import sys
from collections import deque

base = deque(sys.stdin.readline().strip())
min_length = sys.maxsize

for _ in range(len(base)):
    encode = ''
    target = base[0]
    count = 1
    for i in range(1,len(base)):
        if base[i] == target:
            count += 1
        else:
            encode += target + str(count)
            target = base[i]
            count = 1
    
    encode += target + str(count)
    min_length = min(min_length,len(encode))
    base.appendleft(base.pop())

print(min_length)