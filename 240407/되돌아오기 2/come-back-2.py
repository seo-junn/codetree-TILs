dx = [0,1,0,-1]
dy = [1,0,-1,0]

c_dir = 0
x,y = 0,0
time = 0

command = list(input())
reached = False
for c in command:
    if c == 'L':
        c_dir = (c_dir-1)%4
    elif c == 'R':
        c_dir = (c_dir+1)%4
    else:
        x,y = x+dx[c_dir],y+dy[c_dir]
    time += 1
    if x == 0 and y == 0:
        reached = True
        break

print(time if reached else -1)