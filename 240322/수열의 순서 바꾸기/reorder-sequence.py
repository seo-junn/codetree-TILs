N = int(input())
nums = list(map(int,input().split()))

count = 0
for i in range(N-1):
    if nums[i] > nums[i+1]:
        count += i+1

print(count)