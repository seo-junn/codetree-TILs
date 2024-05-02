a,b = map(int,input().split())
print(*list(range(max(a,b),min(a,b)-1,-1)))