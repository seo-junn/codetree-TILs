nums = list(map(int,input().split()))

for i in range(len(nums)):
    if nums[i] == 0:
        print(sum(nums[i-3:i]))
        break