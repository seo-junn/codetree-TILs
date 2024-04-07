from collections import deque

N = int(input())
cache = [-1]*(2*N+1)

q = deque()
q.append(N)
cache[N] = 0

while q:
    cn = q.popleft()
    if cn == 1: break
    nn = cn + 1
    if 0 <= nn <= 2*N and cache[nn] == -1:
        cache[nn] = cache[cn]+1
        q.append(nn)
    nn = cn - 1
    if 0 <= nn <= 2*N and cache[nn] == -1:
        cache[nn] = cache[cn]+1
        q.append(nn)
    if cn%2 == 0:
        nn = cn // 2
        if 0 <= nn <= 2*N and cache[nn] == -1:
            cache[nn] = cache[cn]+1
            q.append(nn)
    if cn%3 == 0:
        nn = cn // 3
        if 0 <= nn <= 2*N and cache[nn] == -1:
            cache[nn] = cache[cn]+1
            q.append(nn)

print(cache[1])