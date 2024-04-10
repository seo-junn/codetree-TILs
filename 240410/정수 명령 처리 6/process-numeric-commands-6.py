import sys
import heapq

arr = []
for _ in range(int(sys.stdin.readline())):
    lines = sys.stdin.readline().strip().split()
    if lines[0] == 'push':
        heapq.heappush(arr,-int(lines[1]))
    elif lines[0] == 'pop':
        print(-heapq.heappop(arr))
    elif lines[0] == 'size':
        print(len(arr))
    elif lines[0] == 'empty':
        print(1 if not arr else 0)
    else:
        print(-arr[0])