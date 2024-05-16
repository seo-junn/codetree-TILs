base = []

for n in map(int,input().split()):
    if n == 0: break
    elif n%2: base.append(n+3)
    else: base.append(n//2)

print(*base)