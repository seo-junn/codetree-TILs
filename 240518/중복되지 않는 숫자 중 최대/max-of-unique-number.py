ans = -1
duplicate = False

N = int(input())
for n in map(int,input().split()):
    if n > ans:
        ans = n
        duplicate = False
    elif n == ans:
        duplicate = True

print(ans if not duplicate else -1)