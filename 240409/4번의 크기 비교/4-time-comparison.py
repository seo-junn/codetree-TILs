a = int(input())
nums = list(map(int,input().split()))

for num in nums:
    print(1 if a>num else 0)