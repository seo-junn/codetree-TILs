n = int(input())
base = [n]

cnt = 1 if base[-1]%5 == 0 else 0

while cnt < 2:
    base.append(base[-1]+n)
    if base[-1]%5 == 0: cnt += 1

print(*base)