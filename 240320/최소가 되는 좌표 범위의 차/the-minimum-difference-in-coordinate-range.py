import sys
import bisect

N, D = map(int,sys.stdin.readline().split())
dots = {}
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    try:
        dots[y].append(x)
    except:
        dots[y] = [x]

index = list(sorted(dots.keys()))
if index[-1]-index[0] < D:
    print(-1)
    exit(0)

dist = 10**7
for left in range(len(index)):
    right = len(index)-1
    while left < right:
        if index[right] - index[left] >= D:
            for lx in dots[index[left]]:
                lidx = bisect.bisect_left(dots[index[right]],lx)
                ridx = bisect.bisect_right(dots[index[right]],lx)
                if lidx == ridx:
                    dist = min(dist,abs(dots[index[right]][0]-lx),abs(dots[index[right]][-1]-lx))
                else:
                    for idx in range(lidx,ridx):
                        dist = min(dist,abs(dots[index[right]][idx]-lx))
                
        right -= 1

print(dist)

'''
dots = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
dots.sort(key=lambda x: (x[1],x[0]))

if dots[-1][1] - dots[0][1] < D:
    print(-1)
    exit(0)

dist = 10**7

for left in range(N):
    right = N-1
    while left < right:
        if dots[right][1] - dots[left][1] >= D:
            dist = min(dist,abs(dots[left][0]-dots[right][0]))
            right -= 1
        else:
            break

print(dist)
'''