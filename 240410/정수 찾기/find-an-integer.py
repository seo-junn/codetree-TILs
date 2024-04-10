import sys

n = int(sys.stdin.readline())
a = set(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
for num in map(int,sys.stdin.readline().split()):
    print(1 if num in a else 0)