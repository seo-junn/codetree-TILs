N = int(input())
nums = list(map(int,input().split()))

for i in range(N):
    if nums[i]%2 == 0:
        nums[i] //= 2

print(*nums)