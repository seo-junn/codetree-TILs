import sys

n = int(sys.stdin.readline())
base = {}

for _ in range(n):
    word = sys.stdin.readline().strip()
    if word in base: base[word] += 1
    else: base[word] = 1

print(max(base.values()))