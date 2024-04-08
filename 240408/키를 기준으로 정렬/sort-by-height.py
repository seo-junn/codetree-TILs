n = int(input())
base = []

for _ in range(n):
    name,height,weight = input().split()
    base.append((name,int(height),int(weight)))

base.sort(key=lambda x:x[1])

for item in base: print(*item)