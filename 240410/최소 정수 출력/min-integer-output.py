import sys
import heapq

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        print(heapq.heappop(arr) if arr else 0)
    else:
        heapq.heappush(arr,num)