import sys

n = int(sys.stdin.readline())
A = list(sorted(map(int,sys.stdin.readline().split())))
B = list(sorted(map(int,sys.stdin.readline().split())))

print("Yes" if A == B else "No")