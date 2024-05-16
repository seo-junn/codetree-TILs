n = int(input())
base = []
for num in map(int,input().split()):
    if num%2 == 0: base.append(num)

print(*base[::-1])