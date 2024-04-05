n = int(input())

cache = [-1]*(n+1)
cache[0] = 1
def find(n):
    if cache[n] != -1:
        return cache[n]
    res = 0
    for i in range(1,5):
        if n >= i:
            res += find(n-i)
    cache[n] = res
    return res

print(find(n))