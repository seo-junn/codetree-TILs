import sys

n = int(sys.stdin.readline())
base = {}
for _ in range(n):
    command,*nums = sys.stdin.readline().split()
    nums = list(map(int,nums))
    if command == 'add':
        base[nums[0]] = nums[1]
    elif command == 'remove':
        base.pop(nums[0])
    else:
        print(base[nums[0]] if nums[0] in base else "None")