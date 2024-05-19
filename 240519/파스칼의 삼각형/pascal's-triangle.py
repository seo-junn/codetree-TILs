n = int(input())

base = [1]

for _ in range(n):
    print(*base)
    temp = [1]
    for i in range(1,len(base)):
        temp.append(base[i]+base[i-1])
    temp.append(1)
    base = temp