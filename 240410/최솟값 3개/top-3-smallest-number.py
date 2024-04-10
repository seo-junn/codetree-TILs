import sys
import heapq

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
three = []
val = 1

for i in range(n):
    if i < 2:
        val *= numbers[i]
        heapq.heappush(three,-numbers[i])
        print(-1)
    elif i == 2:
        val *= numbers[i]
        heapq.heappush(three,-numbers[i])
        print(val)
    else:
        if numbers[i] < -three[0]:
            val //= -heapq.heappop(three)
            val *= numbers[i]
            heapq.heappush(three,-numbers[i])
        print(val)