n,m = map(int,input().split())

ans = [[0]*m for _ in range(n)]

dr = [0,-1,0,1]
dc = [1,0,-1,0]

pr,pc,c_dir = 0,0,0
num = 1
ans[pr][pc] = num
num += 1
while num <= n*m:
    nr,nc = pr+dr[c_dir],pc+dc[c_dir]
    if 0 <= nr < n and 0 <= nc < m and ans[nr][nc] == 0:
        pr,pc = nr,nc
        ans[pr][pc] = num
        num += 1
    else:
        c_dir = (c_dir+1)%4

for line in ans: print(*line)