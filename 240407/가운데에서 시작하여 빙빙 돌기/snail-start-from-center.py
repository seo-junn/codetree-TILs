import sys

n = int(sys.stdin.readline())
ans = [[0]*n for _ in range(n)]

pr,pc = n//2,n//2
step_size = 1
step_cnt = 0
step_chk = 0

dr = [0,-1,0,1]
dc = [1,0,-1,0]
c_dir = 0

num = 1
ans[pr][pc] = num
step_cnt
num += 1

while num <= n**2:
    nr,nc = pr+dr[c_dir],pc+dc[c_dir]
    pr,pc = nr,nc
    ans[pr][pc] = num
    num += 1
    step_chk += 1
    if step_chk == step_size:
        c_dir = (c_dir+1)%4
        step_cnt += 1
        step_chk = 0
    if step_cnt == 2:
        step_size += 1
        step_cnt = 0

for line in ans: print(*line)