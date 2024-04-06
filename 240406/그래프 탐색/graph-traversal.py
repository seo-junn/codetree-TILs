import sys

N, M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s-1].append(e-1)
    graph[e-1].append(s-1)

visited = [0]*N
count = 0

def search(dot):
    global count
    for next_dot in graph[dot]:
        if visited[next_dot] == 0:
            visited[next_dot] += 1
            count += 1
            search(next_dot)

visited[0] = 1
search(0)

print(count)