import sys

n = int(sys.stdin.readline())
nums = list(sorted(map(int,sys.stdin.readline().split())))

left = 0
right = n-1
ans = 2*10**9

while left < right:
    now = nums[left] + nums[right]
    if now > 0:
        right -= 1
    elif now < 0:
        left += 1
    else:
        print(0)
        exit(0)
    ans = min(ans,abs(now))

print(ans)