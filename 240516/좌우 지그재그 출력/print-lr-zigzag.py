n = int(input())

base = [[0]*n for _ in range(n)]
cnt = 1

for i in range(n):
    for j in range(n):
        base[i][j] = cnt
        cnt += 1

for i in range(n):
    if i%2: print(*base[i][::-1])
    else: print(*base[i])