import sys

a,b = map(int,sys.stdin.readline().split())
base = set(map(int,sys.stdin.readline().split()))

for num in map(int,sys.stdin.readline().split()):
    if num in base: base.remove(num)
    else: base.add(num)

print(len(base))