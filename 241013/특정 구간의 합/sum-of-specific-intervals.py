n,m = map(int,input().split())
nums = [0] + list(map(int,input().split()))

for i in range(1,n+1):
    nums[i] += nums[i-1]

def cal(a1,a2):
    return nums[a2]-nums[a1-1]

for _ in range(m):
    a1,a2 = map(int,input().split())
    print(cal(a1,a2))