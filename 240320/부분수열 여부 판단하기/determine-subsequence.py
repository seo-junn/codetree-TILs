import sys

n, m = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

if m > n:
    print("No")
    exit(0)

a_idx = 0
sub = True
for b_idx in range(m):
    while a_idx < n and A[a_idx] != B[b_idx]:
        a_idx += 1
    
    if a_idx == n:
        sub = False
        break
    
    a_idx += 1

print("Yes" if sub else "No")