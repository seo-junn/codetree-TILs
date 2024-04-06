import sys

N, M = map(int,sys.stdin.readline().split())
graph = [[0]*N for _ in range(N)]

for _ in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s-1][e-1] += 1
    graph[e-1][s-1] += 1

visited = [0]*N

def search(dot):
    for i in range(N):
        if graph[dot][i] and visited[i] == 0:
            visited[i] += 1
            search(i)

search(0)

print(sum(visited)-1)