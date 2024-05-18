n = int(input())

base = [[0]*n for _ in range(n)]
num = 0

for i in range(n):
    for j in range(n):
        num += 1
        base[j][i] = num

for line in base: print(*line)