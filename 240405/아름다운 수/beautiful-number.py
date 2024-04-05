n = int(input())

def find(n):
    if n == 0: return 1
    res = 0
    for i in range(1,5):
        if n >= i:
            res += find(n-i)
    return res

print(find(n))