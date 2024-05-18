n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
B = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        A[i][j] = 0 if A[i][j] == B[i][j] else 1

for line in A: print(*line)