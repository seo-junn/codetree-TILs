import sys
import heapq

arr = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        print(-heapq.heappop(arr) if arr else 0)
    else:
        heapq.heappush(arr,-num)