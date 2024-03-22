n = int(input())

count = 0

def ccount(depth):
    if depth < 0: return
    if depth == 0:
        global count
        count += 1
    else:
        for i in range(1,5):
            ccount(depth-i)

ccount(n)
print(count)