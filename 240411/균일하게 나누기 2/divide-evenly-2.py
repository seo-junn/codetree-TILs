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
    else:
        diff = abs(N-cx-cx)
        if diff < x_diff:
            x_target = i
            x_diff = diff
    if ys[i]:
        cy += ys[i]
    else:
        diff = abs(N-cy-cy)
        if diff < y_diff:
            y_diff = diff
            y_target = i

counts = [0]*4
for x,y in dots:
    if x > x_target and y > y_target: counts[0] += 1
    elif x < x_target and y > y_target: counts[1] += 1
    elif x < x_target and y < y_target: counts[2] += 1
    else: counts[3] += 1

print(max(counts))