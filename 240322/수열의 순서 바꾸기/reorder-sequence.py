N = int(input())
nums = list(map(int,input().split()))

for i in range(N-2,-1,-1):
    if nums[i] > nums[i+1]:
        print(i+1)
        break