N = int(input())
base = set()
nums = set()

for n in map(int,input().split()):
    if n in base:
        if n in nums: nums.remove(n)
    else:
        base.add(n)
        nums.add(n)

print(max(nums) if nums else -1)