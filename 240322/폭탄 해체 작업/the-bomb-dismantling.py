import sys

N = int(sys.stdin.readline())
bombs = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
bombs.sort(key=lambda x:(x[1],-x[0]))

total_score = 0
time = 0
for score, tik in bombs:
    if tik > time:
        total_score += score
        time += 1

print(total_score)