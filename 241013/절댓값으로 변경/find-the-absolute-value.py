def modify(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

N = int(input())
nums = list(map(int,input().split()))

modify(nums)

print(*nums)