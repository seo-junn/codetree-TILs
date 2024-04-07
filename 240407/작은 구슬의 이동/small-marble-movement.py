import sys

dr = {'U':-1,'D':1,'L':0,'R':0}
dc = {'U':0,'D':0,'L':-1,'R':1}
chdir = {'U':'D','D':'U','L':'R','R':'L'}

n, t = map(int,sys.stdin.readline().split())
r,c,d = sys.stdin.readline().split()
r = int(r)-1
c = int(c)-1

while t > 0:
    t -= 1
    nr,nc = r+dr[d],c+dc[d]
    if 0 <= nr < n and 0 <= nc < n:
        r,c = nr,nc
    else:
        d = chdir[d]

print(r+1,c+1)