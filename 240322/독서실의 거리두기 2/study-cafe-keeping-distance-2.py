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

dist1 = N-1-start

library[idx] = '1'

dist = 100000
start = 0
for i in range(1,N):
    if library[i] == '1':
        dist = min(dist,i-start)
        start = i

print(max(dist,dist1))