N = int(input())
library = list(input().strip())

dist = 0
idx = -1
start = 0
for i in range(1,N):
    if library[i] == '1':
        temp = i-start
        if temp > dist:
            dist = temp
            idx = (start+i)//2
        start = i

library[idx] = '1'

dist = 10000
start = 0
for i in range(1,N):
    if library[i] == '1':
        temp = i-start
        dist = min(dist,temp)
        start = i

print(dist)