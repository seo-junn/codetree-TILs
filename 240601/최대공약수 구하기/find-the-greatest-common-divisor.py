def gcd(n,m):
    if m <= 1: return n
    n, m = m, n%m
    return gcd(n,m)

n,m = map(int,input().split())
print(gcd(n,m))