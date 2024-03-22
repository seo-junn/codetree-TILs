n, k = map(int,input().split())
nums = list(map(int,input().split()))

now = sum(nums[:k])
ans = now
start = 0
end = k

while end < n:
    now -= nums[start]
    now += nums[end]
    ans = max(ans,now)
    start += 1
    end += 1

print(ans)