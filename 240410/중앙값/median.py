import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    left_pq = []
    right_pq = []
    m = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    mid = nums[0]
    ans = [mid]
    for i in range(1,m):
        if nums[i] < mid:
            heapq.heappush(left_pq,-nums[i])
        else:
            heapq.heappush(right_pq,nums[i])
        if i%2:
            if len(left_pq) > len(right_pq):
                heapq.heappush(right_pq,mid)
                mid = -heapq.heappop(left_pq)
            elif len(left_pq) < len(right_pq):
                heapq.heappush(left_pq,-mid)
                mid = heapq.heappop(right_pq)
            ans.append(mid)
    print(*ans)