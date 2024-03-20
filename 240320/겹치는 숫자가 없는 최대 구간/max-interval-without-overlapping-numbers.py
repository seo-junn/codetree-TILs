n = int(input())
nums = list(map(int,input().split()))

cache = [0]*100001

length = 0

start = 0
for i in range(n):
    if cache[nums[i]] == 0:
        cache[nums[i]] += 1
    else:
        length = max(length,i-start)
        while cache[nums[i]]:
            cache[nums[start]] = 0
            start += 1
        
        cache[nums[i]] += 1

length = max(length,n-start)

print(length)