import sys

n = int(sys.stdin.readline())
meetings = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
meetings.sort(key=lambda x:(x[1],x[0]))

end = 0
count = 0
for s,e in meetings:
    if s >= end:
        end = e
    else:
        count += 1

print(count)