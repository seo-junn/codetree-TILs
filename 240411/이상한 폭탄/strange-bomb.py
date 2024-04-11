import sys

N, K = map(int,sys.stdin.readline().split())

bomb_num = -1
window = {}
window_size = 0

bombs = list(map(int,sys.stdin.read().splitlines()))
tail = 0

for i in range(N):
    bomb = bombs[i]

    if bomb in window:
        bomb_num = max(bomb_num,bomb)

    if bomb in window: window[bomb] += 1
    else: window[bomb] = 1
    window_size += 1

    if window_size == K+1:
        window[bombs[tail]] -= 1
        if window[bombs[tail]] == 0: window.pop(bombs[tail])
        tail += 1

print(bomb_num)