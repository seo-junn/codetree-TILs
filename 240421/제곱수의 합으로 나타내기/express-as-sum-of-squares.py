base = [n**2 for n in range(70,0,-1)]

count = 0
n = int(input())
for i in range(len(base)):
    if base[i] <= n:
        n -= base[i]
        count += 1

print(count)