N = int(input())
library = list(input().strip())

start = -1
dist = 0
for i in range(N):
    if library[i] == '1':
        if start == -1:
            start = i
            continue
        temp = i-start
        if dist < temp:
            dist = temp
            idx = (start+i)//2
        start = i

library[idx] = '1'

dist1 = 100000
start = -1
for i in range(N):
    if library[i] == '1':
        if start == -1:
            start = i
            continue
        dist1 = min(dist1,i-start)
        start = i

dist2 = 0
library[idx] = '0'
if library[-1] == '0':
    library[-1] = '1'
    dist2 = 100000
    start = -1
    for i in range(N):
        if start == -1:
            start = i
            continue
        if library[i] == '1':
            dist2 = min(dist2,i-start)
            start = i
    library[-1] = '0'

dist3 = 0
if library[0] == '0':
    library[0] = '1'
    dist3 = 100000
    start = -1
    for i in range(N):
        if start == -1:
            start = i
            continue
        if library[i] == '1':
            dist3 = min(dist3,i-start)
            start = i

print(max(dist1,dist2,dist3))