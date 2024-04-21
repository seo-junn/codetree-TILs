a,b = map(int,input().split())

res = str(a//b)+'.'

if a > b:
    a %= b
for _ in range(20):
    if a > 0:
        a *= 10
        res += str(a//b)
        if a > b: a %= b
    else: res += '0'
    

print(res)