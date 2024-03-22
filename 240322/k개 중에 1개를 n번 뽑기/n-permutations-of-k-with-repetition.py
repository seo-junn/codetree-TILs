K, N = map(int,input().split())

arr = []

def make(depth):
    if depth == 0:
        print(*arr)
    else:
        for i in range(1,K+1):
            arr.append(i)
            make(depth-1)
            arr.pop()

make(N)