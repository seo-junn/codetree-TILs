nums = list(map(int,input().split()))

base = 0
cnt = 0
for i in range(10):
    if nums[i] >= 250:
        break
    else:
        base += nums[i]
        cnt += 1

print(base,f'{base/cnt:.1f}')