n = int(input())
base = [1,n]

while base[-1] < 100:
    base.append(base[-1]+base[-2])

print(*base)