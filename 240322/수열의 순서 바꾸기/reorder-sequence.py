N = int(input())
nums = list(map(int,input().split()))

def insertion(i,j):
    temp = nums[i]
    for idx in range(i,j):
        nums[idx] = nums[idx+1]
    nums[j] = temp

count = 0
while True:
    if nums[0] == 1:
        idx = -1
        for i in range(N-1):
            if nums[i] > nums[i+1]:
                idx = i
                break
        if idx == -1: break
        insertion(0,idx)
        count += 1
    else:
        idx = 0
        for i in range(1,N):
            if nums[i] == nums[0]-1:
                idx = i
                break
        insertion(0,idx)
        count += 1

print(count)