def gcd(n,m):
    if n == 0: return m
    n,m = m%n,n
    return gcd(n,m)

def lcm(n,m):
    g = gcd(n,m)
    return (n//g)*m

n,m = map(int,input().split())
print(lcm(n,m))