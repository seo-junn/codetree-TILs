import sys

n,m = map(int,sys.stdin.readline().split())
base = {}
for i in range(1,n+1):
    word = sys.stdin.readline().strip()
    base[word] = i
    base[str(i)] = word

for _ in range(m):
    target = sys.stdin.readline().strip()
    print(base[target])