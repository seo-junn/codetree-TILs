import sys
from collections import Counter

word = sys.stdin.readline().strip()
base = Counter(word)

ans = ''
for c in word:
    if base[c] == 1:
        ans += c
        break

print(ans if ans else "None")