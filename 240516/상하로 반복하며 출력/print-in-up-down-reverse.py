n = int(input())

base = [[0]*n for _ in range(n)]

for j in range(n):
    if j%2 == 0:
        for i in range(n):
            base[i][j] = i+1
    else:
        for i in range(n-1,-1,-1):
            base[i][j] = n-i

for line in base: print(''.join(list(map(str,line))))