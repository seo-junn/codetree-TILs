def gcd(n,m):
    if n == 0: return m
    n,m = m%n,n
    return gcd(n,m)

n,m = map(int,input().split())
print(gcd(n,m))