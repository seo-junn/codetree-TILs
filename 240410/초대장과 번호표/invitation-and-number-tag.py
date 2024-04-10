import sys

N, G = map(int,sys.stdin.readline().split())
invited = set([1])

base = []
for _ in range(G):
    length, *group = map(int,sys.stdin.readline().split())
    base.append((length,group))

base.sort(key=lambda x:x[0])

while True:
    n_base = []
    adding = False
    for length, group in base:
        if length > len(invited) + 1:
            n_base.append((length,group))
            continue
        count = 0
        invite = 0
        for p in group:
            if p not in invited:
                count += 1
                invite = p
            if count > 1: break
        if count == 1:
            invited.add(invite)
            adding = True
        elif count > 1:
            n_base.append((length,group))
    if not adding: break
    base = n_base

print(len(invited))