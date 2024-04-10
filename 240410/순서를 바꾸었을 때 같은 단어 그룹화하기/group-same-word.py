import sys

n = int(sys.stdin.readline())
base = {}
for _ in range(n):
    word = ''.join(sorted(list(sys.stdin.readline().strip())))
    if word in base: base[word] += 1
    else: base[word] = 1

max_count = 0
for key in base.keys():
    if base[key] > max_count:
        max_count = base[key]

print(max_count)