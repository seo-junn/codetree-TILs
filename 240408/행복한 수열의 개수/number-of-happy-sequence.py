import sys

n, m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

count = 0
# row check
for row in range(n):
    target = 0
    target_count = 0
    found = False
    for col in range(n):
        if board[row][col] == target:
            target_count += 1
        else:
            if target_count >= m:
                found = True
                break
            target = board[row][col]
            target_count = 1
    if target_count >= m: found = True
    if found: count += 1

# col check
for col in range(n):
    target = 0
    target_count = 0
    found = False
    for row in range(n):
        if board[row][col] == target:
            target_count += 1
        else:
            if target_count >= m:
                found = True
                break
            target = board[row][col]
            target_count = 1
    if target_count >= m: found = True
    if found: count += 1

print(count)