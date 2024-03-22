import sys

C, N = map(int,sys.stdin.readline().split())
reds = [int(sys.stdin.readline()) for _ in range(C)]
blacks = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

reds.sort()
blacks.sort()

r, b = 0, 0
count = 0
while r < C and b < N:
    if reds[r] < blacks[b][0]:
        r += 1
    elif reds[r] > blacks[b][1]:
        b += 1
    else:
        count += 1
        r += 1
        b += 1

print(count)