som,avg,cnt = 0,0,0

nums = list(map(int,input().split()))
for i in range(10):
    if i%2: som += nums[i]
    if i%3 == 2:
        avg += nums[i]
        cnt += 1

print(som,f'{avg/cnt:.1f}')