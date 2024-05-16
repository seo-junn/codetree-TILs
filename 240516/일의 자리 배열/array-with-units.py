base = list(map(int,input().split()))

for i in range(8):
    base.append((base[-1]+base[-2])%10)

print(*base)