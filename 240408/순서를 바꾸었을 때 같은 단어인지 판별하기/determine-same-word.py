import sys

word1 = ''.join(list(sorted(list(sys.stdin.readline().strip()))))
word2 = ''.join(list(sorted(list(sys.stdin.readline().strip()))))

print("Yes" if word1 == word2 else "No")