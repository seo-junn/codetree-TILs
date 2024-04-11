import sys

N = int(sys.stdin.readline())
xs = [0]*1001
ys = [0]*1001
dots = []

for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    xs[x] += 1
    ys[y] += 1
    dots.append((x,y))

cx = 0
x_diff = sys.maxsize
x_target = 0
cy = 0
y_diff = sys.maxsize
y_target = 0
for i in range(1,1001):
    if xs[i]:
        cx += xs[i]
    elif i%2 == 0:
        diff = abs(N-cx-cx)
        if diff < x_diff:
            x_diff = diff
            x_target = i
    if ys[i]:
        cy += ys[i]
    elif i%2 == 0:
        diff = abs(N-cy-cy)
        if diff < y_diff:
            y_diff = diff
            y_target = i

ans = sys.maxsize
for xx in range(-4,5,2):
    for yy in range(-4,5,2):
        counts = [0]*4
        x_line = x_target + xx
        y_line = y_target + yy
        for x, y in dots:
            if x > x_line and y > y_line: counts[0] += 1
            elif x < x_line and y > y_line: counts[1] += 1
            elif x < x_line and y < y_line: counts[2] += 1
            else: counts[3] += 1
        val = max(counts)
        ans = min(ans,val)

print(ans)