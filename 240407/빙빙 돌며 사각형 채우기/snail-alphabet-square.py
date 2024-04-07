alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
idx = 0

n, m = map(int,input().split())
ans = [['']*m for _ in range(n)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

c_dir = 0

pr,pc = 0,0
ans[pr][pc] = alp[idx]
idx = (idx+1)%26


while idx < n*m:
    nr,nc = pr+dr[c_dir],pc+dc[c_dir]
    if 0 <= nr < n and 0 <= nc < m and ans[nr][nc] == '':
        pr,pc = nr,nc
        ans[pr][pc] = alp[idx%26]
        idx += 1
    else:
        c_dir = (c_dir+1)%4

for line in ans: print(*line)