import sys
from bisect import bisect_left

n, k, T = sys.stdin.readline().strip().split()
n,k = int(n),int(k)-1

words = []
l = len(T)
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= l and word[:l] == T: words.append(word)

words.sort()
print(words[k])