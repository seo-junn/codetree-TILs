import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    m = int(sys.stdin.readline())
    arr = []
    ans = []
    nums = list(map(int,sys.stdin.readline().split()))
    for i in range(m):
        heapq.heappush(arr,nums[i])
        if i%2 == 0:
            ans.append(heapq.nsmallest((i//2)+1,arr)[-1])
    print(*ans)