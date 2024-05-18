N = int(input())
base = list(map(int,input().split()))
ans = []

while base:
    val = 0
    idx = -1
    for i in range(len(base)):
        if base[i] > val:
            val = base[i]
            idx = i
    ans.append(idx+1)
    base = base[:idx]

print(*ans)