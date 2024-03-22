N = int(input())
base = []
for _ in range(N):
    pos, card = input().strip().split()
    base.append((int(pos),card))

base.sort()

ans = 0
for left in range(N):
    for right in range(left,N):
        G, H = 0,0
        for i in range(left,right+1):
            if base[i][1] == 'G': G += 1
            else: H += 1
        if G == 0 or H == 0 or G == H:
            ans = max(ans,base[right][0]-base[left][0])

print(ans)