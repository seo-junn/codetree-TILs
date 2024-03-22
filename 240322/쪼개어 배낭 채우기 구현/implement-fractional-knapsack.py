import sys

N, M = map(int,sys.stdin.readline().split())
jewels = []

for _ in range(N):
    w,v = map(int,sys.stdin.readline().split())
    jewels.append((w,v,v/w))

jewels.sort(key=lambda x:-x[-1])

val = 0
jew = 0
while M > 0:
    if jewels[jew][0] < M:
        M -= jewels[jew][0]
        val += jewels[jew][1]
        jew += 1
    else:
        val += jewels[jew][2]*M
        M = 0

print("%.3f"%val)