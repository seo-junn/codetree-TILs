K, N = map(int,input().split())

answer = []

def select(K,depth):
    if depth == 0:
        print(*answer)
        return
    for i in range(1,K+1):
        answer.append(i)
        select(K,depth-1)
        answer.pop()

select(K,N)