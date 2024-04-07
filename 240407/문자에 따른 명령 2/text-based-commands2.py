dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y = 0,0
c_dir = 0

command = list(input().strip())

for c in command:
    if c == 'L':
        c_dir = (c_dir-1)%4
    elif c == 'R':
        c_dir = (c_dir+1)%4
    else:
        x += dx[c_dir]
        y += dy[c_dir]

print(x, y)