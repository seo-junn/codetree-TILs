N = int(input())
nums = list(map(int,input().split()))

count = 0
for i in range(N):
    for j in range(i,N-1):
        if nums[j] > nums[j+1]:
            count += 1
            break

print(count)