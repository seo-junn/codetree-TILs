board = [input().strip() for _ in range(10)]

lx,ly = 0,0
rx,ry = 0,0
bx,by = 0,0

for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            lx,ly = i,j
        elif board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j

if lx == rx == bx:
    if ly < ry < by or by < ry < ly:
        ans = abs(by-ly)+1
    else:
        ans = abs(by-ly)-1
elif ly == ry == by:
    if lx < rx < bx or bx < rx < lx:
        ans = abs(bx-lx)+1
    else:
        ans = abs(bx-lx)-1
else:
    ans = abs(bx-lx)+abs(by-ly)-1

print(ans)