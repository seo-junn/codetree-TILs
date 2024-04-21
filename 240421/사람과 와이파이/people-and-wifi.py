import sys

n, k = map(int,sys.stdin.readline().split())
people = {}

for pos in map(int,sys.stdin.readline().split()):
    if pos in people: people[pos] += 1
    else: people[pos] = 1

positions = list(sorted(people.keys()))
diffs = []
ans = 0
for i in range(len(positions)-1):
    diffs.append(positions[i+1]-positions[i])
    ans += diffs[-1]
diffs.sort()

k -= 1
while k > 0 and diffs:
    ans -= diffs.pop()
    k -= 1

print(ans)