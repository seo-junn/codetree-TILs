import sys

n = int(input())
nums = list(map(int,sys.stdin.read().splitlines()))

def carry(a,b):
    while a and b:
        if a%10 + b%10 >= 10:
            return False
        a //= 10
        b //= 10
    return True

ans = -1
for i in range(n):
    for j in range(i+1,n):
        if carry(nums[i],nums[j]):
            temp = nums[i] + nums[j]
            for k in range(j+1,n):
                if carry(temp,nums[k]):
                    ans = max(ans,temp+nums[k])

print(ans)