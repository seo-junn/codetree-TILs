import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
ans = []

for i in range(len(nums)):
    if i%2 == 0:
        temp = list(sorted(nums[:i+1]))
        ans.append(temp[i//2])

print(*ans)