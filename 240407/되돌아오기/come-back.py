dx = {'N':0,'S':0,'E':1,'W':-1}
dy = {'N':1,'S':-1,'E':0,'W':0}

x, y = 0,0
time = 0
reached = False

for _ in range(int(input())):
    d, dist = input().split()
    for i in range(int(dist)):
        time += 1
        x,y = x+dx[d],y+dy[d]
        if x == 0 and y == 0:
            reached = True
            break
    if reached: break

print(time if reached else -1)