N = int(input())
nums = list(sorted(map(int,input().split()),reverse=True))
print(*nums[:2])