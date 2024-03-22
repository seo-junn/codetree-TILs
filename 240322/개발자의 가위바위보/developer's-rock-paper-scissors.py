N = int(input())

base = [0]*6

for i in range(N):
    game = tuple(map(int,input().split()))
    if game == (1,2) or game == (2,3) or game == (3,1):
        base[1] += 1
        base[2] += 1
        base[5] += 1
    elif game == (2,1) or game == (1,3) or game == (3,2):
        base[0] += 1
        base[3] += 1
        base[4] += 1

print(max(base))