import sys
import heapq

N = int(sys.stdin.readline())
waiting = 0
people = []
wait_line = []

for i in range(1, N + 1):
    a, t = map(int, sys.stdin.readline().split())
    people.append((a,i,t))

people.sort(key=lambda x:x[0])

time = 0
for arrive, num, delay in people:

    while arrive > time and wait_line:
        n_num,n_arrive,n_delay = heapq.heappop(wait_line)
        waiting = max(waiting,time-n_arrive)
        time += n_delay

    if arrive > time:
        time = arrive + delay
    else:
        heapq.heappush(wait_line,(num,arrive,delay))

print(waiting)