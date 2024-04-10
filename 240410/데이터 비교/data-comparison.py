import sys

n = int(sys.stdin.readline())
base = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

ans = []
for num in arr:
    if num in base:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)