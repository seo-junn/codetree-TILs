n = int(input())

res = [n]
temp = n
for _ in range(4):
    temp += n
    res.append(temp)

print(*res)