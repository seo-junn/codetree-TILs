nums = list(map(int,input().split()))

base = []
for n in nums:
    if n: base.append(n)
    else: break

print(*base[::-1])