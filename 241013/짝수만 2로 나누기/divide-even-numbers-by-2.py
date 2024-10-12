def modify(arr):
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            arr[i] //= 2

N = int(input())
nums = list(map(int,input().split()))
modify(nums)

print(*nums)