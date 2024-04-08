n = int(input())
nums = list(sorted(map(int,input().split())))
print(*nums)
print(*nums[::-1])