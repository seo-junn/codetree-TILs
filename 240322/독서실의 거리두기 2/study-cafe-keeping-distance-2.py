N = int(input())
library = list(input().strip())

start = 0
dist = 0
for i in range(N):
    if library[i] == '1':
        temp = i-start
        if dist < temp:
            dist = temp
            idx = (start+i)//2
        start = i

library[idx] = '1'

dist1 = 100000
start = 0
for i in range(1,N):
    if library[i] == '1':
        dist1 = min(dist1,i-start)
        start = i

dist2 = 0
library[idx] = '0'
if library[-1] == '0':
    library[-1] = '1'
    dist2 = 100000
    start = 0
    for i in range(1,N):
        if library[i] == '1':
            dist2 = min(dist2,i-start)
            start = i

print(max(dist1,dist2))