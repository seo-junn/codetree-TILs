import sys

n = int(sys.stdin.readline())
base = []
for _ in range(n):
    name, h, w = sys.stdin.readline().strip().split()
    base.append((name,int(h),int(w)))

base.sort(key=lambda x:(x[1],-x[2]))
for item in base: print(*item)