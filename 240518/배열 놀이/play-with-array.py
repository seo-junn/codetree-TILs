n,q = map(int,input().split())
nums = list(map(int,input().split()))

for _ in range(q):
    line = list(map(int,input().split()))
    if line[0] == 1:
        print(nums[line[1]-1])
    elif line[0] == 2:
        idx = 0
        for i in range(n):
            if nums[i] == line[1]:
                idx = i+1
                break
        print(idx)
    else:
        print(*nums[(line[1]-1):line[2]])