import sys
import heapq

N = int(sys.stdin.readline())
waiting = []
people = []
wait_line = []

for i in range(1, N + 1):
    a, t = map(int, sys.stdin.readline().split())
    heapq.heappush(people, (a, i, t))

time = 0
while people or wait_line:
    if wait_line:
        while people and people[0][0] < time:
            a, i, t = heapq.heappop(people)
            heapq.heappush(wait_line, (i, a, t))
        num, arrive, delay = heapq.heappop(wait_line)
        wait = time - arrive
        heapq.heappush(waiting, -wait)
        time += delay
    else:
        if people[0][0] >= time:
            arrive, num, delay = heapq.heappop(people)
            time = arrive + delay
            heapq.heappush(waiting,0)
        else:
            while people and people[0][0] < time:
                a,i,t = heapq.heappop(people)
                heapq.heappush(wait_line,(i,a,t))

print(-waiting[0])