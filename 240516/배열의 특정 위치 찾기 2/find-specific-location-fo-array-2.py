ans = 0

nums = list(map(int,input().split()))
for i in range(10):
    if i%2: ans += nums[i]
    else: ans -= nums[i]

print(abs(ans))