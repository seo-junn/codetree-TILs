N, M = map(int,input().split())

base = set()
bus = []
def choose(num):
    if num == 0:
        base.add(tuple(sorted(bus)))
    else:
        for i in range(1,N+1):
            if i not in bus:
                bus.append(i)
                choose(num-1)
                bus.pop()

choose(M)
for item in base:print(*item)