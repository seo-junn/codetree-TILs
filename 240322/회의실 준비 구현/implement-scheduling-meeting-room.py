import sys

n = int(sys.stdin.readline())
meetings = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
meetings.sort(key=lambda x:x[1])

count = 0
end_time = 0
for s,e in meetings:
    if s >= end_time:
        end_time = e
        count += 1

print(count)