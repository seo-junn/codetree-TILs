nums = list(map(int,input().split()))

base = 0
cnt = 0

for n in nums:
    if n:
        base += n
        cnt += 1
    else:
        break

print(base,f'{base/cnt:.1f}')