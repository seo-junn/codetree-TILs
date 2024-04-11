import sys

N = int(sys.stdin.readline())
dots = []

for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    dots.append((x,y))

dots.sort()

ans = sys.maxsize
for y_line in range(0,1001,2):
    count = [0]*4

    for x,y in dots:
        if y > y_line : count[0] += 1
        else: count[3] += 1

    for i in range(N):
        if i == 0 or dots[i][0] != dots[i-1][0]:
            ans = min(ans,max(count))

        x,y = dots[i]
        if y > y_line:
            count[0] -= 1
            count[1] += 1
        else:
            count[2] += 1
            count[3] -= 1
print(ans)