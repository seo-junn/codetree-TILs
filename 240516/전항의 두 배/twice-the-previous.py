base = list(map(int,input().split()))

for _ in range(8):
    base.append(base[-1]+2*base[-2])

print(*base)