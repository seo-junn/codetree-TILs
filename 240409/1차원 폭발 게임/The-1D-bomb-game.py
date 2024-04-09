import sys

N, M = map(int,sys.stdin.readline().split())
bombs = [int(sys.stdin.readline()) for _ in range(N)]

while True:
    exploded = False
    target = 0
    count = 0
    next_bombs = []
    for i in range(len(bombs)):
        if bombs[i] == target:
            count += 1
        else:
            if count < M:
                next_bombs += [target]*count
            else:
                exploded = True
            target = bombs[i]
            count = 1
    if count < M:
        next_bombs += [target]*count
    else:
        exploded = True
    
    if not exploded: break
    bombs = next_bombs

print(len(bombs))
for bomb in bombs: print(bomb)