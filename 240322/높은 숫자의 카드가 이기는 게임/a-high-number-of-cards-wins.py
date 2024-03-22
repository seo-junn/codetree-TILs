import sys

N = int(sys.stdin.readline())
cards = [0] + [1]*(2*N)

B = []
for i in range(N):
    c = int(sys.stdin.readline())
    B.append(c)
    cards[c] -= 1

B.sort()

A_idx = 1
B_idx = 0

score = 0
while B_idx < N and A_idx < 2*N+1:
    if cards[A_idx] and B[B_idx] < A_idx:
        cards[A_idx] -= 1
        B_idx += 1
        score += 1
    A_idx += 1

print(score)