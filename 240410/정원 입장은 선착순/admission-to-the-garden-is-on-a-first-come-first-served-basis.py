import sys
import heapq

N = int(sys.stdin.readline())
waiting = []
people = []

for i in range(1, N + 1):
    a, t = map(int, sys.stdin.readline().split())
    heapq.heappush(people, (a, i, t))

time = 0
while people:
    if people[0][0] >= time:
        arrive, num, delay = heapq.heappop(people)
        time = arrive + delay
        heapq.heappush(waiting, 0)
    else:
        candidate = []
        while people and people[0][0] < time:
            a, i, t = heapq.heappop(people)
            heapq.heappush(candidate, (i, a, t))
        num, arrive, delay = heapq.heappop(candidate)
        wait = time - arrive
        heapq.heappush(waiting, -wait)
        time += delay
        while candidate:
            i, a, t = heapq.heappop(candidate)
            heapq.heappush(people, (a, i, t))

print(-waiting[0])