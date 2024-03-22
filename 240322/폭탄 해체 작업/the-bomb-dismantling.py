import sys

N = int(sys.stdin.readline())
bombs = []
max_time = 0
for _ in range(N):
    sc, tc = map(int,sys.stdin.readline().split())
    bombs.append((sc,tc))
    if tc > max_time:
        max_time = tc

timeline = [0]+[0]*max_time
bombs.sort(key=lambda x:(-x[0],-x[1]))

total_score = 0
for score, tik in bombs:
    if timeline[tik] == 0:
        timeline[tik] += 1
        total_score += score
    else:
        for i in range(tik,0,-1):
            if timeline[i] == 0:
                timeline[i] += 1
                total_score += score
                break

print(total_score)